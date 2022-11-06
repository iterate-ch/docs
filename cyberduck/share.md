Share Files
====

Many storage providers have an option to share a file with a third party without access to your account with a publicly accessible link. Depending on the provider, the link may be auto expiring and no longer valid after a given period or a password can be set required to download the file. Some providers support to _Request files…_ from others by creating an URL that allows others to add files to your account.

```{contents} Content
:depth: 2
:local:
```

## Availability

The table below shows the protocols which support to share files using _Share…_ or _Request files…_.

|| **Share…**   || **Request files…** |
|--------------|--------------------| --- | --- |
| **Protocol** | **Folder**         | **File** | **Folder** |
| S3           | ❌                  | ✅ | ❌ |
| B2           | ❌                  | ✅ | ❌ |
| Nextcloud    | ✅                  | ✅ | ✅ |
| OneDrive     | ✅                  | ✅ | ❌ |
| Google Drive | ✅                  | ✅ | ❌ |
| Dropbox      | ✅                  | ✅ | ✅ |
| DRACOON      | ✅                  | ✅ | ✅ |
| Box          | ✅                  | ✅ | ❌ |

## Providers

Providers with support to share a file using a public, password protected or temporary URL and request files to be uploaded.
* _Share…_. Create link for file to be made available publicly or password protected.
* _Request files…_. to create link to request upload of files to your account.
* _Pre-Signed URL_. Create temporary link to download a file.

### S3

For connections using [S3](../protocols/s3/index.md) protocol.

`````{tabs}
````{group-tab} Cyberduck

Create a [pre-signed temporary](../protocols/s3/index.md#pre-signed-temporary-urls) URL. Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [pre-signed temporary](../protocols/s3/index.md#pre-signed-temporary-urls) URL. Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

```{image} ../cyberduck/_images/S3_Pre-Signed_URL.png
:alt: Pre-Signed URL
:width: 400px
```

````
`````

### OpenStack Swift

For connections using [OpenStack Swift](../protocols/openstack/index.md) protocol.

`````{tabs}
````{group-tab} Cyberduck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../protocols/openstack/index.md#temporary-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../protocols/openstack/index.md#temporary-urls). Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

````
`````

### Azure

For connections to [Azure](../protocols/azure.md). 

`````{tabs}
````{group-tab} Cyberduck

Create a [Shared Access Signature URL](../protocols/azure.md#shared-access-signature-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [Shared Access Signature URL](../protocols/azure.md#shared-access-signature-urls). Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

````
`````

### Backblaze B2

For connections to [Backblaze B2](../protocols/b2.md).

`````{tabs}
````{group-tab} Cyberduck

Create an [authorized URL](../protocols/b2.md#authorized-url) to make files available publicly expiring after 7 days. Choose *File → Share…*.

```{image} ../cyberduck/_images/B2_Authorized_URL.png
:alt: B2 Authorized URL
:width: 600px
```

````
````{group-tab} Mountain Duck

Create an [authorized URL](../protocols/b2.md#authorized-url) to make files available publicly expiring after 7 days. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

````
`````

### DRACOON

For [DRACOON](../protocols/dracoon.md) connections.

`````{tabs}
````{group-tab} Cyberduck

Create an [download share](../protocols/dracoon.md#download-share) for a file or folder. Choose *File → Share…*. Optionally set a password required to download the file. Uncheck *Require Passphrase* to create a public with no password protection.

````
````{group-tab} Mountain Duck

Create an [download share](../protocols/dracoon.md#download-share) for a file or folder. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

````
`````

### OneDrive & Sharepoint

For bookmarks configured with [Microsoft OneDrive](../protocols/onedrive.md) & [Microsoft SharePoint](../protocols/sharepoint.md) protocols.

`````{tabs}
````{group-tab} Cyberduck

Create an [shared link](../protocols/onedrive.md) for a file or folder. Choose *File → Share…*.

````
````{group-tab} Mountain Duck

Create a [shared link](../protocols/onedrive.md) for a file or folder. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

````
`````

### Dropbox

For connections to [Dropbox](../protocols/dropbox.md).

`````{tabs}
````{group-tab} Cyberduck

You can share an [URL](../protocols/dropbox.md#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Uncheck *Require Passphrase* to create a public URL with no password protection. Choose *File → Share…*.

```{image} ../cyberduck/_images/Passphrase_Prompt_Dropbox_Share.png
:alt: Passphrase Prompt Dropbox Share
:width: 400px
```

````
````{group-tab} Mountain Duck

You can share an [URL](../protocols/dropbox.md#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Uncheck *Require Passphrase* to create a public URL with no password protection. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

```{image} ../cyberduck/_images/Passphrase_Prompt_Dropbox_Share.png
:alt: Passphrase Prompt Dropbox Share
:width: 400px
```

````
`````

### Google Drive

For connections to [Google Drive](../protocols/google_drive.md).

`````{tabs}
````{group-tab} Cyberduck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *File → Share…*.

````
````{group-tab} Mountain Duck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

```{image} ../cyberduck/_images/Share_File_Google_Drive_.png
:alt: Share File Google Drive
:width: 400px
```

````
`````

### [NextCloud & ownCloud]

For connections to [NextCloud & ownCloud](../protocols/webdav/nextcloud.md) servers.

`````{tabs}
````{group-tab} Cyberduck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Uncheck *Require Passphrase* to create a public URL with no password protection. Choose *File → Share…* for download shares or *File → Request files…* for upload shares.

````
````{group-tab} Mountain Duck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Uncheck *Require Passphrase* to create a public share with no password protection. Choose *Share…* for download shares or *Request files…* for upload shares from the [context menu](../mountainduck/interface.md#share).

```{image} ../cyberduck/_images/Download_Share_Context_Menu.png
:alt: Download Share Context Menu
:width: 300px
```

````
`````

### Box

For connections to [Box](../protocols/box.md).

`````{tabs}
````{group-tab} Cyberduck

Create download shares by choosing *File → Share…*. Optionally set a password required to download the file or folder. Uncheck *Require Passphrase* to create a public URL without password protection. A Box account is not required to open the URL.

````
````{group-tab} Mountain Duck

Create download shares for files and folders by choosing *Share…* from the [context menu](../mountainduck/interface.md#share). Optionally set a password required to download the file or folder. Uncheck *Require Passphrase* to create a public URL without password protection. A Box account is not required to open the URL.

```{image} ../cyberduck/_images/Download_Share_Box.png
:alt: Download Share Box
:width: 400px
```

````
`````

### FTP, SFTP & WebDAV

If you connect to a web root using ### [FTP](../protocols/ftp.md), [SFTP](../protocols/sftp.md) or [WebDAV](../protocols/webdav/index.md), refer to [HTTP URL](../cyberduck/bookmarks.md#http-url) on how to configure your bookmark to allow copying a HTTP URL for a selected file. With a valid configuration, you can open the corresponding HTTP URL of a file selected with your default web browser or copy the URL to the clipboard. To manage permissions, refer to [UNIX Permissions (FTP/SFTP)](info.md#unix-permissions).

```{note}
You must use [Cyberduck](https://cyberduck.io) to edit the Web URL in a bookmark. The Web URL will replace your server address in URLs available in *Copy URL* .
```