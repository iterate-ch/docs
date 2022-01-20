Connection Profiles
====

[Connection profiles](../cyberduck/connection.md#connection-profiles) (`.cyberduckprofile`) are documents describing connection settings for a hosting provider.

- [Third-Party S3 providers](s3/index.md#third-party-providers)
- [OpenStack Providers](openstack/index.md#third-party-providers)

## Installation
Connection profiles can be activated by either installing the file by double clicking a `.cyberduckprofile` file to open and register or enabling in _Preferences → Profiles_.

### Technical File Format Specification

```{note}
Connection profile files ([XML Property List Format](http://en.wikipedia.org/wiki/Property_list)) can be created for customers to make it easier to connect with a double-click on that file without entering the connection details manually. [Contact us](mailto:support@cyberduck.io) if you are a service provider and need assistance in setting this up.
```

The following properties can be defined in a connection profile:

- `Protocol` *(Required)*
- `Vendor` (Hosting Provider) *(Required)*
```{important}
The value of `Vendor` must be unique among all installed connection profiles.
```
- `Description` *(Required)*
- `Default Nickname`
- `Default Hostname`
- `Default Port`
- `Default Path`
- `Username Placeholder`
- `Password Placeholder`
- `Disk` Base64 encoded disk TIFF image icon. Multi Page TIFF with formats `64x64` (72dpi) and `128x128` (144dpi) pixels. Use the {download}`disk template file<https://svn.cyberduck.ch/trunk/profiles/assets/Template.psd>` to create a provider profile image.
- `Icon` Base64 encoded disk TIFF image icon to be used in protocol dropdown menu instead of `Disk` icon
- `Context` Login context path (currently used for Swift profiles)
- `Username Configurable` Boolean if username is configurable.
- `Password Configurable` Boolean if password is configurable.
- `Hostname Configurable` Boolean if hostname is configurable.
- `Port Configurable` Boolean if port number is configurable.
- `Anonymous Configurable` Boolean if anonymous access is configurable.
- `Path Configurable` Boolean if default path is configurable.
- `Certificate Configurable` Boolean if client certificate is configurable.
- `Region` Region name to limit listing containers of a specific region only for [OpenStack Swift](openstack/index.md) and [S3](s3/index.md) profiles. For S3, this value is used for AWS4 signatures when no location can be deferred from the URI for third-party S3 providers.
- `Regions` List of regions supported by the provider. This will populate options in the *Regions* dropdown when creating a new [top level folder](s3/index.md#creating-a-bucket) for [S3](s3/index.md) and [OpenStack Swift](openstack/swiftstack.md) connections.
- `OAuth Client ID` For protocols using OAuth 2.0 you can override the registered application client ID with the provider.
- `OAuth Client Secret` For protocols using OAuth 2.0 you can override the registered application client secret with the provider.
- `Authorization` Set to `AWS2` to default to AWS2 signature authentication for S3. Default is `AWS4HMACSHA256`.
- `Properties` List of custom protocol-specific properties. You can set [hidden configuration options](../cyberduck/preferences.md#hidden-configuration-options) for a specific connection profile. Example usages can be found in:
  * [FTP (Compatibility Mode).cyberduckprofile](https://github.com/iterate-ch/cyberduck/blob/master/profiles/FTP%20(Compatibility%20Mode).cyberduckprofile)
  * [FTP-SSL (Compatibility Mode).cyberduckprofile](https://github.com/iterate-ch/cyberduck/blob/master/profiles/FTP-SSL%20(Compatibility%20Mode).cyberduckprofile)
  * [S3 (Deprecated path style requests).cyberduckprofile](https://github.com/iterate-ch/cyberduck/blob/master/profiles/S3%20(Deprecated%20path%20style%20requests).cyberduckprofile)

#### Example

```{note}
{download}`Disk template file (Adobe Photoshop)<https://svn.cyberduck.ch/trunk/profiles/assets/Template.psd>`
```

```{code-block}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>swift</string>
        <key>Vendor</key>
        <string>hp</string>
        <key>Description</key>
        <string>HP Cloud Object Storage</string>
        <key>Default Hostname</key>
        <string>region-a.geo-1.identity.hpcloudsvc.com</string>
        <key>Default Port</key>
        <string>35357</string>
        <key>Schemes</key>
        <array>
                <string>hp</string>
                <string>https</string>
        </array>
        <key>Hostname Configurable</key>
        <false/>
        <key>Port Configurable</key>
        <false/>
        <key>Context</key>
        <string>/v2.0/tokens</string>
        <key>Username Placeholder</key>
        <string>Tenant ID:Access Key</string>
        <key>Password Placeholder</key>
        <string>Secret Key</string>
        <key>Properties</key>
        <array>
            <string>key=value</string>
        </array>
        <key>Disk</key>
        <string>
            TU0AKgAFiw6AACBQOCQWDQeEQmFQuGQ2HQ+IRGJROKRWLReMRmNRuOR2PR+QSGRSOSSWTSeU
            SmVSuWS2XS+YTGZTOaTWbTecTmdTueT2fT+gUGhUOiUWjUekUmlUumU2nU+oVGpVOqVWrVes
            VmtVuuV2vV+wWGxWOyWWzWe0Wm1Wu2W23W+4XG5XO6XW7Xe8Xm9Xu+X2/X/AYHBYPCYXDYfE
            YnFYvGY3HY/IZHJZPKZXLZfMZnNZvOZ3PZ/QaHRaPSaXTafUanVavWa3Xa/YbHZbPabXbbfc
            bndbveb3fb/gcHhcPicXjcfkcnlcvmc3nc/odHpdPqdXrdfsdntdvud3vd/weHxePyeXzef0
            en1ev2e33e/4fH5fP6fX7ff8fn9fv+f3/P/AEAwFAcCQLA0DwRBMFQXBkGwdB8IQjCUJwpCs
            LQvDEMw1DcOQ7D0PxBEMRRHEkSxNE8URTFUVxZFsXRfGEYxlGcaRrG0bxxHMdR3Hkex9H8gS
            DIUhyJIsjSPHAAyUAMkSbJ0nyhKMpSmkh/ysf8qSzLUtotJcmS5MEwzFMcyTLMMryxM01TXE
            cvIZNyNzhNk5zpOs7TvPDfzQjk9onPs80BQL0TkgtCIJQlDIHRKDApRoXgPSAIA4DgNh8glJ
            g2H6EUaCwXAQBADghKyBSUiVRgBUqs1PVKGSvVFWJ3NNUVNNNYM1VcvrLWVcoHXCDV8AFgIJ
            V0loLYSWTTLEsWLYda15XtFJlY7BWmn1dp1YFqrTa6O20g9vI1YlbKpcFdWdB9uLxcqYXWol
            …
            /aMAAAPcAADAbA==
        </string>
        <key>Regions</key>
        <array>
            <string>custom</string>
            <string>custom2</string>
        </array>
    </dict>
</plist>
```

## Disk icon template

- {download}`Adobe Photoshop disk template file<https://svn.cyberduck.ch/trunk/profiles/assets/Template.psd>`