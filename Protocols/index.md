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
Google_Cloud_Storage
Google_Drive
iRODS
OneDrive
SFTP
SharePoint
Spectra
```

All major server and cloud storage protocols are supported to connect to just about any server you want. Support for the listed protocols and [connection profiles](../Cyberduck/Profiles) is available in [Cyberduck](../Cyberduck/index), [Cyberduck CLI](../CLI/index) and [Mountain Duck](../Mountain_Duck/index).

# Supported Protocols

All major server and cloud storage protocols are supported to connect to just about any server or cloud storage.

## [FTP](FTP)

With support for secure TLS connections and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront) option.

## [Amazon S3](S3/index)

Transfer files to your S3 account and browse the S3 buckets and files in a hierarchical way. Supports Amazon Web Services (AWS) and many third party providers.

- [S3 providers](S3/index#third-party-providers)

## [Google Cloud Storage](Google_Cloud_Storage)

Transfer files to your Google Storage account and browse files, manage ACLs and bucket configurations.

## [Backblaze B2](B2)

Backblaze B2 Cloud Storage is ¼ of the price of Amazon S3

## [WebDAV](WebDAV/index)

Connect to any WebDAV compliant server using both HTTP and HTTP/SSL and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront) option.

- [WebDAV providers](WebDAV/index#providers)

## [SSH/SFTP](SFTP)

Advanced configuration for SSH connections using public key authentication and custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront) option.

## [OpenStack Object Storage](OpenStack/index)
Connect to cloud storage providers using OpenStack Swift for the storage protocol. Includes support for [Rackspace Cloud Files](OpenStack/CloudFiles).

- [OpenStack Providers](OpenStack/index#third-party-providers)

## [Windows Azure](Azure)

Massively scalable object storage for unstructured data.

## [Microsoft OneDrive](OneDrive)

Access OneDrive without syncing to your computer.

## [Microsoft SharePoint](SharePoint)

Connect to SharePoint Server and SharePoint Online.

## [Google Drive](Google_Drive)

Access all your documents and upload files of any type to use your Google Drive account for storage.

## [Dropbox](Dropbox)

Access Dropbox without syncing to your computer.

## [DRACOON](Dracoon)

A highly secure, platform-independent enterprise filesharing solution

## [Files.com](Files.com)

Files.com is Smart Cloud Storage for modern teams

## [iRODS](iRODS)

The Integrated Rule-Oriented Data System (iRODS) is an open source data management software used by research organizations and government agencies worldwide.

## [Spectra BlackPearl Deep Storage Gateway](Spectra)

# Local Disk
Open a window to browse your local hard disk to drag files for download or upload to a remote server from within the application. You can browse [Cryptomator Vaults](../Cryptomator/index) stored on your computer.

# Connection Profiles

[Connection profiles](../Cyberduck/Profiles) (`.cyberduckprofile`) are plugins describing specific connection settings for a hosting provider to make it easier to setup a connection to your provider. A connection profile is installed and adds a provider option in the protocol selection drop down menu in the *Connection* and *Bookmark* panels. No need to enter the connection details manually other than credentials.

## Preferences → Profiles

```{note}
Prelimitary documentation for Cyberduck 8 and Mountain Duck version 4.8
```

Select connection protocols to be installed in addition to the default protocols listed above. The connection profile will be installed after enabling the corresponding checkbox. To disable a connection profile simply uncheck the checkbox. The profile will be disabled after closing the application.

```{note}
You can't disable the default protocols. If you disable the connection profile used in a bookmark, the bookmark won't work after restarting the application.
```