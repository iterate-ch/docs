Configure Public Key Authentication for SFTP using Bitwarden SSH Agent
====

Public-key authentication using Bitwarden SSH Agent allows you to connect to a remote server without a password. Instead, public-key authentication uses two keys:
- Private key managed by Bitwarden
- Public key placed on the server usually by the system administrator

1. Ensure you have configured Bitwarden to manage your SSH keys. For more information, refer to [Bitwarden SSH Agent](https://bitwarden.com/help/ssh-agent/#configure-bitwarden-ssh-agent).
2. Open the OpenSSH configuration file `~/.ssh/config` and add the following configuration specifying to use 1Password as the SSH agent:
    ```
    Host *
       IdentitiesOnly yes
       # Bitwarden SSH agent
       IdentityAgent ~/.1password/agent.sock
    ```
   This [configuration](https://docs.cyberduck.io/protocols/sftp/#openssh-configuration-interoperability) directive is supported by Cyberduck and Mountain Duck.
3. In the [Bookmark](../../cyberduck/bookmarks.md) or [Connection](../../cyberduck/connection.md) panel, select *Use Public Key Authentication*
4. Select the public key corresponding to your SSH private key saved in Bitwarden. Typically, it is located in the `~/.ssh` directory.

## References

* [Bitwarden SSH Agent](https://bitwarden.com/help/ssh-agent/#configure-bitwarden-ssh-agent)