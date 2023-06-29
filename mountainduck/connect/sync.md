Smart Synchronization
====

```{toctree}
:hidden:
:titlesonly:
synchistory
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

Additional to the [general file states](index.md#status-of-files) available using the *Online* mode, there are some more while using the *Smart Synchronization* mode:

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

### ![](../_images/overlay_syncing.png) Sync in Progress
The file or directory is currently syncing with the server or cloud storage. Check the menu with the sync status for current download or upload progress.

## Context Menu Options

Refer to [Context Menu in Finder and Windows File Explorer](../interface.md#context-menu-in-finder-and-windows-file-explorer).

```{image} ../_images/Mountain_Duck_Screenshot_Finder_Dark.png
:alt: Mountain Duck Finder Dark
:width: 800px
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

| Action                                                                 | Error Cause                                                                                                                             | Error State (Overlay Icon)                   | Remarks                                                                                                                                                  |                                          Manual Conflict Resolution |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------:| 
| Indexing folder                                                        | Missing permission                                                                                                                      | Sync Error for files with<br/> pending write | Other files are removed from<br/> local cache                                                                                                            |                               Context menu with options<br/>*Retry* |				  							   				  				   						 
| Open placeholder (1) file                                              | Permission failure reading<br/>file on server                                                                                           | -                                            | Status remains *Online*                                                                                                                                  |                                                                   - |
| Select to keep file offline<br/>placeholder (1) file                   | Permission failure reading<br/>file on server                                                                                           | Sync Error                                   | -                                                                                                                                                        |                               Context menu with options<br/>*Retry* |
| Indexing folder containing<br/>files in write error state              | File with write sync error<br/>state not found on server                                                                                | Sync Error                                   | For error states caused by other Operations<br/>than `write`, the file is removed on local disk                                                          |                               Context menu with options<br/>*Retry* |
| Open placeholder (1) file                                              | Directory index is out of sync.<br/>File not found on server                                                                            | -                                            | File is deleted in local cache                                                                                                                           |                                                                   - |
| Edit file deleted on server                                            | Directory index is out of sync.<br/>File not found on server                                                                            | -                                            | File is uploaded anew to server                                                                                                                          |                                                                   - |
| Edit file renamed on server                                            | Directory index is out of sync.<br/>File not found on server                                                                            | -                                            | File is uploaded anew to server                                                                                                                          |                                                                   - |
| Edit file already changed<br/>on server                                | Last seen checksum differs from current<br/>checksum on server. (Or timestamp<br/>when server does not offer checksum<br/>verification) | -                                            | Existing file on server is renamed<br/> to `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead. |               User has to manually merge<br/>the conflicting edits. |
| Edit file with parent folder<br/>missing on server                     | Upload fails because parent folder<br/>is not found on server                                                                           | Sync Error                                   | -                                                                                                                                                        | Move file to different folder<br/>or *Retry* option in context menu |
| Move or rename *file* to target<br/>that already exists on server      | Directory index is out of sync                                                                                                          | -                                            | Existing file on server is renamed<br/>to `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead.  |               User has to manually merge<br/>the conflicting edits. |
| Move or rename *directory* to target<br/>that already exists on server | Directory index is out of sync                                                                                                          | -                                            | Existing directory on server is renamed<br/>to `<folder> timestamp.<extension>`                                                                          |               User has to manually merge the<br/>conflicting edits. |
| Move or rename *directory* that no<br/>longer exists on server         | Directory index is out of sync                                                                                                          | Sync Error                                   | Directory is removed from local cache                                                                                                                    |                                                                   - |
| Create file that exists already on server                              | Directory index is out of sync                                                                                                          | -                                            | Failure creating file is ignored                                                                                                                         |                                                                   - |
| Create folder that exists already on<br/>server                        | Directory index is out of sync                                                                                                          | -                                            | Failure creating folder is ignored                                                                                                                       |                                                                   - |
| Deleting file already changed on server                                | Directory index is out of sync                                                                                                          | -                                            | File is deleted on server                                                                                                                                |                                                                   - |

(1) Indexed file in local cache not downloaded from server

## Sync Progress

Changes to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{image} ../_images/Sync_in_Progress.gif
:alt: Sync in Progress
:width: 600px
```
Detailed status for current transfers is available in the *Sync* submenu. Refer to [Sync Progress](synchistory.md#sync-progress).

### Pause Sync

You can manually pause background syncing by selecting *Pause Sync* in the submenu for the sync status. Syncing is also paused automatically when your network connection to the server is interrupted but resumed automatically when a connection is restored.

```{warning}
When synchronization is paused by selecting _Pause Sync_ in the menu or caused by a connectivity problem, no changes from the server will be detected. Additionally, files marked as [Online Only](index.md#online-only) can't be opened: The application attempting to open the file will show an error message and a *Access Denied* notification is shown.
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

## File History

You can lookup the latest changes to files. Refer to [Recent Files](synchistory.md#recent-files)