Info Window
====

```{contents} Content
:depth: 2
:local:
```

````{tabs}
```{group-tab} Cyberduck

Select the file in the browser and choose *File → Info (macOS `⌘I` Windows `Alt+Return`)* to display detailed information on a file in a tool window. You can choose in the [Preferences](preferences.md) in the *Browser* tab to use the info window as an inspector of the currently selected files in the browser or open a new panel window to compare different files.

```
```{group-tab} Mountain Duck

Select a file or folder within the Finder and choose *Mountain Duck → Info* from the context menu to display detailed information on the selected content in a tool window.

```
````

## General Panel

### Change Filename

Type in the new filename and press *Tab* to leave the text field and commit the change.

```{image} _images/General.png
:alt: General
:width: 600px
```

### Calculate Folder Size

Calculate the size recursively of all contained files.

## Versions Panel

A list of file versions can be viewed in the *Versions* tab of the Info window. The files can be reverted to a choosen version.

```{image} _images/Info_Panel_Versions.png
:alt: Versions Tab
:width: 600px
```

The following protocols support to review previous versions of files. On macOS, this opens a *QuickLook* window. On Windows, this downloads and opens the file in the default editor. Some protocols also display previous versions of files in [browser](browser.md) when enabling *View → Show Hidden*.

| **Protocol** | **Revert previous version** | **Open/Quick Look previous version** | **Delete version** | **Displayed in browser with *View → Show Hidden*** |
| --- | --- | --- | --- | --- |
| **[S3](../protocols/s3/index.md)** | ✅ | ✅ | ✅ | ✅ |
| **[Backblaze B2](../protocols/b2.md)** | ✅ | ✅ | ✅ | ✅ |
| **[Google Drive](../protocols/google_drive.md)** | ❌ | ✅ | ✅ | ✅ |
| **[Google Storage](../protocols/google_cloud_storage.md)** | ✅ | ✅ | ✅ | ✅ |
| **[Microsoft OneDrive](../protocols/onedrive.md)** | ✅ | ✅ | ❌ | ❌ |
| **[Microsoft Sharepoint](../protocols/sharepoint.md)** | ❌ | ✅ | ❌ | ❌ |
| **[DRACOON](../protocols/dracoon.md)** | ✅ | ❌ | ✅ | ❌ | 
| **[Dropbox](../protocols/dropbox.md)** | ✅ | ✅ | ❌ | ❌ |

```{note}
Using S3 or Backblaze B2, versions will only be displayed if bucket versioning is enabled.
```

## UNIX Permissions

Change the permissions on a particular file or folder when connected to a [FTP](../protocols/ftp.md) or [SFTP](../protocols/sftp.md) server. You can also select multiple files in the browser to edit permissions. Click the checkboxes or enter the [octal notation](http://en.wikipedia.org/wiki/File_system_permissions#Symbolic_notation). The recursive options will update all files within a folder but will not change the executable bit for files if not already set when recursively updating a directory.

```{image} _images/UNIX_Permissions.png
:alt: UNIX Permissions
:width: 400px
```

## Access Control List (ACL)

Edit access control list for fine grained user permissions when connected to [Amazon S3](../protocols/s3/index.md) or [Google Cloud Storage](../protocols/google_cloud_storage.md).

- [S3 ACLs](../protocols/s3/index.md#access-control-acl)
- [Google Storage ACLs](../protocols/google_cloud_storage.md#acls)

```{image} _images/Access_Control_Lists.png
:alt: Access Control Lists
:width: 500px
```

## CDN Panel

Manage [Amazon CloudFront](../cdn/cloudfront.md) and [Rackspace/Akamai](../cdn/akamai.md) distributions ([CDN](../cdn/index.md)) respectively.

### Deployment Status

Upon changing configuration parameters of a distribution configuration, the settings are not distributed immediately in the CDN. While the deployment is in progress (which can take up to 15 minutes), the status *In Progress* is displayed. The updates are fully propagated throughout the CloudFront system when the distribution's state switches from *In Progress* to *Deployed*.

### CloudFront Access Logging

When this option is enabled, access logs are written to `<bucketname>/logs`. The changes to the logging configuration take effect within 12 hours. The logging option is supported for both download and streaming distributions. Choose the target bucket for access logs in the dropdown menu listing all buckets of your account. It is considered best practice to choose a different logging target for each distribution.

### Origin

The source of the content where CloudFront fetches the content to be served in the edge location of the CDN. This is a [S3](../protocols/s3/index) bucket or your custom origin.

### Where
The `cloudfront.net` domain assigned to your distribution. This is directing to the edge location in the CDN next to the user requesting an URL.

### CNAMEs
Enter a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) (alias in the Domain Name System) for the hostname of the distribution given by CloudFront. To use multiple CNAMEs for a single distribution, the hostnames must be space delimited. The CNAME must be registered on the nameserver responsible for your domain and point to `cloudfront.net` domain assigned to your distribution.

Example configuration:

	;; QUESTION SECTION:
	;cdn.cyberduck.ch.		IN	A
	
	;; ANSWER SECTION:
	cdn.cyberduck.ch.	1576	IN	CNAME	d15bfu8of7vup8.cloudfront.net.

### Index File
You can assign a default root object to your HTTP or HTTPS distribution. This default object will be served when Amazon CloudFront receives a request for the root of your distribution – i.e., your distribution’s domain name by itself.

When you define a default root object, a user request that calls the root of your distribution returns the default root object. For example, if you designate the file `index.html` as your default root object, a request for `http://d604721fxaaqy9.cloudfront.net/` returns `http://d604721fxaaqy9.cloudfront.net/index.html`.

### Object Invalidation
[Invalidation](http://aws.amazon.com/about-aws/whats-new/2010/08/31/cloudfront-adds-invalidation-feature/) is one way to remove a distribution object from an edge server cache before the expiration setting on the object's header. Invalidation clears the object from the edge server cache, and a subsequent request for the object will cause CloudFront to return to the origin to fetch the latest version of the object.

```{note}
Use the Invalidate option *File → Info → Distribution (CDN)* to invalidate files from edge locations.
```

## Amazon S3 Panel

Settings specific to the [Amazon S3](../protocols/s3/index.md) service.

- The geographic location of the bucket.
- [Publicly accessible URL](../protocols/s3/index.md#pre-signed-temporary-urls) to the file with a validity of 24 hours. Signed URLs with a different life are available in the *Edit → Copy URL* menu.
- Enabling [access logs](../protocols/s3/index.md#bucket-access-logging) for the bucket.
- Choose storage class ([Reduced Redundancy Storage (RRS)](../protocols/s3/index.md#storage-class)). Settings will be applied recursively if a folder is selected.
- Configure [bucket versioning](../protocols/s3/index.md#versions).
- Configure [Multi-Factor Authentication (MFA) Delete](../protocols/s3/index.md#multi-factor-authentication-mfa-delete).
- Configure [Transfer Acceleration](../protocols/s3/index.md#transfer-acceleration).

```{image} _images/Amazon_S3.png
:alt: Amazon S3
:width: 500px
```

## Metadata (HTTP headers)

View and modify metadata attributes of files.

Any non-standard HTTP header values are (transparently) prefixed with the following values following the guidelines from the different providers:

- Values are prefixed with `x-amz-meta-` for [S3](../protocols/s3/index.md) and [Google Storage](../protocols/google_cloud_storage.md).
- Values are prefixed with `X-Object-Meta-` for [CloudFiles](../protocols/openstack/cloudfiles.md).

```{image} _images/Metadata.png
:alt: Metadata
:width: 500px
```
