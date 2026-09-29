Configure Kerberos Authentication for SFTP
====

> Authentication with _Kerberos_ allows you to connect to a remote server without a password using the ticket you already obtained when logging in to your organization's realm with `kinit` or with your account on the Mac. The ticket is presented to the server using the SSH authentication method `gssapi-with-mic`, the equivalent of `ssh -o GSSAPIAuthentication=yes`.

:::{important}
* Cyberduck [9.6.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [6.0.0](https://mountainduck.io/changelog/) or later required
:::

Authentication with Kerberos is attempted after public key authentication and before prompting for a password when no password is saved for the bookmark. Without a valid ticket the method is skipped and the login continues with the next authentication method offered by the server.

## Requirements

- The server running OpenSSH is configured with `GSSAPIAuthentication yes` in `sshd_config` and has a keytab with the service principal `host/server.example.com@EXAMPLE.COM` for its fully qualified hostname. Refer to your administrator.
- Your principal such as `user@EXAMPLE.COM` is allowed to log in to the account on the server. By default the principal `user@EXAMPLE.COM` maps to the account `user`. Additional principals are listed in `~/.k5login` of the account on the server.
- The Kerberos configuration with the default realm and the Key Distribution Center (KDC) of your organization is found in `/etc/krb5.conf` or can be looked up in DNS.

## Setup

:::::{tabs}
::::{group-tab} macOS

1. Obtain a ticket for your principal. Enter the password of your Kerberos account when prompted.
   ```
   kinit user@EXAMPLE.COM
   ```

   :::{tip}
   Tickets obtained with _Ticket Viewer.app_ in `/System/Library/CoreServices/Applications` or when logging in to a Mac bound to a directory service with Kerberos are used as well.
   :::

2. Verify a ticket for the realm is listed and has not expired.
   ```
   klist
   ```

3. Verify the setup with OpenSSH before connecting with Cyberduck. Use the fully qualified hostname of the server.
   ```
   ssh -o GSSAPIAuthentication=yes -o PreferredAuthentications=gssapi-with-mic user@server.example.com
   ```

   A service ticket for `host/server.example.com@EXAMPLE.COM` is now listed with `klist`.

4. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck. Enter the fully qualified hostname `server.example.com` in _Server_ and your account in _Username_. You do **not** need to set a value for _Password_ or select a _SSH Private Key_.

   :::{warning}
   The hostname must match the service principal in the keytab of the server. Connecting using an IP address or a short hostname may fail when it cannot be resolved to the fully qualified name.
   :::

5. Connect to the server. No prompt is displayed when the ticket is accepted.

::::
:::::

## Kerberos Configuration

The Kerberos configuration is read from `/etc/krb5.conf` or on macOS from `~/Library/Preferences/edu.mit.Kerberos` and `/Library/Preferences/edu.mit.Kerberos` first when found. A minimal configuration for the realm `EXAMPLE.COM` looks like
```
[libdefaults]
    default_realm = EXAMPLE.COM

[realms]
    EXAMPLE.COM = {
        kdc = kdc.example.com
    }

[domain_realm]
    .example.com = EXAMPLE.COM
```

Omit the `[realms]` section and add `dns_lookup_kdc = true` to `[libdefaults]` to look up the KDC from `_kerberos._tcp` and `_kerberos._udp` DNS SRV records of the realm instead.

The following [hidden configuration options](hidden_properties.md) apply to all connections.

| Option                                  | Description                                                                                                                                                                           |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java.security.krb5.conf`               | Path to a Kerberos configuration file to use instead of the default location such as `/etc/krb5.conf`.                                                                                |
| `java.security.krb5.realm`              | Default realm such as `EXAMPLE.COM` overriding the configuration file. Must be set together with `java.security.krb5.kdc`.                                                            |
| `java.security.krb5.kdc`                | Hostname of the KDC for the default realm overriding the configuration file. Must be set together with `java.security.krb5.realm`. Separate multiple KDCs with `:`.                  |
| `ssh.authentication.gssapi.ticketcache` | Path to a credentials cache file to read the ticket from instead of the default cache. Obtain a ticket written to the file with `kinit -c /path/to/file user@EXAMPLE.COM`.            |

Example to set the realm and KDC for Cyberduck on macOS.
```
defaults write ch.sudo.cyberduck java.security.krb5.realm EXAMPLE.COM
defaults write ch.sudo.cyberduck java.security.krb5.kdc kdc.example.com
```

:::{note}
A KDC set with `java.security.krb5.kdc` is always contacted on the default port `88`. Use a configuration file with `kdc = kdc.example.com:port` for a KDC listening on a different port.
:::

## Require Public Key and Kerberos Authentication

Servers can require authentication with both a private key and a Kerberos ticket with `AuthenticationMethods publickey,gssapi-with-mic` in `sshd_config`. Select the private key in _SSH Private Key_ of the bookmark. After the key has been accepted, login completes with the Kerberos ticket.

## Troubleshooting

:::{warning}
When you are prompted for a password instead, no ticket was found or the server did not accept it. Verify with `klist` that the ticket for the realm has not expired and obtain a new ticket with `kinit` otherwise. Verify the login with `ssh -v -o GSSAPIAuthentication=yes user@server.example.com` which prints the reason why the method failed.
:::

:::{warning}
The message _Server not found in Kerberos database_ printed by `ssh -v` indicates no service principal matches the hostname used to connect. Connect using the fully qualified hostname matching the keytab of the server.
:::

:::{warning}
Authentication fails when the clock of your computer differs by more than five minutes from the KDC or the server. Enable _Set time and date automatically_ in _System Settings → General → Date & Time_.
:::

:::{note}
The `GSSAPIAuthentication` directive in `~/.ssh/config` is not required. The authentication method is always attempted when offered by the server. Limit the methods tried with [`PreferredAuthentications`](../protocols/sftp/index.md#configuration-file) instead.
:::

## References

- [`GSSAPIAuthentication` in ssh_config](https://man.openbsd.org/ssh_config#GSSAPIAuthentication)
- [`GSSAPIAuthentication` in sshd_config](https://man.openbsd.org/sshd_config#GSSAPIAuthentication)
- [RFC 4462: GSS-API Authentication and Key Exchange for SSH](https://www.rfc-editor.org/rfc/rfc4462)
- [MIT Kerberos: krb5.conf](https://web.mit.edu/kerberos/krb5-latest/doc/admin/conf_files/krb5_conf.html)
- [Java Kerberos Requirements](https://docs.oracle.com/en/java/javase/21/security/kerberos-requirements1.html) for the lookup of the configuration file and the system properties `java.security.krb5.realm` and `java.security.krb5.kdc`.
