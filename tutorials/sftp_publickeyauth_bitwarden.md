Configure Public Key Authentication for SFTP using Bitwarden SSH Agent
====

Public-key authentication using Bitwarden SSH Agent allows you to connect to a remote server without a password. Instead, public-key authentication uses two keys:
- Private key managed by Bitwarden
- Public key placed on the server.

1. Ensure you have configured Bitwarden to manage your SSH keys. For more information, refer to [Bitwarden SSH Agent](https://bitwarden.com/help/ssh-agent/#configure-bitwarden-ssh-agent). Open _Bitwarden → Settings…_ and select the checkbox _Enable SSH Agent_.

   :::{image} _images/Bitwarden_SSH_Agent_Settings.png
   :alt: Bitwarden Settings
   :width: 800px
   :::

2. Create a new SSH key in Bitwarden and copy the _Public key_ to the clipboard.

   :::{image} _images/Bitwarden_SSH_Key_Create.png
   :alt: Bitwarden SSH Key
   :width: 800px
   :::

3. Confirm the Bitwarden SSH Agent is running as expected by attempting to list available SSH keys with
   ```
   SSH_AUTH_SOCK=~/.bitwarden-ssh-agent.sock ssh-add -l
   ```

4. Add the public key copied from 1Password to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.

   ```
   pbpaste | ssh user@remotehost 'cat >> .ssh/authorized_keys
   ```

5. Open the OpenSSH configuration file `~/.ssh/config` and add the following configuration specifying to use Bitwarden as the SSH agent:
    ```
   Host *
   IdentitiesOnly yes
   # Bitwarden SSH agent
   IdentityAgent ~/.bitwarden-ssh-agent.sock
   ```
   This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck. If you are running Bitwarden installed from the Mac App Store the socket is located in `~/Library/Containers/com.bitwarden.desktop/Data/.bitwarden-ssh-agent.sock` instead.

6. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_.

   :::{image} _images/Bookmark_Panel.png
   :alt: Bookmark Panel
   :width: 600px
   :::

   :::{tip}
   The server may respond with _[Too many authentication failures](../protocols/sftp/index.md#too-many-authentication-failures)_ when trying to authenticate with all keys stored in 1Password. In the [Bookmark](../cyberduck/bookmarks.md) panel, select the public key corresponding to your SSH private key saved in 1Password for *SSH Private Key*. The public key must be available as a file you can write from the clipboard to a file using:

   ```
   pbpaste > ~/.ssh/test.pub
   ```

   Alternatively, add the public key to the OpenSSH configuration file `~/.ssh/config` with the `IdentityFile` directive

   ```
   # Public Key File used to filter identities from SSH agent
   IdentityFile ~/.ssh/test.pub
   ```

7. Connect to the server and acknowledge the prompt to use the private key stored in Bitwarden.

   :::{image} _images/Bitwarden_Confirm_SSH_Key_Usage.png
   :alt: Bitwarden Confirm Key Usage
   :width: 800px
   :::

## References

* [Bitwarden SSH Agent](https://bitwarden.com/help/ssh-agent/#configure-bitwarden-ssh-agent)