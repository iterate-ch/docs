Configure Public Key Authentication for SFTP using OpenSSH
====

Public-key authentication allows you to connect to a remote server without a password. Instead, public-key authentication uses two keys:
- Private key kept in a file and protected with a password.
- Public key placed on the server.

1. Run the command `ssh-keygen` from the _Terminal.app_ (macOS) or _Console_ (Windows) to generate a public/private pair
   of keys. They will be put in your directory `~/.ssh`, though you will probably be asked to approve or change this
   location. When you generate the keys you will be asked for a passphrase. If you use a *passphrase*, then you will
   have to enter it when connecting. Use the key format (`-m PEM`) to create the keys in OpenSSL `PEM` format. Specify the type of key with the parameter `-t` as either `ecdsa`, `ed25519` or `rsa`.

   ```
   ssh-keygen -m PEM -t rsa
   ```

2. Copy the public key to the server you wish to access and add it to the file `authorized_keys` in your `~/.ssh`
   directory. This will cause the server to allow authenticating with your corresponding private key.
   ```
   ssh user@remotehost < ~/.ssh/id_rsa.pub 'cat >> .ssh/authorized_keys'
   ```
3. In the [Bookmark](../cyberduck/bookmarks.md) or [Connection](../cyberduck/connection.md) window, in *SSH Private Key* select the private key in your `~/.ssh` directory. When connecting, you will be prompted to enter the password for the private key. Choose *Save Password* to [save the password](../cyberduck/connection.md#passwords).
