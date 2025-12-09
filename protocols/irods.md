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

To connect to an iRODS server, you must create a [connection profile](index.md#connection-profiles) and store it in the _Profiles_ folder in the [application support folder](../cyberduck/support.md#application-support-folder).

:::{important}
- Cyberduck [9.4.0](https://cyberduck.io/changelog/) or later required
:::

Cyberduck does not provide a preconfigured profile for iRODS. However, a template is provided near the bottom of this page to ease the configuration process. See [Connection Profile Template](#connection-profile-template) for more information.

All configuration properties described on this page are also documented in the [connection profile](index.md#connection-profiles) template.

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

## Connection Profile Template

The following template is provided for quickly creating connection profiles for iRODS.

Copy the template to a new file and save it in the [profiles directory](../cli/index.md#profiles). Make sure the file has a file extension matching `.cyberduckprofile`. Finally, modify the new profile to match the requirements of the iRODS server.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ~ Copyright (c) 2002-2017 iterate GmbH. All rights reserved.
  ~ https://cyberduck.io/
  ~
  ~ This program is free software; you can redistribute it and/or modify
  ~ it under the terms of the GNU General Public License as published by
  ~ the Free Software Foundation; either version 2 of the License, or
  ~ (at your option) any later version.
  ~
  ~ This program is distributed in the hope that it will be useful,
  ~ but WITHOUT ANY WARRANTY; without even the implied warranty of
  ~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  ~ GNU General Public License for more details.
  -->

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>irods</string>
        <key>Vendor</key>
        <string>iRODS Consortium</string>
        <key>Description</key>
        <string>iRODS (Integrated Rule-Oriented Data System)</string>

        <key>Hostname Configurable</key>
        <true/>
        <key>Port Configurable</key>
        <true/>

        <key>Default Port</key>
        <string>1247</string>

        <!-- The zone of the iRODS server to connect to. -->
        <!-- For backward compatibility, a root resource can be specified by appending ":<resource>" to the zone. -->
        <!-- The specified resource is only used when uploading files. -->
        <!-- Prefer setting "Destination Resource" under the "Properties" section. -->
        <key>Region</key>
        <string>tempZone</string>

        <!-- The authentication scheme used to establish a connection to an iRODS server. -->
        <!-- Must be set to "native" or "pam_password". "standard" is an alias for "native". -->
        <key>Authorization</key>
        <string>native</string>

        <key>Properties</key>
        <dict>
            <!-- The root resource to target when uploading files. -->
            <!-- DO NOT define this option unless needed. -->
            <!-- This option supersedes any resource defined by "Region". -->
            <!--
            <key>Destination Resource</key>
            <string>demoResc</string>
            -->

            <!-- Controls whether deletion of an object permanently removes or moves it into the trash collection. -->
            <key>Delete Objects Permanently</key>
            <string>no</string>

            <!-- The size (in bytes) of a file that must be exceeded before using parallel transfer. -->
            <!-- The value must satisfy the range [1, 2^31-1]. -->
            <key>Parallel Transfer Threshold</key>
            <string>33554432</string>

            <!-- The number of iRODS connections used for parallel transfer of a single file. -->
            <!-- Each transfer will use the specified number of iRODS connections. -->
            <!-- The value must satisfy the range [2, 10]. -->
            <key>Parallel Transfer Connections</key>
            <string>3</string>

            <!-- The buffer size (in bytes) used for parallel transfer of a single file. -->
            <!-- Applies to uploads and downloads. -->
            <!-- The value must satisfy the range [1, 128MB]. -->
            <key>Parallel Transfer Buffer Size</key>
            <string>4194304</string>

            <!-- Secure Communication Options -->

            <!-- Must be set to "CS_NEG_REQUIRE", "CS_NEG_DONT_CARE", or "CS_NEG_REFUSE". -->
            <!-- - CS_NEG_REQUIRE:   Demand TLS be used. -->
            <!-- - CS_NEG_DONT_CARE: Let the server decide if TLS should be used. -->
            <!-- - CS_NEG_REFUSE:    Do not use TLS. -->
            <key>Client Server Negotiation</key>
            <string>CS_NEG_REFUSE</string>

            <!-- Options which are only used when TLS is active. -->

            <key>Encryption Algorithm</key>
            <string>AES-256-CBC</string>
            <key>Encryption Key Size</key>
            <string>32</string>
            <key>Encryption Salt Size</key>
            <string>8</string>
            <key>Encryption Hash Rounds</key>
            <string>16</string>
        </dict>
    </dict>
</plist>
```

## References

- [irods.org](https://irods.org/)
- [docs.irods.org](https://docs.irods.org/)
- [Downloading and Uploading Data](https://cyverse.atlassian.net/wiki/spaces/DS/pages/241869862/Downloading+and+Uploading+Data)
- [Using Cyberduck for Uploading and Downloading to the Data Store](https://cyverse.atlassian.net/wiki/spaces/DS/pages/241869843/Using+Cyberduck+for+Uploading+and+Downloading+to+the+Data+Store)
- [iRODS Error Codes](https://github.com/irods/irods/blob/main/lib/core/include/irods/rodsErrorTable.h)
