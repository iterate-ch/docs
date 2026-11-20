Configure Public Key Authentication for SFTP using a PKCS#11 Smartcard
====

> Public-key authentication with a smartcard allows you to connect to a remote server without a password. The private key is kept on the card and never leaves it. A _PKCS#11_ module, the native library shipped with the driver of your card, is used to read the public keys from the card and to sign the login with the corresponding private key protected by a PIN. This is the equivalent of `ssh -I /path/to/module.so`.

:::{important}
* Cyberduck [9.7.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [6.0.0](https://mountainduck.io/changelog/) or later required
:::

:::{note}
Only keys with a matching certificate on the card are found. Cards holding a key without a certificate, such as a key generated with `pkcs11-tool --keypairgen` only, cannot be used.
:::

## Setup

:::::{tabs}
::::{group-tab} macOS

1. Install the _PKCS#11_ module for your card. [OpenSC](https://github.com/OpenSC/OpenSC) supports many cards including _PIV_, _CAC_ and _OpenPGP_ cards and hardware tokens such as a _YubiKey_ with the _PIV_ application.
   ```
   brew install opensc
   ```

   :::{tip}
   Cyberduck already bundles _OpenSC_ and uses it by default. The installation is only required for the command line tools used in the following steps to read the public key from the card and to verify the setup with OpenSSH.
   :::

   :::{warning}
   The module `/usr/lib/ssh-keychain.dylib` included with macOS for a smartcard paired with `sc_auth pair` can only be loaded by `ssh` and is not supported in Cyberduck and Mountain Duck.
   :::

2. Verify the module can read the certificates from the card. Insert the card first.
   ```
   pkcs11-tool --module /opt/homebrew/lib/opensc-pkcs11.so --list-objects --type cert
   ```

3. Print the public keys on the card and save them to a file.
   ```
   ssh-keygen -D /opt/homebrew/lib/opensc-pkcs11.so > ~/.ssh/smartcard.pub
   ```

   The command prints a line for every key on the card. Edit the file to only keep the line with the key to authenticate with.

4. Add the public key to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.
   ```
   ssh-copy-id -fi ~/.ssh/smartcard.pub user@remotehost
   ```

5. Verify the setup with OpenSSH before connecting with Cyberduck. You are prompted for the PIN of the card.
   ```
   ssh -I /opt/homebrew/lib/opensc-pkcs11.so user@remotehost
   ```

6. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_ because the keys are read from the card.

7. In _SSH Private Key_ select the public key `smartcard.pub` saved in step 3 to only offer the matching key on the card to the server.

   :::{tip}
   With no key selected, every key on the card is offered to the server in turn. The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when the card holds several keys.
   :::

8. Connect to the server and enter the PIN of the card when prompted. The PIN is requested once and the card remains unlocked until you quit the application.

::::
::::{group-tab} Windows

1. Install the _PKCS#11_ module for your card. No module is bundled with Cyberduck on Windows. [OpenSC](https://github.com/OpenSC/OpenSC/releases) supports many cards including _PIV_, _CAC_ and _OpenPGP_ cards and hardware tokens such as a _YubiKey_ with the _PIV_ application. Choose the 64-bit installer.

2. Set the [hidden configuration option](hidden_properties.md) `connection.keystore.pkcs11.library` to the path of the module and restart Cyberduck. Write the path with forward slashes.
   ```
   connection.keystore.pkcs11.library=C:/Program Files/OpenSC Project/OpenSC/pkcs11/opensc-pkcs11.dll
   ```

3. Add the public key of the key on the card to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH. The public key is usually provided by the issuer of the card or can be read from the card with `ssh-keygen -D` and the path of the module.

4. Add a new [Bookmark](../cyberduck/bookmarks.md). Enter the hostname in _Server_. You do **not** need to set a value for _Password_ because the keys are read from the card.

5. In _SSH Private Key_ select the file with the public key to only offer the matching key on the card to the server.

   :::{tip}
   With no key selected, every key on the card is offered to the server in turn. The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when the card holds several keys.
   :::

6. Connect to the server and enter the PIN of the card when prompted. The PIN is requested once and the card remains unlocked until you quit the application.

   :::{note}
   A card connected to the Windows computer is not available in a _Remote Desktop_ session. Connect the card to the computer running the Remote Desktop client instead and enable the redirection of smart cards.
   :::

::::
:::::

## Use a Different Module

The bundled _OpenSC_ module is used by default on macOS. To use the module from the vendor of your card instead, refer to it in your OpenSSH configuration file `~/.ssh/config`. On Windows, set the path of the module with the hidden configuration option as described above.

```
Host *
    PKCS11Provider /path/to/module.so
```

This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck. You can restrict the setting to a single alias in the configuration file instead of matching it for all connections with `*`. Alternatively set the [hidden configuration option](hidden_properties.md) `connection.keystore.pkcs11.library` to the absolute path of the module.

## Limit Connections Using the Card

With a card inserted, the keys on the card are attempted for every connection before a private key file or the prompt for a password. You are prompted for the PIN of the card including for servers you do not log in to with a key on the card, unless a password is saved for the bookmark or the login succeeds with an identity from the SSH agent.

- Cancel the prompt for the PIN to skip the card. The login continues with the private key file selected in the bookmark or the prompt for a password.
- Select a private key file for _SSH Private Key_ in the [Bookmark](../cyberduck/bookmarks.md). The card is not used and there is no prompt for the PIN.
- Set `PKCS11Provider none` for the host in `~/.ssh/config` to not use the card.
- Set `IdentitiesOnly yes` for the host in `~/.ssh/config`. Only the key on the card matching the public key file set with `IdentityFile` is offered and the card is not used when `IdentityFile` is missing or set to a private key file.
  ```
  Host remotehost
      IdentityFile ~/.ssh/smartcard.pub
      IdentitiesOnly yes
  ```
- Set the [hidden configuration option](hidden_properties.md) `ssh.authentication.pkcs11.enable` to `false` to disable authentication with a smartcard for all connections.

## Troubleshooting

:::{warning}
When no key from the card is offered, verify the card holds a certificate for the key with `pkcs11-tool --module <module> --list-objects --type cert`. A key without a certificate on the card is not found. When a public key file is selected in the bookmark, verify it matches a key on the card.
:::

:::{warning}
When the connection continues with a prompt for a password with no prompt for the PIN before, no card was found or the module could not be loaded. Verify the card is inserted and that a path set with `PKCS11Provider` works with `ssh -I`. On Windows, verify the path set with `connection.keystore.pkcs11.library`.
:::

:::{note}
Removing the card while connected fails the session. Reconnect with the card inserted.
:::

## References

- [OpenSC supported hardware](https://github.com/OpenSC/OpenSC/wiki/Supported-hardware-%28smart-cards-and-USB-tokens%29)
- [`PKCS11Provider` in ssh_config](https://man.openbsd.org/ssh_config#PKCS11Provider)
- [Client certificate on a smartcard](../protocols/webdav/index.md#client-certificate-on-smartcard) for mutual TLS with WebDAV.
- [Use a FIDO2 Security Key](sftp_publickeyauth_securitykey.md) for authentication with a key in the Secure Enclave or on a hardware token such as a YubiKey.
