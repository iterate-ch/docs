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
- *Smart Synchronization:* Files opened are made available for later offline access. You can explicitly make files available offline using the [context menu](Sync#Selectfilesandfolderstoalwayskeepoffline).

# Status of files

Files and folders on a mounted volume have a status icon overlay in File Explorer (Windows) and Finder (macOS).

```{note}
Please make sure to enable the Mountain Duck [Integration]() in *System Preferences → Extensions → Finder* on macOS.
```

## Up to Date

```{image}

```

The file or the contents of a directory has been opened and downloaded to your computer and therefore currently synced with the server or cloud storage. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will appear as *Online Only* and are not downloaded automatically. Files copied to a volume are kept cached by default.

## In Sync

```{image}

```

The file or directory is selected to be synced with the server or cloud storage to always keep offline. The file takes disk space on your computer and can always be opened even when no connection to the server or cloud storage is possible. New files in a directory on the remote server will be downloaded automatically.

## Online Only

```{image}

```

The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

## Sync in Progress

```{image}

```

The file or directory is currently synced with the server or cloud storage.


```{image} _images/Mountain_Duck_Screenshot_Finder_Dark.png
:alt: Send Command
:width: 500px
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

To reach the context menu right-click on a file or folder in File Explorer (Windows) or FInder (macOS). Refer to [Finder Extension & Windows File Explorer Extension](Interface#ContextMenuinFinderandWindowsFileExplorer).

### Keep Offline

- Choose *Mountian Duck → Keep Offline on Local Disk* to make the file available offline. The status of the file will change to *In Sync*. The action is recursive for all contained files when a folder is selected and applies to new files found on the remote storage.

### Delete on Local Disk

- Choose *Mountain Duck →Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk

```{note}
Choosing this option won't prevent Mountain Duck from downloading there files and folders into the synchronization cache again.
```

```{video} _videos/Keep_Offline.mp4
:alt: Send Command
:width: 500
:height: 300
```

# Sync Conflicts

A conflict may be caused by two or more users editing the same files at the same time or while on the road before the files are synced. We do not merge changes to files like version control systems do. The file with conflicting edits will be renamed with the current time added to the filename. You will have to compare the changes manually and delete the duplicate file afterwards.

| Action | Error Cause | Error State (Overlay Icon) | Remarks | Manual Conflict Resolution |
| --- | --- | --- | --- | ---: | 
| Indexing folder | Missing permission | Sync Error for files with<br/> pending write | Other files are removed from<br/> local cache | Context menu with options<br/> *Retry* |				  							   				  				   						 
