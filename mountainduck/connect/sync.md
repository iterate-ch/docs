Smart Synchronization
====

```{toctree}
:hidden:
:titlesonly:
```

```{image} ../_images/Disk_Syncing.png
:alt: Disk Syncing
:width: 200px
```
> In _Smart Synchronization_ connect mode, files are copied to a local cache for faster access prior synchronization with the server in the background. Directories can be browsed when offline and files opened are made available for later offline access. You can also choose to make explicitly all or only selected files and folders available for offline use. Changes to files are saved in a local cache first and uploaded in the background as soon as a connection is available.

```{tip}
You can access volumes in _Smart Synchronization_ connect mode without being always connected the server or cloud storage.
```

```{contents} Content
:depth: 1
:local:
```

## Status of Files

Files and folders on a mounted volume have a status icon overlay in _File Explorer_ (Windows) and _Finder_ (macOS).

```{admonition} macOS only
:class: tip
Please make sure to enable the Mountain Duck [Integration](../installation/index.md) in *System Preferences → Extensions → Finder* on macOS. For macOS Ventura and later, the setting can be found in *System Settings → Privacy & Security → Extensions → Added Extensions*.
```

### ![](../_images/overlay_uptodate.png) Up to Date
The file or the contents of a directory has been opened and downloaded to your computer and therefore currently synced with the server or cloud storage. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will appear as *Online Only* and are not downloaded automatically. Files copied to a volume are kept cached by default.

```{note}
Files can be purged automatically from the cache when not accessed or the cache size limit is exceeded. Refer to [Cache Limitations](../preferences.md#cache-limitations).
```

### ![](../_images/overlay_infinite.png) Online Only
The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

### ![](../_images/overlay_sync.png) In Sync
The file or folder is selected to be synced with the server or cloud storage to always keep offline. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will be downloaded automatically.

```{tip}
Files explicitly selected to keep offline are **not** automatically purged. Refer to [Cache Limitations](../preferences.md#cache-limitations).
```

### ![](../_images/overlay_syncing.png) Sync in Progress
The file or folder is currently syncing with the server or cloud storage. Check the menu with the sync status for current download or upload progress.

### ![](../_images/overlay_error.png) Sync Error
Files that failed to sync after changes. You are missing permission to write to the file or another problem occurred. Please contact your web hosting service provider for assistance. To resolve the error, move the file to your local disk, and reload the directory. Refer to [Sync Conflicts](sync.md#sync-conflicts) for possible error scenarios. You can try to repeat the failed transfer by selecting *Mountain Duck → Retry* in the [context menu](sync.md#context-menu-options). If a sync error cannot be solved using *Mountain Duck → Retry* because the server does not allow the operation (i.e. due to a permission issue), you can resolve the error state on the file or folder by

- Move the file or folder to another location on the volume
- Delete the file or folder
- To upload files to a target directory no longer existing on the server, you have to move the files to a location found on the server.

### ![](../_images/overlay-pause.png) Sync Paused
The file or folder is pending syncing with the server but synchronization has been [paused](#pause-sync).

### ![](../_images/overlay_ignored.png) Ignored
The file or folder is only saved in local cache and not synced. New _Folders_, empty files and files matching [excluded filename patterns](../issues/index.md#filenames) are not uploaded. Folders are uploaded after being renamed.

## Notifications


```{image} ../_images/File_Updated_Notification.png
:alt: File Updated Notification
:width: 500px
```
Notifications can be posted for the following events:
- **Filesystem mounted**. The volume is now connected.
- **Filesystem unmounted**. The volume has been disconnected.
- **Pause Sync**. Synchronization has paused due to the server not reachable because of a network or login error.
- **Resume Sync**. Synchronization has automatically resumed as after reachability change.
- **File Added:** New file found on server for previously indexed folder.
- **File Deleted**. File has been deleted on the server previously synced.
- **File Updated:** File changed on server since previously indexing a folder
- **File Uncached**. File previously cached for offline access has been purged.
- **Download complete**. File download completed in the background.
- **Upload complete**. File upload completed in the background.
- **Sync Error**. Error synchronizing file because of a server error response.
- **Sync Conflict:** Conflicting change in file lead to duplicate of file being created with previous content edited on server.

You can adjust which notifications you want to receive in [*Preferences → Notifications*](../preferences.md#notifications).

## Context Menu Options

To reach the context menu right-click on a file or folder in _File Explorer_ (Windows) or _Finder_ (macOS). Refer to [Finder Extension & Windows File Explorer Extension](../interface.md#context-menu-in-finder-and-windows-file-explorer).

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
As long as the volume is mounted, files marked _Up to Date_ or _In Sync_ with a green checkmark remain accessible even if the network connection drops. Changes are synchronized in the background when the server is reachable again. 
```

### Delete on Local Disk

Choose *Mountain Duck → Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk.

```{note}
Files will get cached again regardless this setting if accessed again later (e.g. Finder and Windows Explorer thumbnail preview and media file metadata retrieval).
```

<video width="800" height="450" controls>
	<source src="../../../_static/videos/mountainduck/keepoffline.mp4" type="video/mp4" />
</video>

<br>
<br>

### Retry

Choose _Mountain Duck → Retry_ to retry a sync operation failed previously with an error.

## Cache Size

The cache size can be limited per bookmark within the *Preferences → Sync* tab. Also files not accessed within a chosen period of time can be purged. Refer to [Cache Limitations](../preferences.md#cache-limitations). The cache contains obfuscated file contents on local disk to make files available when offline.


## Transfer progress

While transferring files and folders, a transfer [progress](../interface.md#copying-files) window shows in _Finder.app_ or _Windows Explorer_. When completed, the file(s) are queued for synchronization with the server.

## Sync Progress

Changes to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{image} ../_images/Icon_Sync_in_Progress.gif
:alt: Sync in Progress
:width: 600px
```
Detailed status for current transfers is available in the *Sync* submenu. The sync progress shows the files that currently get synchronized and pending changes after the current transfer.

```{image} ../_images/Menu_Sync_in_Progress.png
:alt: Sync Progress
:width: 800px
```

Shown for the current transfers are transfer rate, remaining data, and already transferred data. If Mountain Duck synchronizes files in a badge, the file state might differ from the state within the file browser. The sync progress display is limited to 5 entries.


### Pause Sync
You can manually pause background syncing by selecting *Pause Sync* in the submenu for the sync status. The paused sync status is indicated with a greyed-out icon in the tray (Windows) or status bar (macOS).

```{image} ../_images/Sync_Paused_macOS.png
:alt: Sync Paused (macOS)
:width: 500px
```
Syncing is also paused automatically when your network connection to the server is interrupted but resumed automatically when a connection is restored.

```{warning}
When synchronization is paused by selecting _Pause Sync_ in the menu or caused by a connectivity problem, no changes from the server will be detected. Additionally, files marked as [Online Only](#online-only) cannot be opened: The application attempting to open the file will show an error message and a *Access Denied* notification is shown.
```

### Cancel upload in progress
To abort the upload of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Delete the file
3. *Resume Synchronization* in the dropdown menu.

### Cancel download in progress
To abort the download of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Select *Delete on local Disk* within the Mountain Duck [context menu](../interface.md#context-menu-in-finder-and-windows-file-explorer).
3. *Resume Synchronization* in the dropdown menu.

## Recent Files
The *Recent Files* area shows the last 20 changes to files by you or on the server:
```{image} ../_images/Recent_Files.png
:alt: Recent Files
:width: 600px
```

#### ![Delete](../_images/delete.png) Delete
A file or folder has been deleted either *by you* or *on the server*

#### ![Create](../_images/plus.png) Create
A file or folder was created or updated *on the server*.

#### ![Upload](../_images/transfer_upload.png) Upload
A file or folder was added or changed *by you* and uploaded to the server.

#### ![Download](../_images/transfer_download.png) Download
A file is downloaded to the local cache to be available for offline use. This state also occurs if a file that is marked as *Keep offline* has updated on the server.

#### ![Error](../_images/alert.png) Error
The sync operation failed for the file. A file may show up with an error state indicating an issue while synchronizing. Further details are available through the [sync option menu item](../interface.md#context-menu-in-finder-and-windows-file-explorer).

### Application Display

```{admonition} Windows Only
:class: tip

The application that was used for editing the file is displayed within the *Recent Files* area.
```
### Reveal file
Selecting an item in the *Recent Files* section reveals the file in the _Finder_ (macOS) of _File Explorer_ (Windows).

### Clear Menu
Clear out all entries of the list by clicking on the *Clear Menu* button at the bottom of the menu.


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
