Integrated
====

```{toctree}
:hidden:
:titlesonly:
```

```{image} ../_images/Disk_Syncing.png
:alt: Disk Syncing
:width: 200px
```

> Local storage is managed by the operating system. The mount is not seen as a remote volume by applications but as a regular folder on disk. This option uses the tightly integrated _File Provider_ (macOS) and _Cloud Files_ (Windows) APIs. Directories can be browsed when offline and files opened are made available for later offline access. You can choose to make selected files and folders available for offline use. Changes to files are uploaded in the background as soon as a connection is available.

```{tip}
You can access files in _Integrated_ connect mode without being always connected the server or cloud storage.
```


## Status of Files

Files and folders on a mounted volume have a status icon overlay in _File Explorer_ (Windows) and _Finder_ (macOS).

### ![](../_images/overlay_uptodate.png) Up to Date
The file or the contents of a directory has been opened and downloaded to your computer and therefore currently synced with the server or cloud storage. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will appear as *Online Only* and are not downloaded automatically. Files copied to a volume are kept cached by default.

```{note}
Files can be purged automatically from the cache when not accessed or the cache size limit is exceeded. Refer to [Cache Limitations](../preferences.md#cache-limitations).
```

### ![](../_images/overlay_infinite.png) Online Only
The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

:::{admonition} macOS only
:class: note
```{image} ../_images/File_Provider_Online_Only.png
:alt: File Provider Icon
:width: 24px
:align: left
```
Click this additional icon displayed next to the filename in Finder.app to request the download of the file.
:::

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

:::{admonition} macOS only
:class: note
```{image} ../_images/File_Provider_Ignored.png
:alt: File Provider Icon
:width: 24px
:align: left
```
This additional icon displayed next to the filename in Finder.app indicates the file is not synced.
:::

### ![](../_images/overlay-pause.png) Sync Paused
The file or folder is pending syncing with the server but synchronization has been [paused](sync.md#pause-sync).

### ![](../_images/overlay_ignored.png) Ignored
The file or folder is only saved in local cache and not synced. New _Folders_, empty files and files matching [excluded filename patterns](../issues/index.md#filenames) are not uploaded. Folders are uploaded after being renamed.

:::{admonition} macOS only
:class: note
```{image} ../_images/File_Provider_Error.png
:alt: File Provider Icon
:width: 24px
:align: left
```
This additional icon displayed next to the filename in Finder.app indicates a sync error for the file.
:::


## Sync Progress

Changes to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{admonition} macOS only
:class: tip
Progress is shown when downloading or uploading a file with a progress bar over the file icon or circular progress indicator adjacent the filename.
```

### Keep Offline

Choose *Mountain Duck → Keep Offline on Local Disk* to make files and folders available offline. The status of the file will change to *In Sync*. The action is recursive for all contained files when a folder is selected and applies to new files found on the remote storage.

:::{admonition} macOS only
:class: tip

```{image} ../_images/File_Provider_Online_Only.png
:alt: File Provider Icon
:width: 24px
:align: left
```
_Download Now_ when using _Integrated_ connect mode downloads the file but allows it to be removed from cache on low disk space. 
:::


### Delete on Local Disk

Choose *Mountain Duck → Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk.

```{admonition} macOS only
:class: tip

Choose _Remove Download_ instead when using _Integrated_ connect mode.
```

## Limitations

- Custom mount locations are not honoured using the Integrated mode.
- The *Pseudo File locking* available in the Mountain Duck preferences *Connection* tab is not supported in *Integrated* mode.
