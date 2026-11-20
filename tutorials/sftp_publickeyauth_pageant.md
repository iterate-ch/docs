Configure Public Key Authentication for SFTP using Pageant
====

> Public-key authentication using _Pageant_ SSH Agent allows you to connect to a remote server without a password. Instead of passwords, you use a pair of keys (private and public) for authentication. The private key is kept secret, while the public key is shared with the server.

:::{important}
* Cyberduck [9.6](https://cyberduck.io/changelog/) or later required
* PuTTY/Pageant [0.77](https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html) or later required

The previous built-in Pageant integration has been removed in Cyberduck 9.6. Refer to [#18479](https://github.com/iterate-ch/cyberduck/issues/18479).
:::

Refer to [How To Use Pageant to Streamline SSH Key Authentication with PuTTY](https://www.digitalocean.com/community/tutorials/how-to-use-pageant-to-streamline-ssh-key-authentication-with-putty) for general usage of Pageant. Pageant supports writing the `IdentityAgent`-option into an OpenSSH configuration file on startup.

1. Install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), which includes _Pageant_ and _PuTTYgen_.

2. Start Pageant with the `--openssh-config` option, e.g. in the shortcut used to launch Pageant at login. Private key files to load can be appended to the command line.

   ```
   pageant.exe --openssh-config %USERPROFILE%\.ssh\pageant.conf
   ```

3. Add an `Include` directive at the top of `%USERPROFILE%\.ssh\config` before any `Host` entry to apply it to all hosts.

   ```
   Include ~/.ssh/pageant.conf
   ```

4. Open your private key in _PuTTYgen_ and copy the public key shown in _Public key for pasting into OpenSSH authorized_keys file_. Add it to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.

5. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_.

   :::{tip}
   The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when trying to authenticate with all keys loaded in _Pageant_. In the [Bookmark](../cyberduck/bookmarks.md) panel, select the public key corresponding to your private key loaded in _Pageant_ for *SSH Private Key*. The public key must be available as a file, e.g. saved from _PuTTYgen_ to `%USERPROFILE%\.ssh\mykey.pub`.

   Alternatively, add the public key to the OpenSSH configuration file `~/.ssh/config` with the `IdentityFile` directive

   ```
   # Public Key File used to filter identities from SSH agent
   IdentityFile ~/.ssh/mykey.pub
   ```
   :::

6. Connect to the server. The private key loaded in _Pageant_ is used to authenticate.

## References

* [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [How To Use Pageant to Streamline SSH Key Authentication with PuTTY](https://www.digitalocean.com/community/tutorials/how-to-use-pageant-to-streamline-ssh-key-authentication-with-putty)
