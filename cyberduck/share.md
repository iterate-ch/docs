Share Files
====

Many storage providers have an option to share a file with a third party without access to your account with a publicly accessible link. Depending on the provider, the link may be auto expiring and no longer valid after a given period or a password can be set required to download the file.

```{contents} Content
:depth: 2
:local:
```

## Availability of Upload and Download Shares

*Upload* and *Download Shares* aren't available for all supported protocols. The table below shows the protocols which either support *Upload* or *Download Shares*.

|| **Download Share** || **Upload Share** |
| --- | --- | --- | --- |
| **Protocol** | **Folder** | **File** | **Folder** |
| S3 | ❌ | ✅ | ❌ |
| B2 | ❌ | ✅ | ❌ |
| Nextcloud | ✅ | ✅ | ✅ |
| OneDrive | ✅ | ✅ | ❌ |
| Google Drive | ✅ | ✅ | ❌ |
| Dropbox | ❌ | ✅ | ❌ |
| DRACOON | ✅ | ✅ | ✅ |
| Box | ✅ | ✅ | ❌ |

## Providers with support to share a file using a public, password protected or temporary URL

### [S3](../protocols/s3/index.md)

`````{tabs}
````{group-tab} Cyberduck

Create a [pre-signed temporary](../protocols/s3/index.md#pre-signed-temporary-urls) URL. Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [pre-signed temporary](../protocols/s3/index.md#pre-signed-temporary-urls) URL. Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

```{image} _images/S3_Pre-Signed_URL.png
:alt: Pre-Signed URL
:width: 400px
```

````
`````

### [OpenStack Swift](../protocols/openstack/index.md)

`````{tabs}
````{group-tab} Cyberduck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../protocols/openstack/index.md#temporary-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../protocols/openstack/index.md#temporary-urls). Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

````
`````

### [Azure](../protocols/azure.md)

`````{tabs}
````{group-tab} Cyberduck

Create a [Shared Access Signature URL](../protocols/azure.md#shared-access-signature-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [Shared Access Signature URL](../protocols/azure.md#shared-access-signature-urls). Choose *Copy URL* from the [context menu](../mountainduck/interface.md#share).

````
`````

### [Backblaze B2](../protocols/b2.md)

`````{tabs}
````{group-tab} Cyberduck

Create an [authorized URL](../protocols/b2.md#authorized-url) to make files available publicly expiring after 7 days. Choose *File → Share…*.

````
````{group-tab} Mountain Duck

Create an [authorized URL](../protocols/b2.md#authorized-url) to make files available publicly expiring after 7 days. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

```{image} _images/B2_Authorized_URL.png
:alt: B2 Authorized URL
:width: 600px
```

````
`````

### [DRACOON](../protocols/dracoon.md)

`````{tabs}
````{group-tab} Cyberduck

Create an [download share](../protocols/dracoon.md#download-share) for a file or folder. Choose *File → Share…*. Optionally set a password required to download the file. Choose *Cancel* to create a public with no password protection.

````
````{group-tab} Mountain Duck

Create an [download share](../protocols/dracoon.md#download-share) for a file or folder. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

````
`````

### [Microsoft OneDrive](../protocols/onedrive.md) & [Microsoft SharePoint](../protocols/sharepoint.md)

`````{tabs}
````{group-tab} Cyberduck

Create an [shared link](../protocols/onedrive.md) for a file or folder. Choose *File → Share…*.

````
````{group-tab} Mountain Duck

Create a [shared link](../protocols/onedrive.md) for a file or folder. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

````
`````

### [Dropbox](../protocols/dropbox.md)

`````{tabs}
````{group-tab} Cyberduck

You can share an [URL](../protocols/dropbox.md#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *File → Share…*.

```{image} _images/Passphrase_Prompt_Dropbox_Share.png
:alt: Passphrase Prompt Dropbox Share
:width: 400px
```

````
````{group-tab} Mountain Duck

You can share an [URL](../protocols/dropbox.md#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

```{image} _images/Passphrase_Prompt_Dropbox_Share.png
:alt: Passphrase Prompt Dropbox Share
:width: 400px
```

````
`````

### [Google Drive](../protocols/google_drive.md)

`````{tabs}
````{group-tab} Cyberduck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *File → Share…*.

````
````{group-tab} Mountain Duck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *Share…* from the [context menu](../mountainduck/interface.md#share).

```{image} _images/Share_File_Google_Drive_.png
:alt: Share File Google Drive
:width: 400px
```

````
`````

### [NextCloud and ownCloud](../protocols/webdav/nextcloud.md)

`````{tabs}
````{group-tab} Cyberduck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *File → Share…* for download shares or *File → Request files…* for upload shares.

````
````{group-tab} Mountain Duck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Choose *Cancel* to create a public share with no password protection. Choose *Share…* for download shares or *Request files…* for upload shares from the [context menu](../mountainduck/interface.md#share).

```{image} _images/Download_Share_Context_Menu.png
:alt: Download Share Context Menu
:width: 300px
```

````
`````

### [Box](../protocols/box.md)

`````{tabs}
````{group-tab} Cyberduck

Create download shares by choosing *File → Share…*. Optionally set a password required to download the file or folder. Choose *Cancel* to create a public URL without password protection. A Box account is not required to open the URL.

````
````{group-tab} Mountain Duck

Create download shares for files and folders by choosing *Share…* from the [context menu](../mountainduck/interface.md#share). Optionally set a password required to download the file or folder. Choose *Cancel* to create a public URL without password protection. A Box account is not required to open the URL.

```{image} _images/Download_Share_Box.png
:alt: Download Share Box
:width: 400px
```

````
`````

### [FTP](../protocols/ftp.md), [SFTP](../protocols/sftp.md) & [WebDAV](../protocols/webdav/index.md)

If you connect to a web root, refer to [HTTP URL](bookmarks.md#http-url) on how to configure your bookmark to allow copying a HTTP URL for a selected file. With a valid configuration, you can open the corresponding HTTP URL of a file selected with your default web browser or copy the URL to the clipboard. To manage permissions, refer to [UNIX Permissions (FTP/SFTP)](info.md#unix-permissions).
