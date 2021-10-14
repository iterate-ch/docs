Share Files
===

Many storage providers have an option to share a file with a third party without access to your account with a publicly accessible link. Depending on the provider, the link may be auto expiring and no longer valid after a given period or a password can be set required to download the file.

# Availability of Upload and Download Shares

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

# Providers with support to share a file using a public, password protected or temporary URL

## [S3](../Protocols/S3/index)

`````{tabs}
````{group-tab} Cyberduck

Create a [pre-signed temporary](../Protocols/S3/index#pre-signed-temporary-urls) URL. Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [pre-signed temporary](../Protocols/S3/index#pre-signed-temporary-urls) URL. Choose *Copy URL* from the [context menu](../Mountain_Duck/interface#share).

```{image} _images/S3_Pre-Signed_URL.png
:alt: Send Command
:width: 400px
```

````
`````

## [OpenStack Swift](../Protocols/OpenStack/index)

`````{tabs}
````{group-tab} Cyberduck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../Protocols/OpenStack/index#temporary-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

A private object stored in OpenStack Swift can be made publicly available for a limited time using a [signed URL](../Protocols/OpenStack/index#temporary-urls). Choose *Copy URL* from the [context menu](../Mountain_Duck/interface#share).

````
`````

## [Azure](../Protocols/Azure)

`````{tabs}
````{group-tab} Cyberduck

Create a [Shared Access Signature URL](../Protocols/Azure#share-access-signature-urls). Choose *Edit → Copy URL → Signed URL*.

````
````{group-tab} Mountain Duck

Create a [Shared Access Signature URL](../Protocols/Azure#shared-access-signature-urls). Choose *Copy URL* from the [context menu](../Mountain_Duck/interface#share).

````
`````

## [Backblaze B2](../Protocols/B2)

`````{tabs}
````{group-tab} Cyberduck

Create an [authorized URL](../Protocols/B2#authorized-url) to make files available publicly expiring after 7 days. Choose *File → Share...*.

````
````{group-tab} Mountain Duck

Create an [authorized URL](../Protocols/B2#authorized-url) to make files available publicly expiring after 7 days. Choose *Create Download Share* from the [context menu](../Mountain_Duck/interface#share).

```{image} _images/B2_Authorized_URL.png
:alt: Send Command
:width: 600px
```

````
`````

## [DRACOON](../Protocols/Dracoon)

`````{tabs}
````{group-tab} Cyberduck

Create an [download share](../Protocols/Dracoon#download-share) for a file or folder. Choose *File → Share...*. Optionally set a password required to download the file. Choose *Cancel* to create a public with no password protection.

````
````{group-tab} Mountain Duck

Create an [download share](../Protocols/Dracoon#download-share) for a file or folder. Choose *Create Download Share* from the [context menu](../Mountain_Duck/interface#share).

````
`````

## [Microsoft OneDrive](../Protocols/OneDrive) & [Microsoft SharePoint](../Protocols/SharePoint)

`````{tabs}
````{group-tab} Cyberduck

Create an [shared link](../Protocols/OneDrive#shared-link) for a file or folder. Choose *File → Share...*.

````
````{group-tab} Mountain Duck

Create a [shared link](../Protocols/OneDrive#shared-link) for a file or folder. Choose *Create Download Share* from the [context menu](../Mountain_Duck/interface#share).

````
`````

## [Dropbox](../Protocols/Dropbox)

`````{tabs}
````{group-tab} Cyberduck

You can share an [URL](../Protocols/Dropbox#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *Edit → Copy URL → Signed URL*.

```{image} _images/Passphrase_Prompt_Dropbox_Share.png
:alt: Send Command
:width: 400px
```

````
````{group-tab} Mountain Duck

You can share an [URL](../Protocols/Dropbox#share) to provide access to a document in your Dropbox. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *Copy URL* from the [context menu](../Mountain_Duck/interface#share).

```{image} _images/Passphrase_Prompt_Dropbox_Share.png
:alt: Send Command
:width: 400px
```

````
`````

## [Google Drive](../Protocols/Google_Drive)

`````{tabs}
````{group-tab} Cyberduck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *File → Share...*.

````
````{group-tab} Mountain Duck

Share the web link to open download or open the file in Google Docs. This will set the permission of the file to `reader/anyone`. Choose *Create Download Share* from the [context menu](../Mountain_Duck/interface#share).

```{image} _images/Share_File_Google_Drive_.png
:alt: Send Command
:width: 400px
```

````
`````

## [NextCloud & ownCloud](../Protocols/WebDAV/Nextcloud)

`````{tabs}
````{group-tab} Cyberduck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Choose *Cancel* to create a public URL with no password protection. Choose *File → Share...*.

````
````{group-tab} Mountain Duck

Create public shares for people who are not Nextcloud users. Optionally set a password required to download the file. Choose *Cancel* to create a public with no password protection. Choose *Create Download Share* from the [context menu](../Mountain_Duck/interface#share).

```{image} _images/Download_Share_Context_Menu.png
:alt: Send Command
:width: 300px
```

````
`````

## [FTP](../Protocols/FTP), [SFTP](../Protocols/SFTP) & [WebDAV](../Protocols/WebDAV/index)

If you connect to a web root, refer to [HTTP URL](Bookmarks#http-url) on how to configure your bookmark to allow copying a HTTP URL for a selected file. With a valid configuration, you can open the corresponding HTTP URL of a file selected with your default web browser or copy the URL to the clipboard. To manage permissions, refer to [UNIX Permissions (FTP/SFTP)](Info#unix-permissions-ftp-sftp).