Configure Public Key Authentication for SFTP using a PKCS#11 Smartcard
====

> Public-key authentication with a smartcard allows you to connect to a remote server without a password. The private key is kept on the card and never leaves it. A _PKCS#11_ module, the native library shipped with the driver of your card, is used to read the public keys from the card and to sign the login with the corresponding private key protected by a PIN. This is the equivalent of `ssh -I /path/to/module.so`.

:::{important}
* Cyberduck [9.6.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [6.0.0](https://mountainduck.io/changelog/) or later required
:::

:::{note}
Only keys with a matching certificate on the card are found. Cards holding a key without a certificate, such as a key generated with `pkcs11-tool --keypairgen` only, cannot be used.
:::

## Setup

:::::{tabs}
::::{group-tab} macOS

1. Install the _PKCS#11_ module for your card. [OpenSC](https://github.com/OpenSC/OpenSC) supports many cards including _PIV_, _CAC_ and _OpenPGP_ cards.
   ```
   brew install opensc
   ```

   :::{tip}
   Cyberduck and Mountain Duck already bundle _OpenSC_. Refer to the bundled library by its file name `opensc-pkcs11.so` instead of an absolute path when configuring the module. For a smartcard paired with macOS using `sc_auth pair`, the system module `/usr/lib/ssh-keychain.dylib` can be used instead.
   :::

2. Verify the module can read the certificates from the card. Insert the card first.
   ```
   pkcs11-tool --module /opt/homebrew/lib/opensc-pkcs11.so --list-objects --type cert
   ```

3. Print the public keys on the card and save them to a file.
   ```
   ssh-keygen -D /opt/homebrew/lib/opensc-pkcs11.so > ~/.ssh/smartcard.pub
   ```

4. Add the public key to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.
   ```
   ssh-copy-id -fi ~/.ssh/smartcard.pub user@remotehost
   ```

5. Verify the setup with OpenSSH before connecting with Cyberduck. You are prompted for the PIN of the card.
   ```
   ssh -I /opt/homebrew/lib/opensc-pkcs11.so user@remotehost
   ```

6. Refer to the module in your OpenSSH configuration file `~/.ssh/config`.
   ```
   Host *
       PKCS11Provider /opt/homebrew/lib/opensc-pkcs11.so
   ```

   This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck. You can restrict the setting to a single alias in the configuration file instead of matching it for all connections with `*`. Alternatively set the [hidden configuration option](hidden_properties.md) `ssh.authentication.pkcs11.library` to the path of the module or to `opensc-pkcs11.so` for the bundled version.

7. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_ or select a _SSH Private Key_ because the keys are read from the card.

   :::{tip}
   The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when the card holds several keys. Select the public key saved in step 3 for _SSH Private Key_ to only offer the matching identity.
   :::

8. Connect to the server and enter the PIN of the card when prompted.

::::
:::::

## Troubleshooting

:::{warning}
When no key from the card is offered, verify the card holds a certificate for the key with `pkcs11-tool --module <module> --list-objects --type cert`. A key without a certificate on the card is not found.
:::

:::{warning}
When the connection continues with a prompt for a password, the module could not be loaded. Verify the path set with `PKCS11Provider` and that the same path works with `ssh -I`.
:::

:::{note}
Removing the card while connected fails the session. Reconnect with the card inserted.
:::

## References

- [OpenSC supported hardware](https://github.com/OpenSC/OpenSC/wiki/Supported-hardware-%28smart-cards-and-USB-tokens%29)
- [`PKCS11Provider` in ssh_config](https://man.openbsd.org/ssh_config#PKCS11Provider)
- [Use a FIDO2 Security Key](sftp_publickeyauth_securitykey.md) for authentication with a key in the Secure Enclave or on a hardware token such as a YubiKey.
