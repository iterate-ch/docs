Configure Public Key Authentication for SFTP using _yubikey-agent_
====

> Public-key authentication using _[yubikey-agent](https://github.com/FiloSottile/yubikey-agent)_ SSH Agent allows you to connect to a remote server without a password. Instead of passwords, you use a pair of keys (private and public) for authentication. The private key is kept secret, while the public key is shared with the server.

Authenticate SSH connections with the SSH private key stored on a _YubiKey_. Setup _yubikey-agent_, a seamless ssh-agent for _YubiKey_.

:::::{tabs}
::::{group-tab} macOS

1. Install `yubikey-agent` using [Homebrew](https://brew.sh) on macOS.
   ```
   brew install yubikey-agent
   ```

2. Launch _YubiKey_ Agent
    ```
    brew services start yubikey-agent
    ```
3. Run setup to create a new SSH key on the _YubiKey_
   ```
   🔐 The PIN is up to 8 numbers, letters, or symbols. Not just numbers!
   ❌ The key will be lost if the PIN and PUK are locked after 3 incorrect tries.
   
   Choose a new PIN/PUK:
   Repeat PIN/PUK:
   
   🧪 Reticulating splines...
   
   ✅ Done! This YubiKey is secured and ready to go.
   🤏 When the YubiKey blinks, touch it to authorize the login.
   
   🔑 Here's your new shiny SSH public key:
   ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEX52rEAXMPs7m75uvckZwhV6k+pUFRADkSaGhhALt484hBAP8C1XOHISJzAF46oWgVopDXP/4BD58UwkeMDSJc=
   
   Next steps: ensure yubikey-agent is running via launchd/systemd/...,
   set the SSH_AUTH_SOCK environment variable, and test with "ssh-add -L"
   
   💭 Remember: everything breaks, have a backup plan for when this YubiKey does.
   ```                    

4. Specify the socket the _YubiKey_ SSH Agent is listening in your OpenSSH configuration file `~/.ssh/config`.
   ```
   Host *
       IdentitiesOnly yes
       IdentityAgent /opt/homebrew/var/run/yubikey-agent.sock
   ```

5. Copy the SSH public from the output and save it to a file:
   ```
   echo "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEX52rEAXMPs7m75uvckZwhV6k+pUFRADkSaGhhALt484hBAP8C1XOHISJzAF46oWgVopDXP/4BD58UwkeMDSJc=" > ~/.ssh/yubikey.pub
   ```

6. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the alias from your OpenSSH configuration or the hostname in _Server_. You do **not** need to set a value for _Password_.

   :::{image} _images/Bookmark_Panel.png
   :alt: Bookmark Panel
   :width: 600px
   :::

   :::{tip}
   The public key selected allows to identify the corresponding private key retrieved from the SSH agent avoiding _Too many authentication failures_.
   :::

7. Add the public key to the `authorized_keys` in your `~/.ssh` directory on the server running OpenSSH.
   ```
   ssh-copy-id -fi ~/.ssh/yubikey.pub user@remotehost   
   ```

8. Verify the agent is running and can access keys on your _YubiKey_
   ```
   SSH_AUTH_SOCK="/opt/homebrew/var/run/yubikey-agent.sock" ssh-add -l
   256 SHA256:etGxFZK2D+AFJITkoaAm5BoxHqQlZfIWkhnSMMjGZ2I YubiKey #15203057 PIV Slot 9a (ECDSA)
   ```

9. Connect to the server and enter the PIN for the _YubiKey_ to unlock the private key:

   :::{image} _images/YubiKey_Agent_PIN_Prompt.png
   :alt: YubiKey Agent PIN Prompt
   :width: 600px
   :::

   :::{important}
   Touch the _YubiKey_ when it blinks to verify human interaction and allow to proceed the connection.
   :::

   :::{warning}
   If you receive a prompt to login using a password with the message _Unknown key format for file yubikey.pub. Please contact your web hosting service provider for assistance_, there was a failure accessing the private key. Ensure the SSH agent is running.
   :::

::::
:::::

## References

- [Yubico](https://www.yubico.com/)
- [Guide to using YubiKey for GnuPG and SSH](https://github.com/drduh/YubiKey-Guide)
- [Seamless ssh-agent for YubiKey](https://github.com/FiloSottile/yubikey-agent)