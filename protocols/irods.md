iRODS (Integrated Rule-Oriented Data System)
====

> The Integrated Rule-Oriented Data System (iRODS) is an open-source, policy-based data management software used by research, commercial, and governmental organizations worldwide.

:::{admonition} iRODS
:class: tip

- Enables data discovery using a metadata catalog that describes every file, every directory, and every storage resource in the data grid.
- Automates data workflows, with a rule engine that permits any action to be initiated by any trigger on any server or client in the grid.
- Enables secure collaboration, so users only need to log in to their home grid to access data hosted on a remote grid.
- Implements data virtualization, allowing access to distributed storage assets under a unified namespace, and freeing organizations from getting locked into single-vendor storage solutions.
:::

:::{important}
Requires iRODS 4.3.2 or newer.
:::

## Connecting

Download the corresponding *Connection Profile* for preconfigured settings and double-click on it to install it. Choose the profile from the list of protocols when editing a [bookmark](../cyberduck/bookmarks.md) or use the `<vendor>:/` scheme when using the [CLI](../cli/index).

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

### Provider

A general purpose iRODS connection profile is available {download}`here<https://profiles.cyberduck.io/iRODS.cyberduckprofile>`.

All configuration properties described on this page are also documented in the connection profile.

### Authentication

#### Authentication with the Native scheme

To authenticate, set the **Authorization** value to `native` or `standard` in the [connection profile](index.md#connection-profiles). Defaults to `native`.

```
    <key>Authorization</key>
    <string>native</string>
```

`standard` is an alias for `native`. It is provided for backward compatibility.

#### Authentication with the PAM scheme

:::{note}
PAM requires a secure connection to the server. See [Secure Communication](#secure-communication) to learn more.
:::

To authenticate with PAM, set the **Authorization** value to `pam_password` or `pam` in the [connection profile](index.md#connection-profiles).

```
    <key>Authorization</key>
    <string>pam_password</string>
```

`pam` is an alias for `pam_password`. It is provided for backward compatibility.

#### Configuring the iRODS Zone

The zone of the target server must be specified before connecting to it. To do that, set the **Region** value in the [connection profile](index.md#connection-profiles).

```
    <key>Region</key>
    <string>zone_name</string>
```

### Secure Communication

To require secure communication, you must first set the **Client Server Negotiation** value to `CS_NEG_REQUIRE` in the [connection profile](index.md#connection-profiles).

```
    <key>Properties</key>
    <dict>
        <key>Client Server Negotiation</key>
        <string>CS_NEG_REQUIRE</string>
    </dict>
```

Set the value to `CS_NEG_DONT_CARE` to let the server decide whether to use secure communication. Set it to `CS_NEG_REFUSE` to require an insecure channel. If the client and server cannot agree on how to proceed, the connection will fail and result in an error.

Next, configure the encryption values to match those of the server. Consult the administrator of the iRODS zone to obtain the correct values.

```
    <key>Properties</key>
    <dict>
        <key>Encryption Algorithm</key>
        <string>AES-256-CBC</string>
        
        <key>Encryption Key Size</key>
        <string>32</string>
        
        <key>Encryption Salt Size</key>
        <string>8</string>
        
        <key>Encryption Hash Rounds</key>
        <string>16</string>
    </dict>
```

#### Storage Resource

To upload files to a specific resource, set the **Destination Resource** value in the [connection profile](index.md#connection-profiles). The specified resource must be the root of a resource hierarchy. This property supersedes any resource defined by the **Region** property.

```
    <key>Properties</key>
    <dict>
        <key>Destination Resource</key>
        <string>resource_name</string>
    </dict>
```

For backward compatibility, it can also be set by appending the name of the resource to the **Region**'s value. This method may be removed in the future.

```
    <key>Region</key>
    <string>zone_name:resource_name</string>
```

## Transfers

### Parallel Transfer

Large file uploads will use parallel transfer when the requirements are satisfied. By default, a file must be larger than 32MB in order to trigger parallel transfer.

The default values for parallel transfer are shown below. Descriptions of each property follow.

```
    <key>Properties</key>
    <dict>
        <key>Parallel Transfer Threshold</key>
        <string>33554432</string>

        <key>Parallel Transfer Connections</key>
        <string>3</string>

        <key>Parallel Transfer Buffer Size</key>
        <string>4194304</string>
    </dict>
```

**Parallel Transfer Threshold** is the size (in bytes) of a file to upload that must be exceeded before parallel transfer is used. The value must satisfy the range [1, 2<sup>31</sup>-1].

**Parallel Transfer Connections** is the number of connections used to upload a single file when parallel transfer is used. The value must satisfy the range [2, 10].

**Parallel Transfer Buffer Size** is the size (in bytes) of each buffer used to transfer bytes to the server. This property applies to uploads and downloads. The value must satisfy the range [1, 128MB].

### Trash Policy

To delete data objects and collections permanently, set the **Delete Objects Permanently** value to `yes` in the [connection profile](index.md#connection-profiles). Defaults to `no`.

```
    <key>Properties</key>
    <dict>
        <key>Delete Objects Permanently</key>
        <string>yes</string>
    </dict>
```

## References

- [irods.org](https://irods.org/)
- [docs.irods.org](https://docs.irods.org/)
- [Downloading and Uploading Data](https://cyverse.atlassian.net/wiki/spaces/DS/pages/241869862/Downloading+and+Uploading+Data)
- [Using Cyberduck for Uploading and Downloading to the Data Store](https://cyverse.atlassian.net/wiki/spaces/DS/pages/241869843/Using+Cyberduck+for+Uploading+and+Downloading+to+the+Data+Store)
- [iRODS Error Codes](https://github.com/irods/irods/blob/main/lib/core/include/irods/rodsErrorTable.h)
