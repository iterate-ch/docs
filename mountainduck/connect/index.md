Connect mode
===

:::{toctree}
:hidden:
:titlesonly:
integrated
sync
online
:::

When connecting to a server, you can choose between *[Online](online.md)*, *[Smart Synchronization](sync.md)*, and
*[Integrated](integrated.md)* connect
mode:

:::::{tabs}
::::{tab} Integrated

The [_Integrated_ connect mode](integrated.md) synchronizes files and folders from a directory on the local disk with
support from macOS and Windows.

```{admonition} Version 5
:class: note
Mountain Duck 5 required.
```

::::
::::{tab} Online

Using [_Online_ connect mode](online.md), changes to a file are immediately uploaded and in sync when an application has
finished saving a file.

:::{admonition} Windows only
:class: tip

You may be prompted for additional driver [installation](../installation/index.md#optional-driver-installation) on
Windows.
:::

::::
::::{tab} Smart Synchronization

In [_Smart Synchronization_ connect mode](sync.md), files are copied to a local cache for faster access prior
synchronization with the server in the background.

:::{admonition} Windows only
:class: tip

You may be prompted for additional driver [installation](../installation/index.md#optional-driver-installation) on
Windows.
:::

::::
:::::

## Feature Comparison

|                                          | **Online**                                             | **Smart Synchronization**                                                       | **Integrated**                                                                                         |
|------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Network Volume**                       | ✔                                                      | ✔                                                                               | –                                                                                                      |
| **Custom Cache Location**                | –                                                      | ✔                                                                               | –                                                                                                      |
| **Offline Access**                       | –                                                      | ✔ Save files in cache on disk for access with no server connectivity            | ✔                                                                                                      |
| **Index Files**                          | –                                                      | ✔ Index folder contents in cache on disk for access with no server connectivity | ✔                                                                                                      |
| **Buffer file contents**                 | ︎Temporarily save opened files for faster access later | Temporarily save opened files to copy to cache on disk                          | –                                                                                                      |
| **Synchronization**                      | Changes are immediately uploaded                       | ✔ Synchronize changes in the background                                         | ✔                                                                                                      |
| **Transfer Progress**                    | Progress window in _Finder.app_ or _Windows Explorer_  | Progress in the status bar (macOS) or taskbar (Windows)                         | Progress in the status bar (macOS) or taskbar (Windows) and progress icon in Finder & Windows Explorer |
| **[Recent Files](sync.md#recent-files)** | –                                                      | ✔ Available in the status bar (macOS) or taskbar (Windows)                      | ✔                                                                                                      |
| **[Lock Files](../locking.md)**          | ✔︎                                                     | ✔                                                                               | –                                                                                                      |
| **[Share Files](../share.md)**           | ✔                                                      | ✔                                                                               | ✔                                                                                                      |

## Quota Support

Mountain Duck displays the overall quota present on the server as available disk space on the mounted volume.

| Protocol                                                                  | Support |
|---------------------------------------------------------------------------|:-------:|
| [Local Disk](../../protocols/index.md#local-disk)                         |    ✅    |
| [SFTP](../../protocols/sftp/index.md#free-space-calculation-is-incorrect) |    ✅    |
| [FTP](../../protocols/ftp.md)                                             |    ❌    |
| [WebDAV](../../protocols/webdav/index.md)			                              |    ✅    |
| [Google Drive](../../protocols/googledrive.md)                            |    ✅    |
| [Google Cloud Storage](../../protocols/googlecloudstorage.md)             |    ❌    |
| [Microsoft OneDrive](../../protocols/onedrive.md#quota)                   |    ✅    |
| [Microsoft Sharepoint](../../protocols/sharepoint.md#quota)               |    ✅    |
| [Files.com](../../protocols/files.com.md)                                 |    ❌    |
| [DRACOON](../../protocols/dracoon.md)                                     |    ✅    |
| [Backblaze B2](../../protocols/b2.md)                                     |    ❌    |
| [Box.com](../../protocols/box.md)                                         |    ❌    |
| [Dropbox](../../protocols/dropbox.md)                                     |    ✅    |
| [Nextcloud](../../protocols/webdav/nextcloud.md)                          |    ✅    |
| [ownCloud](../../protocols/webdav/nextcloud.md)                           |    ✅    |
| [S3](../../protocols/s3/index.md)                                         |    ❌    |
| [SMB](../../protocols/smb.md)                                             |    ✅    |
| [Windows Azure ](../../protocols/azure.md)                                |    ❌    |
| [OpenStack Object Storage](../../protocols/openstack/index.md)            |    ✅    |

:::{admonition} Limited Support
:class: attention

- **[Microsoft OneDrive](../../protocols/onedrive.md#quota)**: Quota is only supported when setting the *Path* in the
  bookmark configuration to a folder different from `/`.
- **[Microsoft SharePoint](../../protocols/sharepoint.md#quota)**: Quota is only supported when setting the *Path* in
  the bookmark configuration to a *Drives* folder in a SharePoint site folder.
  :::

Some protocols do not report the available quota. Finder and Windows Explorer will show exabyte values in *Online*
connect mode and the available space within the synchronization cache location on your local disk in *Smart
Synchronization* connect mode for the affected protocols.

:::{note}
Quota support can be [disabled](../../protocols/sftp/index.md#free-space-calculation-is-incorrect) for all protocols.
:::