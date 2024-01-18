Connect mode
===

```{toctree}
:hidden:
:titlesonly:
sync
online
```

When connecting to a server, you can choose between *[Online](online.md)* and *[Smart Synchronization](sync.md)* connect
mode.

```{admonition} Online
In _Online_ connect mode, changes to a file are immediately uploaded and in sync when an application has finished saving a file.
```

```{admonition} Smart Synchronization
In _Smart Synchronization_ connect mode, files are copied to a local cache for faster access prior synchronization with the server in the background.
```

## Feature Comparison

|                                          | **Online**                                                            | **Smart Synchronization**                                                     |
|------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Offline Access**                       | –                                                                     | Save files in cache on disk for access with no server connectivity            |
| **Index Files**                          | –                                                                     | Index folder contents in cache on disk for access with no server connectivity |
| **Buffer file contents**                 | ︎Temporarily save opened files for faster access later                | Temporarily save opened files to copy to cache on disk                        |
| **Synchronization**                      | Changes are immediately uploaded                                      | Synchronize changes in the background                                         |
| **Transfer Progress**                    | Upload shown in progress window in _Finder.app_ or _Windows Explorer_ | Uploads shown in the status bar (macOS) or taskbar (Windows)                  |
| **[Recent Files](sync.md#recent-files)** | –                                                                     | Available in the status bar (macOS) or taskbar (Windows)                      |
| **[Lock Files](../locking.md)**          | ✔︎                                                                    | ✔                                                                             |
| **[Share Files](../share.md)**           | ✔                                                                     | ✔                                                                             |

## Quota support
Mountain Duck has support for the overall quota of a server but quota reporting is not supported for all protocols.

| Protocol                 | Support |
|--------------------------| :---: |
| Local Disk               | ✅ |
| SFTP                     | ✅ |
| FTP                      | ❌ |
| WebDAV			       | ✅ |
| Google Drive             | ✅ |
| Google Cloud Storage     | ❌ |
| Microsoft OneDrive       | ✅ |
| Microsoft Sharepoint     | ✅ |
| Files.com                | ❌ |
| DRACOON                  | ✅ |
| Backblaze B2             | ❌ |
| Box.com                  | ❌ |
| Dropbox                  | ✅ |
| Nextcloud                | ✅ |
| ownCloud                 | ✅ |
| S3                       | ❌ |
| SMB                      | ✅ |
| Windows Azure            | ❌ |
| OpenStack Object Storage | ✅ |

```{admonition} Limited Support
:class: attention
- **[Microsoft OneDrive](../../protocols/onedrive.md#quota)**: Quota is only supported if a folder other than the virtual root is mounted.
- **[Microsoft SharePoint](../../protocols/sharepoint.md#quota)**: Quota is only supported for the *Drives* folders within the respective SharePoint site folders.
```

Mountain Duck can't display the correct remaining free space for protocols that can't report quota. Finder and Windows Explorer will show exabyte values within the *Online* mode and the available space within the synchronization cache location within the *Smart Synchronization* mode for servers and protocols that don't have support for quota reporting.