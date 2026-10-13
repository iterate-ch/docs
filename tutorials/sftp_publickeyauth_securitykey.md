Configure Public Key Authentication for SFTP using a FIDO2 Security Key
====

> Public-key authentication with a _FIDO2_ security key allows you to connect to a remote server without a password. The private key never leaves the authenticator, which is either the Secure Enclave of your Mac unlocked with _Touch ID_ or a hardware token such as a _YubiKey_ you touch to confirm. OpenSSH calls these keys `sk-ecdsa-sha2-nistp256@openssh.com` and `sk-ssh-ed25519@openssh.com`.

:::{important}
* Cyberduck [9.6.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [6.0.0](https://mountainduck.io/changelog/) or later required
:::

The key file in `~/.ssh` holds a reference to the credential on the authenticator but no private key. Signing a login is therefore delegated either to a _security key provider_ library talking to the authenticator or to an [SSH agent](#let-an-ssh-agent-handle-the-security-key) holding the key.

:::{note}
A security key provider library is configured by default on macOS only, serving keys in the Secure Enclave. On Windows and Linux OpenSSH talks to a token with built-in USB HID support instead of a library, which Cyberduck cannot load. Leave the key to an [SSH agent](#let-an-ssh-agent-handle-the-security-key) there, or set `SecurityKeyProvider` to a middleware library for your token.
:::

:::{important}
The server must run _OpenSSH 8.2_ or later. Earlier versions do not know the `sk-*` key types and ignore the entry in `authorized_keys`. Verify the version of the server with `ssh -v user@remotehost` and look for the line `remote software version`.
:::

## Create a Key in the Secure Enclave unlocked with Touch ID

:::::{tabs}
::::{group-tab} macOS

1. Create an identity in the Secure Enclave protected with _Touch ID_. The private key is generated on the device and cannot be extracted.
   ```
   sc_auth create-ctk-identity -l "MacBook Touch ID SSH" -k p-256-ne -t bio
   ```

   :::{tip}
   `-k p-256-ne` creates a non-extractable key on the NIST P-256 curve, the only curve supported by the Secure Enclave. `-t bio` requires _Touch ID_ to use the key.
   :::

2. Write the key file for the credential. Run the command in `~/.ssh` as the files are written to the current working directory.
   ```
   cd ~/.ssh && ssh-keygen -w /usr/lib/ssh-keychain.dylib -K
   ```

   This writes `id_ecdsa_sk_rk` and `id_ecdsa_sk_rk.pub`. Repeat the command with `-K` whenever you need the files again on another Mac with access to the same identity.

3. Add the public key to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.
   ```
   ssh-copy-id -fi ~/.ssh/id_ecdsa_sk_rk.pub user@remotehost
   ```

4. Verify the setup with OpenSSH before connecting with Cyberduck. Confirm the prompt with _Touch ID_.
   ```
   ssh -o SecurityKeyProvider=/usr/lib/ssh-keychain.dylib -i ~/.ssh/id_ecdsa_sk_rk user@remotehost
   ```

5. In the [Bookmark](../cyberduck/bookmarks.md) or [Connection](../cyberduck/connection.md) window, in _SSH Private Key_ select `id_ecdsa_sk_rk` in your `~/.ssh` directory. You do **not** need to set a value for _Password_.

6. Connect to the server and confirm the prompt with _Touch ID_ to allow the Secure Enclave to sign the login.

::::
:::::

## Create a Key on a Hardware Token such as YubiKey

:::::{tabs}
::::{group-tab} macOS

1. Insert the security key and create a credential on the token. Touch the token when it blinks.
   ```
   cd ~/.ssh && ssh-keygen -t ed25519-sk -O resident
   ```

   :::{tip}
   Use `-t ecdsa-sk` instead for tokens without support for Ed25519 credentials, such as a _YubiKey_ with a firmware version earlier than 5.2.3. Add `-O verify-required` to require the PIN of the token in addition to touching it. The option `-O resident` stores the credential on the token allowing to write the key files again on another machine with `ssh-keygen -K`.
   :::

   :::{note}
   `ssh-keygen` talks to the token with the USB HID support built into OpenSSH. No middleware library is required to create the key. Pass `-w <library>` only to use a middleware library of your own instead.
   :::

2. Add the public key to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.
   ```
   ssh-copy-id -fi ~/.ssh/id_ed25519_sk.pub user@remotehost
   ```

3. Refer to the middleware library for the token in your OpenSSH configuration file `~/.ssh/config`. The default `/usr/lib/ssh-keychain.dylib` set on macOS serves keys in the Secure Enclave only.
   ```
   Host *
       SecurityKeyProvider /path/to/middleware.so
   ```

   This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck. A value beginning with `$` is read from the environment variable of that name. Alternatively set the [hidden configuration option](hidden_properties.md) `ssh.authentication.securitykey.provider` to the path of the library.

   :::{important}
   The USB HID support built into OpenSSH is not a library and cannot be loaded. Unless the token comes with a middleware library implementing the OpenSSH security key API, leave the security key to an [SSH agent](#let-an-ssh-agent-handle-the-security-key) instead, which works with any token supported by OpenSSH.
   :::

4. In the [Bookmark](../cyberduck/bookmarks.md) or [Connection](../cyberduck/connection.md) window, in _SSH Private Key_ select `id_ed25519_sk` in your `~/.ssh` directory.

5. Connect to the server and touch the security key when it blinks. Enter the PIN of the token when prompted for a key created with `-O verify-required`.

::::
:::::

## Let an SSH Agent handle the Security Key

Instead of talking to the authenticator, Cyberduck and Mountain Duck can leave the security key to an SSH agent. The agent prompts for the touch or the PIN and returns the signature.

:::::{tabs}
::::{group-tab} macOS

1. Add the security key to the SSH agent of OpenSSH. You are asked to confirm with _Touch ID_ or to touch the token.
   ```
   ssh-add ~/.ssh/id_ecdsa_sk_rk
   ```

2. Verify the agent holds the key. The key type is printed as `ECDSA-SK` or `ED25519-SK`.
   ```
   ssh-add -l
   ```

3. Add a new [Bookmark](../cyberduck/bookmarks.md). No _SSH Private Key_ needs to be selected because the key is offered by the agent.

   :::{tip}
   The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when the agent holds many keys. Select the public key `id_ecdsa_sk_rk.pub` for _SSH Private Key_ to only offer the matching identity from the agent.
   :::

::::
:::::

Other SSH agents manage keys of their own instead of a credential on a security key, with the approval prompt of the application taking the place of the touch. Refer to the tutorials for the [1Password SSH Agent](sftp_publickeyauth_1password.md), the [Bitwarden SSH Agent](sftp_publickeyauth_bitwarden.md) and [yubikey-agent](sftp_publickeyauth_yubikey.md) for the setup of the agent socket with `IdentityAgent` in `~/.ssh/config`.

## Troubleshooting

:::{warning}
When the connection fails with the message _No security key provider configured_, no middleware library is set for your platform. A library is configured by default on macOS only. Set `SecurityKeyProvider` in `~/.ssh/config` or add the key to an SSH agent instead. A failure naming the library instead means it could not be loaded, in which case verify the path.
:::

:::{warning}
When the server refuses the key without prompting for a touch, the public key is not accepted. Verify the entry in `authorized_keys` and that the server runs _OpenSSH 8.2_ or later.
:::

## References

- [Cyberduck 9.6.0](https://cyberduck.io/changelog/) or later is required for authentication with a security key without an SSH agent.
- [OpenSSH 8.2 release notes announcing FIDO/U2F support](https://www.openssh.com/txt/release-8.2)
- [PROTOCOL.u2f describing the `sk-*` key types](https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.u2f)
- [Yubico Developers: Securing SSH with FIDO2](https://developers.yubico.com/SSH/Securing_SSH_with_FIDO2.html)
