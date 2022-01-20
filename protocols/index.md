Protocols
====

```{toctree}
:hidden:
:titlesonly:
profiles
openstack/index
s3/index
webdav/index
azure
b2
dracoon
dropbox
files.com
ftp
google_client_id
google_cloud_storage
google_drive
box
irods
onedrive
sftp
sharepoint
spectra
```

All major server and cloud storage protocols are supported to connect to just about any server or cloud storage. Support for the listed protocols and [connection profiles](profiles.md) is available in [Cyberduck](../cyberduck/index.md), [Cyberduck CLI](../cli/index.md) and [Mountain Duck](../mountainduck/index.md).

### [FTP](ftp.md)
With support for secure TLS connections and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../cdn/cloudfront) option.

### [Amazon S3](s3/index.md)
Transfer files to your S3 account and browse the S3 buckets and files in a hierarchical way. Supports Amazon Web Services (AWS) and many third party providers.

- [S3 providers](s3/index.md#third-party-providers)

### [Google Cloud Storage](google_cloud_storage.md)

Transfer files to your Google Storage account and browse files, manage ACLs and bucket configurations.

### [Backblaze B2](b2.md)
Backblaze B2 Cloud Storage is ¼ of the price of Amazon S3

### [WebDAV](webdav/index.md)
Connect to any WebDAV compliant server using both HTTP and HTTP/SSL and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../cdn/cloudfront.md) option.

- [WebDAV providers](webdav/index.md#providers)

### [SSH/SFTP](sftp.md)
Advanced configuration for SSH connections using public key authentication and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../cdn/cloudfront.md) option.

### [OpenStack Object Storage](openstack/index.md)
Connect to cloud storage providers using OpenStack Swift for the storage protocol. Includes support for [Rackspace Cloud Files](openstack/cloudfiles).

- [OpenStack Providers](openstack/index.md#third-party-providers)

### [Windows Azure](azure.md)
Massively scalable object storage for unstructured data.

### [Microsoft OneDrive](onedrive.md)
Access OneDrive without syncing to your computer.

### [Microsoft SharePoint](sharepoint.md)
Connect to SharePoint Server and SharePoint Online.

### [Google Drive](google_drive.md)
Access all your documents and upload files of any type to use your Google Drive account for storage.

### [Box](box.md)
Simple, secure file sharing and collaboration from anywhere.

### [Dropbox](dropbox.md)
Access Dropbox without syncing to your computer.

### [DRACOON](dracoon.md)
A highly secure, platform-independent enterprise filesharing solution

### [Files.com](files.com.md)
Files.com is Smart Cloud Storage for modern teams

### [iRODS](irods.md)
The Integrated Rule-Oriented Data System (iRODS) is an open source data management software used by research organizations and government agencies worldwide.

### [Spectra BlackPearl Deep Storage Gateway](spectra.md)

### Local Disk
Open a window to browse your local hard disk to drag files for download or upload to a remote server from within the application. You can browse [Cryptomator Vaults](../cryptomator/index.md#access-vaults-on-local-disk) stored on your computer.


# Connection Profiles

[Connection profiles](profiles.md) (`.cyberduckprofile`) are plugins describing specific connection settings for a hosting provider to make it easier to setup a connection to your provider. A connection profile is installed and adds a provider option in the protocol selection drop down menu in the *Connection* and *Bookmark* panels. No need to enter the connection details manually other than credentials.

## Preferences → Profiles

Select connection protocols in _Preferences → Profiles_ to be installed in addition to the default protocols listed below. Either scroll through the list or use the search function to look for a specific profile. The connection profile will be installed after enabling the corresponding checkbox. To disable a connection profile simply uncheck the checkbox. The profile will be disabled after closing the application.

`````{tabs}
````{group-tab} macOS

```{image} _images/Preferences_Profiles_macOS.png
:alt: macOS
:width: 600px
```

````
````{group-tab} Windows

```{image} _images/Preferences_Profiles.png
:alt: Windows
:width: 500px
```
````
`````

```{note}
You cannot disable default protocols or connection profiles currently in use in any bookmark.
```

# Modification Date
Retaining the modification date for files uploaded is not supported for all protocols.

```{admonition} Mountain Duck
:class: attention
Protocols with limited support for modification dates only allow to set the modification for new files uploaded but not changing it later.
```

| Protocol             | Native Support | Limited Support |
|----------------------| :---: | :---: |
| Local Disk           | ✅ ||
| SFTP                 | ✅ ||
| FTP                  | ✅ ||
| Google Drive         | ✅ ||
| Google Cloud Storage | ✅ ||
| Microsoft OneDrive   | ✅ ||
| Microsoft Sharepoint | ✅ ||
| Files.com            | ✅ ||
| DRACOON              | ✅ ||
| Backblaze B2         | ❌	| ✅ |
| Box.com              | ❌	| ✅ |
| Dropbox              | ❌	| ✅ |
| Nextcloud            | ❌ | ✅ |
| ownCloud             | ❌	| ✅ |
| S3                   | ❌ | ✅ |
| Windows Azure        | ❌ | ❌ |
| OpenStack Object Storage        | ❌ | ❌ |

```{admonition} Interoperability
:class: attention
- **WebDAV**: Saving the modification dates requires support from server storing metadata in custom namespace
- **FTP**: Requires support from server for `MFMT` or `UTIME` extensions
```
