Connect to Azure Blob Storage with SFTP
====

> Azure Blob Storage provides an [SFTP endpoint](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support) for storage accounts with the hierarchical namespace enabled. This tutorial describes how to enable SFTP in the Azure Portal and connect with Cyberduck or Mountain Duck, either with a [local user](#local-user-with-password-or-private-key) authenticating with a password or an SSH private key, or with a [Microsoft Entra ID](#ssh-certificate-with-microsoft-entra-id) account authenticating with an SSH certificate and no local users.

:::{admonition} Authentication with an SSH certificate
:class: important

- Cyberduck [9.6.0](https://cyberduck.io/changelog/) or later required
- Mountain Duck [5.4.0](https://mountainduck.io/changelog/) or later required
:::

## Prerequisites

- A *standard general-purpose v2* or *premium block blob* storage account with the [hierarchical namespace](https://learn.microsoft.com/en-us/azure/storage/blobs/upgrade-to-data-lake-storage-gen2-how-to) (Azure Data Lake Storage Gen2) enabled. The *SFTP* setting is not shown for other accounts.
- Permission to change the storage account in the [Azure Portal](https://portal.azure.com/).

:::{note}
SFTP support is billed hourly for as long as it is enabled on the storage account. Select _Disable SFTP_ in the _SFTP_ settings of the storage account when not in use.
:::

## Enable SFTP

1. Sign in to the [Azure Portal](https://portal.azure.com/) and open your **Storage account**.
2. Under _Settings_, select **SFTP**.
3. Select **Enable SFTP**.

The endpoint for SFTP is the Blob Storage endpoint `<storageaccount>.blob.core.windows.net`. The Data Lake Storage endpoint `<storageaccount>.dfs.core.windows.net` is *not* supported.

## Local User with Password or Private Key

Azure does not accept shared access signatures (SAS) for SFTP. A *local user* in the storage account is the identity to authenticate with a password or an SSH key pair. Password and key can both be enabled for a user but the client authenticates with only one of them. Requiring both is not supported.

### Azure Portal

1. Open the storage account, select **SFTP** under _Settings_ and select **Add local user**.
2. Enter a _Username_ such as `sftpuser`.
3. Select the authentication method. Select **SSH Password**, **SSH Key pair** or both.
   - For *SSH Key pair* choose a _Public key source_:
     - **Generate a new key pair**. Enter a key name. The private key is offered for download after you add the user.
     - **Use existing public key**. Paste the public key in OpenSSH format such as `ssh-rsa AAAAB3N...` generated with `ssh-keygen`. Other formats such as PuTTY `.ppk` must be converted first.
     - **Use existing key stored in Azure**.
4. Select **Next**. On the _Permissions_ tab choose the **Container** to make available and the permissions *Read*, *Write*, *List*, *Delete*, *Create*, *Modify Ownership* and *Modify Permissions*. Grant at least *Read* and *List* for browsing and *Write*, *Create* and *Delete* for upload and removal.
5. Enter a _Home directory_ such as `mycontainer` or `mycontainer/mydirectory`. Optionally select **Allow ACL authorization** to authorize with POSIX ACLs of files and directories in the container.
6. Select **Add**.
   - For *SSH Password*, a generated password of at least 32 characters is shown **once**. Copy it. It cannot be retrieved later but only regenerated with _Reset password_ in the local user.
   - For a new key pair, select **Download** to save the private key such as `sftpuser.pem`. Move it to `~/.ssh/` and restrict its permissions on macOS with `chmod 600 ~/.ssh/sftpuser.pem`.

:::{important}
The local user must be granted at least one permission on the container it connects to. Otherwise the login fails.
:::

### Cyberduck or Mountain Duck

1. Add a new [Bookmark](../cyberduck/bookmarks.md) (_Bookmark → New Bookmark_ in Cyberduck) or connection in Mountain Duck and choose **SFTP (SSH File Transfer Protocol)**.
2. Enter the following.

   | Field    | Value                                                                                      |
   |----------|--------------------------------------------------------------------------------------------|
   | Server   | `<storageaccount>.blob.core.windows.net`                                                   |
   | Port     | `22`                                                                                       |
   | Username | `<storageaccount>.<username>` such as `contoso4.sftpuser`                                  |

   :::{note}
   If you did not set a home directory for the user, include the container in the username as `<storageaccount>.<container>.<username>` such as `contoso4.mycontainer.sftpuser`.
   :::

3. Choose the authentication method.
   - **Password**. Paste the generated password in _Password_ and leave _SSH Private Key_ set to _None_. Alternatively leave _Password_ empty and enter it when prompted, then choose _Save Password_ to store it in the keychain.
   - **Private key**. Leave _Password_ empty and in _SSH Private Key_ choose _Choose…_ and select the downloaded private key such as `~/.ssh/sftpuser.pem`. For a key protected with a passphrase, enter the passphrase when prompted. Refer to [Configure Public Key Authentication](sftp_publickeyauth.md) for details.

4. Close the bookmark and connect. Verify the host key presented by the server against the [published host keys](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-host-keys) before choosing _Allow_.

:::{tip}
The container is displayed at the root of the connection if no home directory is set for the local user and not part of the username. Navigate into it to see the blobs.
:::

## SSH Certificate with Microsoft Entra ID

Authenticating with Microsoft Entra ID replaces local users with your existing identities including multi-factor authentication, [Azure RBAC](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control-model) and ACLs. You sign in to Entra ID, obtain a short-lived OpenSSH certificate signed for your account and present the certificate with its private key to the SFTP endpoint. No local user is required and none is used. Passwords are not supported with Entra ID.

:::{important}
* Only **RSA** keys and certificates are supported. ECDSA and Ed25519 keys cannot be used.
* The certificate is valid for only **65 minutes**. Request a new certificate when it expires.
* Managed identities, a home directory and the container name in the username are not supported.
:::

### Azure Portal

1. Open the storage account and make sure **SFTP** is enabled as described [above](#enable-sftp).
2. To disable password and key access with local users, remove every local user: select **SFTP** under _Settings_, select the local users and choose **Delete**. Without local users the SFTP endpoint accepts only Entra ID certificates.
3. Grant the Entra ID user, group or service principal a data role on the storage account or the container. Select **Access Control (IAM) → Add → Add role assignment** and choose **Storage Blob Data Contributor** (read and write), **Storage Blob Data Owner** (additionally required to change ownership) or **Storage Blob Data Reader** (read only). On the _Members_ tab select the user. Role assignments can take a few minutes to apply.

:::{note}
The permission *Storage Blob Data Contributor* is required even for the account owner. The Azure roles *Owner* or *Contributor* do not grant access to data.
:::

### Obtain the Certificate

Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and sign in.

1. Generate an RSA key pair in PEM format unless you already have one. Use the `-m PEM` option to create the private key in a format supported by Cyberduck.
   ```
   ssh-keygen -m PEM -t rsa -b 4096 -f ~/.ssh/azure_sftp
   ```
2. Sign in to Entra ID.
   ```
   az login
   ```
3. Request the certificate for the public key. Save the certificate next to the private key and suffixed with `-cert.pub`, the filename Cyberduck and Mountain Duck look for.
   ```
   az sftp cert --public-key-file ~/.ssh/azure_sftp.pub --file ~/.ssh/azure_sftp-cert.pub
   ```

   On Windows, the equivalent with Azure PowerShell and the module [Az.Sftp](https://www.powershellgallery.com/packages/Az.Sftp) is
   ```
   Connect-AzAccount
   New-AzSftpCertificate -PublicKeyFile "$HOME\.ssh\azure_sftp.pub" -CertificatePath "$HOME\.ssh\azure_sftp-cert.pub"
   ```

### Cyberduck or Mountain Duck

1. Add a new [Bookmark](../cyberduck/bookmarks.md) or connection and choose **SFTP (SSH File Transfer Protocol)** with the following settings.

   | Field    | Value                                                 |
   |----------|-------------------------------------------------------|
   | Server   | `<storageaccount>.blob.core.windows.net`              |
   | Username | `<storageaccount>.<username>` such as `contoso4.jdoe` |

   Use the username from the _Principals_ of the certificate **without** the domain. For the account `jdoe@example.com` the username is `jdoe`. For a service principal use its ID in place of the username. Do not add the container name.

   :::{tip}
   The _Principals_ section lists the username to connect with and _Valid_ the expiration.
   ```
   ssh-keygen -L -f ~/.ssh/azure_sftp-cert.pub
   ```
   :::

2. In _SSH Private Key_ choose _Choose…_ and select the private key `~/.ssh/azure_sftp`. Leave _Password_ empty. The signed certificate `~/.ssh/azure_sftp-cert.pub` is picked up from the folder of the private key and sent to the server with the key.
3. Choose _Connect_. The root of the connection lists all containers you have access to.

:::{warning}
The `CertificateFile` directive in `~/.ssh/config` is not supported. The certificate *must* reside next to the private key. Refer to [OpenSSH User Certificate Authentication](../protocols/sftp/index.md#openssh-user-certificate-authentication).
:::

:::{tip}
After 65 minutes the certificate expires and the login fails with an authentication error. Repeat step 3 of [Obtain the Certificate](#obtain-the-certificate) to replace the file `azure_sftp-cert.pub`; the bookmark does not need to be changed. Reconnect open connections afterwards.
:::

## Troubleshooting

Verify the login with OpenSSH to inspect the reason for the failure. 

* For a local user, run 
```
sftp -v contoso4.sftpuser@contoso4.blob.core.windows.net
```

* For an Entra ID certificate, run
```
sftp -v -o PubkeyAcceptedAlgorithms=rsa-sha2-256-cert-v01@openssh.com,rsa-sha2-256 -o IdentityFile=~/.ssh/azure_sftp -o CertificateFile=~/.ssh/azure_sftp-cert.pub contoso4.jdoe@contoso4.blob.core.windows.net
```

## References

- [SSH File Transfer Protocol (SFTP) in Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support)
- [Enable or disable SFTP in Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support-how-to)
- [Authorize SFTP access to Azure Blob Storage with local users](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support-authorize-access)
- [Authorize SFTP access to blobs using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support-entra-id-based-access)
- [Connect to Azure Blob Storage from an SFTP client](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support-connect)
