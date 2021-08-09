Smart Synchronization
===

```{image} _images/Disk_Syncing.png
:alt: Send Command
:width: 200px
```

The smart sync feature allows making files available offline. You can also choose to make explicitly all or only selected files and folders available for offline use. Changes to files are saved in a local cache first and uploaded in the background as soon as connection is available.

# Bookmark Options

You can change the synchronization options for a bookmark in *Connect Mode*.

- *Default:* Use setting from *Preferences*
- *Online:* Do not synchronize any files to your computer. You can only access this volume when a connection is possible to the server or cloud storage. Files are accessed on demand from the remote when opened and do not take up any local disk space.
- *Smart Synchronization:* Files opened are made available for later offline access. You can explicitly make files available offline using the [context menu](Sync#Select-files-and-folders-to-always-keep-offline).

# Status of files

Files and folders on a mounted volume have a status icon overlay in File Explorer (Windows) and Finder (macOS).

```{note}
Please make sure to enable the Mountain Duck [Integration](Installation) in *System Preferences → Extensions → Finder* on macOS.
```

## Up to Date

```{image} _images/overlay_uptodate.png
:alt: Send Command
:width: 50px
```

The file or the contents of a directory has been opened and downloaded to your computer and therefore currently synced with the server or cloud storage. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will appear as *Online Only* and are not downloaded automatically. Files copied to a volume are kept cached by default.

## In Sync

```{image} _images/overlay_sync.png
:alt: Send Command
:width: 50px
```

The file or directory is selected to be synced with the server or cloud storage to always keep offline. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will be downloaded automatically.

## Online Only

```{image} _images/overlay_infinite.png
:alt: Send Command
:width: 50px
```

The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

## Sync in Progress

```{image} _images/overlay_syncing.png
:alt: Send Command
:width: 50px
```

The file or directory is currently synced with the server or cloud storage.

## Sync Error

```{image} _images/overlay_error.png
:alt: Send Command
:width: 50px
```

There was an error updating the file after changes. You are missing permission to write to the file or another problem occured. Please contact your web hosting service provider for assistance. To resolve the error, move the file to your local disk and reload the directory.

## Ignored

```{image} _images/overlay_ignored.png
:alt: Send Command
:width: 50px
```

The file is only saved in a local temporary location and never synced to the server or cloud storage.


```{image} _images/Mountain_Duck_Screenshot_Finder_Dark.png
:alt: Send Command
:width: 800px
```

# Context Menu Options

```{admonition} macOS only
:class: tip

Please make sure to enable the Mountain Duck [Integration](index#FinderExtensionWindowsFileExplorerExtensionFinder) in *System Preferences → Extensions → Finder Extensions*.
```

## Select files and folders to always keep offline

You can choose to make files and folders available offline in the context menu. Those files and folders are located within an obfuscated synchronization cache and can't be accessed outside of your bookmark. You need an active connection to the bookmark to see the offline folders. That means that you have to connect to your server once while you have access to an active internet connection. If you don't disconnect the bookmark and the connection to the server isn't interrupted otherwise you can still access the files that are located within the local synchronization cache. As soon as you are connected to the internet again, all changes are transferred to the server in the background.

```{image} _images/Sync_Context_Menu_macOS.png
:alt: Send Command
:width: 500px
```

To reach the context menu right-click on a file or folder in File Explorer (Windows) or FInder (macOS). Refer to [Finder Extension & Windows File Explorer Extension](Interface#context-menu-in-finder-and-windows-file-explorer).

### Keep Offline

- Choose *Mountian Duck → Keep Offline on Local Disk* to make the file available offline. The status of the file will change to *In Sync*. The action is recursive for all contained files when a folder is selected and applies to new files found on the remote storage.

### Delete on Local Disk

- Choose *Mountain Duck →Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk

```{note}
Choosing this option won't prevent Mountain Duck from downloading there files and folders into the synchronization cache again.
```

```{video} _videos/Keep_Offline.mp4
:width: 500
:height: 300
```

![Keep Offline](_videos/KeepOffline.mp4)


# Sync Conflicts

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
| Edit file already changed<br/>on server | Last seen checksum differs from current<br/>checksum on server. (Or timestamp<br/>when server does not offer checksum<br/>verification) | - | Existing file on server is renamed<br/> ro `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead. | User has to manually merge<br/>the conflicting edits. |
| Edit file with parent folder<br/>missing on server | Upload fails because parent folder<br/>is not found on server | Sync Error | - | Move file to different folder<br/>or *Retry* option in context menu |
| Move or rename *file* to target<br/>that already exists on server | Directory index is out of sync | - | Existing file on server is renamed<br/>to `<filename> timestamp.<extension>`.<br/>Eventually with user preference to<br/>default to sync error instead. | User has to manually merge<br/>the conflicting edits. |
| Move or rename *directory* to target<br/>that already exists on server | Directory index is out of sync | - | Existing directory on server is renamed<br/>to `<folder> timestamp.<extension>` | User has to manually merge the<br/>conflicting edits. |
| Move or rename *directory* that no<br/>longer exists on server | Directory index is out of sync | Sync Error | Directory is removed from local cache | - |
| Create file that exists already on server | Directory index is out of sync | - | Failure creating file is ignored | - |
| Create folder that exists already on<br/>server | Directory index is out of sync | - | Failure creating folder is ignored | -  
| Deleting file already changed on server | Directory index is out of sync | - | File is deleted on server | - |

(1) Indexed file in local cache not downloaded from server

# Sync Progress

CHanges to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{image} _images/Sync_in_Progress.gif
:alt: Send Command
:width: 600px
```
Detailed status for current transfers is available in the *Sync* submenu. Refer to [Sync Progress](Sync_History#sync-progress).

## Pause Sync

You can manually pause background syncing by selecting *Pause Sync* in the submenu for the sync status. Syncing is also paused automatically when your network connection to the server is interrupted but resumed automatically when a connection is restored.

The paused sync status is indicated with a greyed-out icon in the tray (Windows) or status bar (macOS).

# Sync Errors

Files that failed to sync get a sync error badge. You can try to repeat the failed transfer by selecting *Mountain Duck → Retry* in the context menu.

## Resolve Errors

If a sync error cannot be solved using *Mountain Duck → Retry* because the server does not allow the operatio due to a permission issue you can resolve the error state on the file or folder by

- Move the file or folder to another location on the volume
- Delete the file or folder

# File History

You can lookup the latest changes to files. Refer to [Recent Files](Sync_History#recent-files)

## Notifications

```{image} _images/File_Updated_Notification.png
:alt: Send Command
:width: 500px
```

- **File Added:** New file found on server for previously indexed folder.
- **File Updated:** File changed on server since previously indexing a folder
- **Sync Conflict:** Conflicting change in file lead to duplicate of file being created with previous content edited on server.

Refer also to [Preferences → Notifications](Preferences#notifications)

# Preferences

Refer to [Preferences](Preferences).