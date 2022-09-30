Smart Synchronization
====

```{toctree}
:hidden:
:titlesonly:


history
```

```{image} ../_images/Disk_Syncing.png
:alt: Disk Syncing
:width: 200px
```

The smart synchronization [connect mode](../interface.md#connect-mode) allows working with files when offline. You can also choose to make explicitly all or only selected files and folders available for offline use. Changes to files are saved in a local cache first and uploaded in the background as soon as a connection is available.

```{contents} Content
:depth: 2
:local:
```

## Status of Files

Files and folders on a mounted volume have a status icon overlay in File Explorer (Windows) and Finder (macOS).

```{note}
Please make sure to enable the Mountain Duck [Integration](../installation/index.md) in *System Preferences → Extensions → Finder* on macOS.
```

### ![](../_images/overlay_uptodate.png) Up to Date
The file or the contents of a directory has been opened and downloaded to your computer and therefore currently synced with the server or cloud storage. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will appear as *Online Only* and are not downloaded automatically. Files copied to a volume are kept cached by default.

```{note}
Files can be purged automatically from the cache when not accessed or the cache size limit is exceeded. Refer to [Cache Limitations](../preferences.md#cache-limitations).
```

### ![](../_images/overlay_sync.png) In Sync
The file or directory is selected to be synced with the server or cloud storage to always keep offline. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will be downloaded automatically.

```{tip}
Files explicitly selected to keep offline are **not** automatically purged. Refer to [Cache Limitations](../preferences.md#cache-limitations).
```

### ![](../_images/overlay_infinite.png) Online Only
The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

### ![](../_images/overlay_syncing.png) Sync in Progress
The file or directory is currently syncing with the server or cloud storage. Check the menu with the sync status for current download or upload progress.

### ![](../_images/overlay_error.png) Sync Error
There was an error updating the file after changes. You are missing permission to write to the file or another problem occured. Please contact your web hosting service provider for assistance. To resolve the error, move the file to your local disk, and reload the directory or use the _Retry_ option within the context menu. Refer to [Sync Conflicts](#sync-conflicts) for possible error scenarios.

### ![](../_images/overlay_ignored.png) Ignored
The file is only saved in a local temporary location and never synced to the server or cloud storage.

```{tip}
Rename a file to synchronize with the server.
```

## Context Menu Options
```{image} ../_images/Mountain_Duck_Screenshot_Finder_Dark.png
:alt: Mountain Duck Finder Dark
:width: 800px
```

```{admonition} macOS only
:class: tip

Please make sure to enable the Mountain Duck [Integration](../interface.md#context-menu-in-finder-and-windows-file-explorer) in *System Preferences → Extensions → Finder Extensions*.
```

### Keep Offline

Choose *Mountain Duck → Keep Offline on Local Disk* to make files and folders available offline. The status of the file will change to *In Sync*. The action is recursive for all contained files when a folder is selected and applies to new files found on the remote storage.

```{image} ../_images/Sync_Context_Menu_macOS.png
:alt: Sync Context Menu (macOS)
:width: 500px
```

```{note}
As long as the volume is mounted, files marked _Up to Date_ or _In Sync_ with a green checkmark remain accessible even if the network connection drops. Changes are synchronized in the background when the server is reachable again. This is made possible by caching file contents in an obfuscated cache on a local disk, which is unavailable for direct use.
```

To reach the context menu right-click on a file or folder in File Explorer (Windows) or Finder (macOS). Refer to [Finder Extension & Windows File Explorer Extension](../interface.md#context-menu-in-finder-and-windows-file-explorer).

### Delete on Local Disk

Choose *Mountain Duck → Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk.

```{note}
Files will get cached again regardless this setting if accessed again later (e.g. Finder and Windows Explorer thumbnail preview and media file metadata retrieval).
```

<video width="800" height="450" controls>
	<source src="../_static/videos/mountainduck/keepoffline.mp4" type="video/mp4" />
</video>

<br>
<br>

## Cache Size

The cache size can be limited per bookmark within the *Preferences → Sync* tab. Also files not accessed within a chosen period of time can be purged. Refer to [Cache Limitations](../preferences.md#cache-limitations).

## Sync Conflicts

A conflict may be caused by two or more users editing the same files at the same time or while on the road before the files are synced. We do not merge changes to files like version control systems do. The file with conflicting edits will be renamed with the current time added to the filename. You will have to compare the changes manually and delete the duplicate file afterwards.

| Action | Error Cause | Error State (Overlay Icon) | Remarks | Manual Conflict Resolution |
| --- | --- | --- | --- | ---: | 
| Indexing folder | Missing permission | Sync Error for files with<br/> pending write | Other files are removed from<br/> local cache | Context menu with options<br/>*Retry* |				  							   				  				   						 
| Open placeholder (1) file | Permission failure reading<br/>file on server | - | Status remains *Online* | - |
| Select to keep file offline<br/>placeholder (1) file | Permission failure reading<br/>file on server | Sync Error | - | Context menu with options<br/>*Retry* |
| Indexing folder containing<br/>files in write error state | File with write sync error<br/>state not found on server | Sync Error | For error states caused by other Operations<br/>than `write`, the file is removed on local disk | Context menu with options<br/>*Retry* |
| Open placeholder (1) file | Directory index is out of sync.<br/>File not found on server | - | File is deleted in local cache | - |
| Edit file deleted on server | Directory index is out of sync.<br/>File not found on server | - | File is uploaded anew to server | - |
| Edit file renamed on server | Directory index is out of sync.<br/>File not found on server | - | File is uploaded anew to server | - |
| Edit file already changed<br/>on server | Last seen checksum differs from current<br/>checksum on server. (Or timestamp<br/>when server does not offer checksum<br/>verification) | - | Existing file on server is renamed<br/> to `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead. | User has to manually merge<br/>the conflicting edits. |
| Edit file with parent folder<br/>missing on server | Upload fails because parent folder<br/>is not found on server | Sync Error | - | Move file to different folder<br/>or *Retry* option in context menu |
| Move or rename *file* to target<br/>that already exists on server | Directory index is out of sync | - | Existing file on server is renamed<br/>to `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead. | User has to manually merge<br/>the conflicting edits. |
| Move or rename *directory* to target<br/>that already exists on server | Directory index is out of sync | - | Existing directory on server is renamed<br/>to `<folder> timestamp.<extension>` | User has to manually merge the<br/>conflicting edits. |
| Move or rename *directory* that no<br/>longer exists on server | Directory index is out of sync | Sync Error | Directory is removed from local cache | - |
| Create file that exists already on server | Directory index is out of sync | - | Failure creating file is ignored | - |
| Create folder that exists already on<br/>server | Directory index is out of sync | - | Failure creating folder is ignored | -  
| Deleting file already changed on server | Directory index is out of sync | - | File is deleted on server | - |

(1) Indexed file in local cache not downloaded from server

## Sync Progress

Changes to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{image} ../_images/Sync_in_Progress.gif
:alt: Sync in Progress
:width: 600px
```
Detailed status for current transfers is available in the *Sync* submenu. Refer to [Sync Progress](../sync/history.md#sync-progress).

### Pause Sync

You can manually pause background syncing by selecting *Pause Sync* in the submenu for the sync status. Syncing is also paused automatically when your network connection to the server is interrupted but resumed automatically when a connection is restored.

```{warning}
When synchronization is paused by selecting _Pause Sync_ in the menu or caused by a connectivity problem, no changes from the server will be detected.
```

The paused sync status is indicated with a greyed-out icon in the tray (Windows) or status bar (macOS).

```{image} ../_images/Sync_Paused_macOS.png
:alt: Sync Paused (macOS)
:width: 500px
```

### Cancel upload in progress
To abort the upload of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Delete the file
3. *Resume Synchronization* in the dropdown menu.

You can use the steps as well to cancel *Keep Offline* processes.

### Cancel download in progress
To abort the download of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Select *Delete on local Disk* within the Mountain Duck [context menu](../interface.md#context-menu-in-finder-and-windows-file-explorer).
3. *Resume Synchronization* in the dropdown menu.

## Sync Errors

Files that failed to sync get a sync error badge. You can try to repeat the failed transfer by selecting *Mountain Duck → Retry* in the context menu.

### Resolve Errors

If a sync error cannot be solved using *Mountain Duck → Retry* because the server does not allow the operation (i.e. due to a permission issue), you can resolve the error state on the file or folder by

- Move the file or folder to another location on the volume
- Delete the file or folder 

To upload files to a target directory no longer existing on the server, you have to move the files to a location found on the server.

## File History

You can lookup the latest changes to files. Refer to [Recent Files](history.md#recent-files)

### Notifications

```{image} ../_images/File_Updated_Notification.png
:alt: File Updated Notification
:width: 500px
```

- **File Added:** New file found on server for previously indexed folder.
- **File Updated:** File changed on server since previously indexing a folder
- **Sync Conflict:** Conflicting change in file lead to duplicate of file being created with previous content edited on server.

You can adjust which notifications you want to receive within [*Preferences → Notifications*](../preferences.md#notifications).

## Preferences

Refer to [Preferences](../preferences.md).
