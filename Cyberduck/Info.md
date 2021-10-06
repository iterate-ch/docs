Info Window
===

Select the file in the browser and choose *File → Info (macOS `⌘-I` Windows `Alt+Return`)* to display detailed information on s file in a tool window. You can choose in the [Preferences](Preferences) in the *Browser* tab to use the info window as an inspector of the currently selected files in the browser or open a new panel window to compare different files.

# General Panel

## Change Filename

Type in the new filename and press *Tab* to leave the text field and commit the change.

```{image} _images/General.png
:alt: Send Command
:width: 600px
```

## Calculate Folder Size

Calculate the size recursively of all contained files.

# UNIX Permissions (FTP/SFTP)

Change the permissions on a particular file or folder when connected to a [FTP](../Protocols/FTP) or [SFTP](../Protocols/SFTP) server. You can also select multiple files in the browser to edit permissions. Click the checkboxes or enter the [octal notation](http://en.wikipedia.org/wiki/File_system_permissions#Symbolic_notation). The recursive options will update all files within a folder but will not change the executable bit for files if not already set when recursively updating a directory.

```{image} _images/UNIX_Permissions.png
:alt: Send Command
:width: 400px
```

# Access Control List (ACL)

Edit access control list for fine grained user permissions when connected to [Amazon S3](../Protocols/S3/index) or [Google Cloud Storage](../Protocols/Google_Cloud_Storage).

- [S3 ACLs](../Protocols/S3/index#access-control-acl)
- [Google Storage ACLs](../Protocols/Google_Cloud_Storage#acls)

```{image} _images/Access_Control_Lists.png
:alt: Send Command
:width: 500px
```

# CDN Panel

Manage [Amazon CloudFront](../CDN/CloudFront) and [Rackspace/Akamai](../CDN/Akamai) distributions ([CDN](../CDN/index)) respectively.

# Amazon S3 Panel

Settings specific to the [Amazon S3](../Protocols/S3/index) service.

- The geographic location of the bucket.
- [Publicly accessible URL](../Protocols/S3/index#pre-signed-temporary-urls) to the file with a validity of 24 hours. Signed URLs with a different life are available in the *Edit → Copy URL* menu.
- [Torrent URL](../Protocols/S3/index#bit-torrent-urls) to the file.
- Enabling [access logs](../Protocols/S3/index#bucket-access-logging) for the bucket.
- Choose storage class ([Reduced Redundancy Storage (RRS)](../Protocols/S3/index#storage-class)). Settings will be applied recursively if a folder is selected.
- Configure [bucket versioning](../Protocols/S3/index#versions).
- Configure [Multi-Factor Authentication (MFA) Delete](../Protocols/S3/index#multi-factor-authentication-mfa-delete).
- Configure [Transfer Acceleration](../Protocols/S3/index#transfer-acceleration).

```{image} _images/Amazon_S3.png
:alt: Send Command
:width: 500px
```

# Metadata (HTTP headers)

View and modify metadata attributes of files.

Any non-standard HTTP header values are (transparently) prefixed with the following values following the guidelines from the different providers:

- Values are prefixed with `x-amz-meta-` for [S3](../Protocols/S3/index) and [Google Storage](../Protocols/Google_Cloud_Storage).
- Values are prefixed with `X-Object-Meta-` for [CloudFiles](../Protocols/OpenStack/CloudFiles).

```{image} _images/Metadata.png
:alt: Send Command
:width: 500px
```