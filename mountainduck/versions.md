File Versions
====

`````{tabs}
````{tab} Version 4.11 and earlier
Mountain Duck supports opening and reverting previous versions of files. You can get a list of previous versions by right-clicking on a file in *Finder* on macOS or *File Explorer* on Windows and choosing *Versions*.

**Supported Providers**

Support is currently limited to connections to [Amazon S3](../protocols/s3/index.md) with buckets that have versioning enabled.

**Amazon S3**

**Enable Versioning**

Versioning can be enabled per bucket in by choosing *Info → S3* in *Finder* on macOS or *File Explorer* on Windows. Alternatively, enable versioning in AWS Console or [Cyberduck](../cyberduck/index.md).

**Quick Look**

You can open a previous version of a file by choosing *Versions → ... → Quick Look*. This will open a *Quick Look preview* on macOS or open the previous version of the file in the defailt application on Windows.

```{image} _images/Revert_File_Context_Menu_Option_Windows.png
:alt: Revert File Context Menu Option (Windows)
:width: 900px
```

**Revert**

You can revert to a previous version of a file by choosing *Versions → ... → Revert*. Wait for the *File Updated* notification which notifies the previous version has been restored.

```{image} _images/File_Updated_Notification_Windows.png
:alt: File Updated Notification (Windows)
:width: 400px
```

````
````{tab} Version 4.12 and later

The *Versions* option within the contect menu is not available anymore. A list of file versions can be viewed within the *Versions* tab of the *Info* window. The files can also be reverted to a choosen version of the list.

**Supported Providers**

The versions feature within the *Info* window is supported for the following protocols:

| **Protocol** | **Revert previous version** | **Open/Quick Look previous version** | **Delete version** |
| --- | --- | --- | --- |
| **[S3](../protocols/s3/index.md)** | ✅ | ✅ | ✅ |
| **[Backblaze B2](../protocols/b2.md)** | ✅ | ✅ | ✅ |
| **[Google Drive](../protocols/google_drive.md)** | ❌ | ✅ | ✅ |
| **[Google Storage](../protocols/google_cloud_storage.md)** | ✅ | ✅ | ✅ |
| **[Microsoft OneDrive](../protocols/onedrive.md)** | ✅ | ✅ | ❌ |
| **[Microsoft Sharepoint](../protocols/sharepoint.md)** | ❌ | ✅ | ❌ |
| **[DRACOON](../protocols/dracoon.md)** | ✅ | ❌ | ✅ |
| **[Dropbox](../protocols/dropbox.md)** | ✅ | ✅ | ❌ |

```{note}
Using [S3](../protocols/s3/index.md) or [Backblaze B2](../protocols/b2.md), versions will only be displayed if bucket versioning is enabled.
```

**Enable Versioning**

**Amazon S3**

Versioning can be enabled per bucket in by choosing *Info → S3* in *Finder* on macOS or *File Explorer* on Windows. Alternatively, enable versioning in AWS Console or [Cyberduck](../cyberduck/index.md).

**Backblaze B2**

`Bucket versioning` is enabled per default. It can be verified within the *B2* panel of the *Info* window.

````
`````