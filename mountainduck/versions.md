File Versions
====

```{note}
Mountain Duck 4.12 or later required. Previously versions could be accessed from the [context menu](interface.md#context-menu-in-finder-and-windows-file-explorer) by right-clicking on a file in *Finder* on macOS or *File Explorer* on Windows and choosing *Versions*.
```

A list of file versions can be viewed within the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window. The files can also be reverted to a chosen version of the list.

## Supported Protocols

The versions feature within the *Info* window is supported for the following protocols:

| **Protocol** | **Revert previous version** | **Open/Quick Look previous version** | **Delete version** |
| --- | --- | --- | --- |
| **[S3](../protocols/s3/index.md)** | ✅ | ✅ | ✅ |
| **[Backblaze B2](../protocols/b2.md)** | ✅ | ✅ | ✅ |
| **[Google Drive](../protocols/googledrive.md)** | ❌ | ✅ | ✅ |
| **[Google Storage](../protocols/googlecloudstorage.md)** | ✅ | ✅ | ✅ |
| **[Microsoft OneDrive](../protocols/onedrive.md)** | ✅ | ✅ | ❌ |
| **[Microsoft Sharepoint](../protocols/sharepoint.md)** | ❌ | ✅ | ❌ |
| **[DRACOON](../protocols/dracoon.md)** | ✅ | ❌ | ✅ |
| **[Dropbox](../protocols/dropbox.md)** | ✅ | ✅ | ❌ |
| **[Nextcloud & ownCloud](../protocols/webdav/nextcloud.md)** | ✅ | ✅ | ❌ |

```{attention}
Using [S3](../protocols/s3/index.md) versions will only be displayed for buckets with versioning enabled. Versioning can be enabled per bucket in by choosing *Info → S3* in *Finder* on macOS or *File Explorer* on Windows. Alternatively, enable versioning in AWS Console or [Cyberduck](../cyberduck/index.md).
```

 ### Revert

You can revert to a previous version of a file by choosing *Versions → ... → Revert*. Wait for the *File Updated* notification which notifies the previous version has been restored.

```{image} _images/File_Updated_Notification_Windows.png
:alt: File Updated Notification (Windows)
:width: 400px
```

### Delete 
Permanently delete a previous version of the selected file.

### Preview 

This will open a *Quick Look preview* on macOS or open the previous version of the file in the default application on Windows.
