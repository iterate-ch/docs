Connection Profiles
====

:::{toctree}
:hidden:
:titlesonly:
google_client_id
aws_oidc
:::

:::{contents} Content
:depth: 2
:local:
:::

[Connection profiles](../../cyberduck/connection.md#connection-profiles) (`.cyberduckprofile`) are documents describing connection settings for a hosting provider.

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

- [Third-Party S3 providers](../s3/providers.md)
- [OpenStack Providers](../openstack/index.md#third-party-providers)

## Installation

Connection profiles can be activated by either installing the file by double-clicking a `.cyberduckprofile` file to open and register or enabling in _Preferences → Profiles_.

## Contributing Connection Profiles

:::{admonition} Info
:class: tip

To contribute new connection profiles, open a pull request in the [`iterate-ch/profiles` repository](https://github.com/iterate-ch/profiles). Once the pull request is approved the profile will be available through the _Preferences → Profiles_ tab in [Mountain Duck](../../mountainduck/preferences.md#profiles) and Cyberduck.
:::

### Technical File Format Specification

:::{note}
Connection profile files ([XML Property List Format](http://en.wikipedia.org/wiki/Property_list)) can be created for customers to make it easier to connect with a double-click on that file without entering the connection details manually. [Contact us](mailto:support@cyberduck.io) if you are a service provider and need assistance in setting this up.
:::

The following properties can be defined in a connection profile:

- `Protocol` *(Required)*
- `Vendor` (Hosting Provider) *(Required)*
:::{important}
The value of `Vendor` must be unique among all installed connection profiles.
:::
- `Description` *(Required)*
- `Default Nickname` Prefilled bookmark name.
- `Default Hostname` Prefilled server name.
- `Hostname Configurable` Boolean if hostname is configurable.
- `Hostname Placeholder` Suggestion for server name.
- `Default Port` Prefilled port number.
- `Port Configurable` Boolean if port number is configurable.
- `Default Path`
- `Schemes` Additional array of schemes this profile can be referenced with in [Cyberduck CLI](../../cli/index.md)
  :::{note}
  All additional schemes are registered as a scheme handler when opening [Mountain Duck](../../mountainduck/index.md). This allows to reference files and folders in a web application using a custom scheme like `customscheme:/(/<hostname>)/path` to open in Windows Explorer or Finder.
  :::
- `Username Configurable` Boolean if username is configurable.
- `Username Placeholder` Suggestion for username in login credentials. Used for input field label when editing bookmark.
- `Password Placeholder` Suggestion for password in login credentials. Used for input field label when editing bookmark.
- `Password Configurable` Boolean if password is configurable.
- `Disk` Base64 encoded disk TIFF image icon. Multi Page TIFF with formats `64x64` (72dpi) and `128x128` (144dpi) pixels.

  :::{tip} 
  Use the {download}`disk template file<https://github.com/iterate-ch/profiles/blob/master/assets/Template.psd>` to create a custom icon.
  :::
- `Icon` Base64 encoded disk TIFF image icon to be used in protocol dropdown menu instead of `Disk` icon
- `Context` Currently used for 
  * Login context path for [OpenStack Swift](../openstack/index.md) profiles.
  * Prefix all requests with path for [S3](../s3/index.md) profiles.
- `Anonymous Configurable` Boolean if anonymous access is configurable.
- `Path Configurable` Boolean if default path is configurable.
- `Certificate Configurable` Boolean if client certificate is configurable.
- `Region` Region name to limit listing containers of a specific region only for [OpenStack Swift](../openstack/index.md) and [S3](../s3/index.md) profiles.
  :::{admonition} S3
  :class: tip

  This value is used for AWS4 signatures when no location can be deferred from the URI for third-party S3 providers.
  :::
- `Regions` List of regions supported by the provider. This will populate options in the *Regions* dropdown when creating a new [top level folder](../s3/index.md#creating-a-bucket) for [S3](../s3/index.md) and [OpenStack Swift](../openstack/swiftstack.md) connections.
- `OAuth Client ID` For protocols using OAuth 2.0 you can override the registered application client ID with the provider.
  * A profile can omit the `OAuth Client ID` to prompt the user for manual input when connecting.
- `OAuth Client Secret` For protocols using OAuth 2.0 you can override the registered application client secret with the provider.
  * A profile can define an empty value for `OAuth Client Secret`. The OAuth authorization flow will then use no client secret in client parameters to authenticate with the server.
  * A profile can omit the `OAuth Client Secret` to prompt the user for manual input when connecting.
- `Authorization` Set to `AWS2` to default to AWS2 signature authentication for S3. Default is `AWS4HMACSHA256`.
- `Properties` List of custom protocol-specific properties. You can set [hidden configuration options](../../cyberduck/preferences.md#hidden-configuration-options) for a specific connection profile. Example usages can be found in:
  * [FTP (Compatibility Mode).cyberduckprofile](https://github.com/iterate-ch/profiles/blob/master/FTP%20(Compatibility%20Mode).cyberduckprofile)
  * [FTP-SSL (Compatibility Mode).cyberduckprofile](https://github.com/iterate-ch/profiles/blob/master/FTP-SSL%20(Compatibility%20Mode).cyberduckprofile)
  * [S3 (Deprecated path style requests).cyberduckprofile](https://github.com/iterate-ch/profiles/blob/master/S3%20(Deprecated%20path%20style%20requests).cyberduckprofile)

#### Example

```xml
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

### Disk Icon Template

- {download}`Adobe Photoshop disk template file<https://github.com/iterate-ch/profiles/blob/master/assets/Template.psd>`

### Icon Set

Create a *multi-TIFF* containing the needed icon sizes:
1. Create a high-resolution *.png* file based on the PSD template
2. Use the following script to generate the different resolutions and the multi-TIFF *disk.tiff* file:
    ```
    png=[LOCATION_OF_HIGH_RESOLUTION_PNG]
    tmp=$TMPDIR
    target=[TARGET_FOLDER]
    /usr/bin/sips -s format png -z 128 128 -s dpiHeight 144.0 -s dpiWidth 144.0 ${png} --out ${tmp}/icon_64x64@2x.png
    /usr/bin/sips -s format png -z 64 64 -s dpiHeight 72.0 -s dpiWidth 72.0 ${png} --out ${tmp}/icon_64x64.png
    /usr/bin/sips -s format png -z 96 96 -s dpiHeight 144.0 -s dpiWidth 144.0 ${png} --out ${tmp}/icon_96@2x.png
    /usr/bin/sips -s format png -z 48 48 -s dpiHeight 72.0 -s dpiWidth 72.0 ${png} --out ${tmp}/icon_96.png
    /usr/bin/sips -s format png -z 256 256 -s dpiHeight 144.0 -s dpiWidth 144.0 ${png} --out ${tmp}/icon_256@2x.png
    /usr/bin/sips -s format png -z 128 128 -s dpiHeight 72.0 -s dpiWidth 72.0 ${png} --out ${tmp}/icon_256.png
    /usr/bin/tiffutil -cathidpicheck ${tmp}/icon_64x64@2x.png ${tmp}/icon_64x64.png ${tmp}/icon_96.png ${tmp}/icon_96@2x.png ${tmp}/icon_256.png ${tmp}/icon_256@2x.png -out ${target}/ disk.tiff
    ```
3. Use the command `cat disk.tiff | base64 -b 70` to generate the base64 version of the multi-TIFF file. This final version will be used for the connection profile.

## Sample Connection Profiles

### Google Custom OAuth Client ID

- [Custom OAuth 2.0 Client ID for Google Cloud Storage and Google Drive](google_client_id.md).

### S3 and OpenID Connect Federation 

Customization of connection profiles using OpenID Connect provider and AssumeRoleWithWebIdentity STS API
- [Sample connection profiles for S3 and OpenID Connect Federation](aws_oidc.md)
