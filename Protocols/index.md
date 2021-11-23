Protocols
===

```{toctree}
:hidden:

OpenStack/index
S3/index
WebDAV/index
Azure
B2
Dracoon
Dropbox
Files.com
FTP
Google_Client_ID
Google_Cloud_Storage
Google_Drive
iRODS
OneDrive
SFTP
SharePoint
Spectra
```

All major server and cloud storage protocols are supported to connect to just about any server you want. Support for the listed protocols and [connection profiles](../Cyberduck/Profiles.md) is available in [Cyberduck](../Cyberduck/index.md), [Cyberduck CLI](../CLI/index.md) and [Mountain Duck](../Mountain_Duck/index.md).

# Supported Protocols

All major server and cloud storage protocols are supported to connect to just about any server or cloud storage.

## [FTP](FTP.md)

With support for secure TLS connections and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront) option.

## [Amazon S3](S3/index.md)

Transfer files to your S3 account and browse the S3 buckets and files in a hierarchical way. Supports Amazon Web Services (AWS) and many third party providers.

- [S3 providers](S3/index.md#third-party-providers)

## [Google Cloud Storage](Google_Cloud_Storage.md)

Transfer files to your Google Storage account and browse files, manage ACLs and bucket configurations.

## [Backblaze B2](B2.md)

Backblaze B2 Cloud Storage is ¼ of the price of Amazon S3

## [WebDAV](WebDAV/index.md)

Connect to any WebDAV compliant server using both HTTP and HTTP/SSL and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront.md) option.

- [WebDAV providers](WebDAV/index.md#providers)

## [SSH/SFTP](SFTP.md)

Advanced configuration for SSH connections using public key authentication and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront.md) option.

## [OpenStack Object Storage](OpenStack/index.md)
Connect to cloud storage providers using OpenStack Swift for the storage protocol. Includes support for [Rackspace Cloud Files](OpenStack/CloudFiles).

- [OpenStack Providers](OpenStack/index.md#third-party-providers)

## [Windows Azure](Azure.md)

Massively scalable object storage for unstructured data.

## [Microsoft OneDrive](OneDrive.md)

Access OneDrive without syncing to your computer.

## [Microsoft SharePoint](SharePoint.md)

Connect to SharePoint Server and SharePoint Online.

## [Google Drive](Google_Drive.md)

Access all your documents and upload files of any type to use your Google Drive account for storage.

## [Dropbox](Dropbox.md)

Access Dropbox without syncing to your computer.

## [DRACOON](Dracoon.md)

A highly secure, platform-independent enterprise filesharing solution

## [Files.com](Files.com.md)

Files.com is Smart Cloud Storage for modern teams

## [iRODS](iRODS.md)

The Integrated Rule-Oriented Data System (iRODS) is an open source data management software used by research organizations and government agencies worldwide.

## [Spectra BlackPearl Deep Storage Gateway](Spectra.md)

# Local Disk
Open a window to browse your local hard disk to drag files for download or upload to a remote server from within the application. You can browse [Cryptomator Vaults](../Cryptomator/index.md) stored on your computer.

# Connection Profiles

[Connection profiles](../Cyberduck/Profiles.md) (`.cyberduckprofile`) are plugins describing specific connection settings for a hosting provider to make it easier to setup a connection to your provider. A connection profile is installed and adds a provider option in the protocol selection drop down menu in the *Connection* and *Bookmark* panels. No need to enter the connection details manually other than credentials. 

## Preferences → Profiles

Select connection protocols in _Preferences → Profiles_ to be installed in addition to the default protocols listed above. The connection profile will be installed after enabling the corresponding checkbox. To disable a connection profile simply uncheck the checkbox. The profile will be disabled after closing the application.

```{note}
You cannot disable any of the default protocols or a connection profile in use.
```
