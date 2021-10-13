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

## Deployment Status

Upon changing configuration parameters of a distribution configuration, the settings are not distributed immediately in the CDN. While the deployment is in progress (which can take up to 15 minutes), the status *In Progress* is displayed. The updates are fully propagated throughout the CloudFront system when the distribution's state switches from *In Progress* to *Deployed*.

## CloudFront Access Logging

When this option is enabled, access logs are written to `<bucketname>/logs`. The changes to the logging configuration take effect within 12 hours. The logging option is supported for both download and streaming distributions. Choose the target bucket for access logs in the dropdown menu listing all buckets of your account. It is considered best practice to choose a different logging target for each distribution.

## Origin

The source of the content where CloudFront fetches the content to be served in the edge location of the CDN. This is a [S3](../Protocols/S3/index) bucket or your custom origin.

## Where
The `cloudfront.net` domain assigned to your distribution. This is directing to the edge location in the CDN next to the user requesting an URL.

## CNAMEs
Enter a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) (alias in the Domain Name System) for the hostname of the distribution given by CloudFront. To use multiple CNAMEs for a single distribution, the hostnames must be space delimited. The CNAME must be registered on the nameserver responsible for your domain and point to `cloudfront.net` domain assigned to your distribution.

Example configuration:

	;; QUESTION SECTION:
	;cdn.cyberduck.ch.		IN	A
	
	;; ANSWER SECTION:
	cdn.cyberduck.ch.	1576	IN	CNAME	d15bfu8of7vup8.cloudfront.net.

## Index File
You can assign a default root object to your HTTP or HTTPS distribution. This default object will be served when Amazon CloudFront receives a request for the root of your distribution – i.e., your distribution’s domain name by itself.

When you define a default root object, a user request that calls the root of your distribution returns the default root object. For example, if you designate the file `index.html` as your default root object, a request for `http://d604721fxaaqy9.cloudfront.net/` returns `http://d604721fxaaqy9.cloudfront.net/index.html`.

## Object Invalidation
[Invalidation](http://aws.amazon.com/about-aws/whats-new/2010/08/31/cloudfront-adds-invalidation-feature/) is one way to remove a distribution object from an edge server cache before the expiration setting on the object's header. Invalidation clears the object from the edge server cache, and a subsequent request for the object will cause CloudFront to return to the origin to fetch the latest version of the object.

```{note}
Use the Invalidate option *File → Info → Distribution (CDN)* to invalidate files from edge locations.
```

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