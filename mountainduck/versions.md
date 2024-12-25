File Versions
====

:::{note}
Mountain Duck 4.12 or later required. Previously versions could be accessed from
the [context menu](interface.md#context-menu-in-finder-and-windows-file-explorer) by right-clicking on a file in
*Finder* on macOS or *File Explorer* on Windows and choosing *Versions*.
:::

A list of file versions can be viewed within the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window.
The files can also be reverted to a chosen version of the list.

## Supported Protocols

The versions feature within the *Info* window is supported for the following protocols:

| **Protocol**                                             | **Revert previous version** | **Open/Quick Look previous version** | **Delete version** |
|----------------------------------------------------------|-----------------------------|--------------------------------------|--------------------|
| [Nextcloud & ownCloud](../protocols/webdav/nextcloud.md) | ✅                           | ✅                                    | ❌                  |
|                                                          |
| [S3](../protocols/s3/index.md)                           | ✅                           | ✅                                    | ✅                  |
| [Google Storage](../protocols/googlecloudstorage.md)     | ✅                           | ✅                                    | ✅                  |
| [Backblaze B2](../protocols/b2.md)                       | ✅                           | ✅                                    | ✅                  |
|                                                          |
| [Microsoft OneDrive](../protocols/onedrive.md)           | ✅                           | ✅                                    | ❌                  |
| [Microsoft Sharepoint](../protocols/sharepoint.md)       | ❌                           | ✅                                    | ❌                  |
| [Google Drive](../protocols/googledrive.md)              | ❌                           | ✅                                    | ✅                  |
| [Dropbox](../protocols/dropbox.md)                       | ✅                           | ✅                                    | ❌                  |
|                                                          |
| [DRACOON](../protocols/dracoon.md)                       | ✅                           | ❌                                    | ✅                  |

:::{attention}
Using [S3](../protocols/s3/index.md) versions will only be displayed for buckets with versioning enabled. Versioning can
be enabled per bucket in by choosing *Info → S3* in *Finder* on macOS or *File Explorer* on Windows. Alternatively,
enable versioning in AWS Console or [Cyberduck](../cyberduck/index.md).
:::

### Revert

You can revert to a previous version of a file by choosing *Versions → ... → Revert*. Wait for the *File Updated*
notification which notifies the previous version has been restored.

:::{image} _images/File_Updated_Notification_Windows.png
:alt: File Updated Notification (Windows)
:width: 400px
:::

### Delete

Permanently delete a previous version of the selected file.

### Preview

This will open a *Quick Look preview* on macOS or open the previous version of the file in the default application on
Windows.

## Custom versioning

Enable the custom versioning option in *Preferences → Versions* to store previous versions of a file for protocols without native versioning. The versions can be previewed, deleted or restored in *Info → Versions*.

Select you preferred handling in case of sync conflicts with earlier changes. Choose between *Rename existing* and *Overwrite*.

```{image} _images/Preferences_Versions_macOS.png
:alt: Preferences Versions (macOS)
:width: 600px
```

Alternatively, use the corresponding option in the bookmark configuration to enable or disable versioning for specific connections only.

```{image} _images/Bookmark_Versioning_macOS.png
:alt: Bookmark Versioning
:width: 400px
```

The versions are stored in a hidden folder named `.duckversions` in each folder on the mount. The versions are named like the following pattern: `filename.extension → filename-20230906102017.762.extension`

### Exclude files

Versioning can be limited to files matching a regular expression using the [hidden configuration option](preferences.md#hidden-configuration-options).

    versioning.include.regex=.*

### Number of saved versions

Per default, the number of saved versions is limited to 5. The oldest version will be deleted once a new version is uploaded exceeding the limit.

The number of saved versions can be customized by using a [hidden configuration option](preferences.md#hidden-configuration-options).

    versioning.limit=5