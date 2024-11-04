Configure Public Key Authentication for SFTP using OpenSSH
====

Public-key authentication allows you to connect to a remote server without a password. Instead, public-key authentication uses two keys:
- Private key that only you have kept in a secure place and protected with a password.
- Public key placed on the server usually by the system administrator.

1. Run the command `ssh-keygen` from the _Terminal.app_ (macOS) or _Console_ (Windows) to generate a public/private pair
   of keys. They will be put in your directory `~/.ssh`, though you will probably be asked to approve or change this
   location. When you generate the keys you will be asked for a passphrase. If you use a *passphrase*, then you will
   have to enter it when connecting. Use the key format (`-m PEM`) to create the keys in OpenSSL `PEM` format. Specify the type of key with the parameter `-t` as either `ecdsa`, `ed25519` or `rsa`.

   ```
   ssh-keygen -m PEM -t rsa
   ```

2. Copy the public key to the server you wish to access and add it to the file `authorized_keys` in your `~/.ssh`
   directory.
   :::{tip}
   You may need to create the file if it does not exist.
   :::

   This will cause the server to allow authenticating with your corresponding private key.
   ```
   ssh hostname < ~/.ssh/id_rsa.pub 'cat >> .ssh/authorized_keys'
   ```
3. In the [Bookmark](../../cyberduck/bookmarks.md) or [Connection](../../cyberduck/connection.md) panel, select *Use Public Key Authentication* and select the private key in your `~/.ssh` directory.