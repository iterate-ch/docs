Configure Public Key Authentication for SFTP using 1Password SSH Agent
====

> Public-key authentication using _1Password_ SSH Agent allows you to connect to a remote server without a password. Instead of passwords, you use a pair of keys (private and public) for authentication. The private key is kept secret, while the public key is shared with the server.

:::::{tabs}
::::{group-tab} macOS
1. Ensure you have configured _1Password_ to manage your SSH keys. For more information, refer to [1Password SSH Agent](https://developer.1password.com/docs/ssh/agent). Enable the _1Password SSH Agent_ in _1Password → Settings… → Developer_

   :::{image} _images/1Password_SSH_Agent_Settings.png
   :alt: 1Password SSH Agent Settings
   :width: 600px
   :::

2. Verify the _1Password SSH Agent_ is running as expected by attempting to list available SSH keys with
   ```
   SSH_AUTH_SOCK=~/Library/Group\ Containers/2BUA8C4S2C.com.1password/t/agent.sock ssh-add -l
   ```
3. Open the OpenSSH configuration file `~/.ssh/config` and add the following configuration specifying to use _1Password_ as the SSH agent:
    ```
    Host *
        IdentitiesOnly yes
        # 1Password SSH agent
        IdentityAgent "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"
    ```
   Alternatively allow 1Password to add the setting automatically:

   :::{image} _images/1Password_SSH_Agent_Edit_Automatically.png
   :alt: 1Password SSH Agent Edit Configuration
   :width: 600px
   :::

   This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck. You can restrict the settings to a single alias in the configuration file instead of matching it for all connections with `*`. 
 
4. Create a new SSH key in 1Password and copy the _Public key_ to the clipboard.

   :::{image} _images/1Password_SSH_Key_Create.png
   :alt: 1Password SSH Key
   :width: 600px
   :::

5. Add the public key copied from _1Password_ to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.

   ```
   pbpaste | ssh user@remotehost 'cat >> .ssh/authorized_keys
   ```

6. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_.

   :::{image} _images/Bookmark_Panel.png
   :alt: Bookmark Panel
   :width: 600px
   :::

   :::{tip}
   The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when trying to authenticate with all keys stored in _1Password_. In the [Bookmark](../cyberduck/bookmarks.md) panel, select the public key corresponding to your SSH private key saved in _1Password_ for *SSH Private Key*. The public key must be available as a file you can write from the clipboard to a file using:

   ```
   pbpaste > ~/.ssh/test.pub
   ```

   Alternatively, add the public key to the OpenSSH configuration file `~/.ssh/config` with the `IdentityFile` directive

   ```
   # Public Key File used to filter identities from SSH agent
   IdentityFile ~/.ssh/test.pub
   ```

7. Connect to the server and acknowledge the prompt to use the private key stored in _1Password_.

   :::{image} _images/1Password_Authorize_SSH_Key_Usage.png
   :alt: 1Password Confirm Key Usage
   :width: 600px
   :::

::::
:::::

## References

* [1Password SSH Agent](https://developer.1password.com/docs/ssh/agent)