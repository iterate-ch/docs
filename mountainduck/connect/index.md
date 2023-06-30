Connect mode
===

```{toctree}
:hidden:
:titlesonly:
sync
```
While connecting to a server, you can choose between *Online* mode and *[Smart Synchronization](sync.md)* mode.

## Online Mode

The *online* mode is the most basic connect mode. Files you open get stored in the temporary system cache and deleted at the latest when the bookmark is disconnected.

### Transfer progress

While transferring files and folders, a transfer window will popup showing the transfer progress. In case of small files, the transfer might be finished to quick to actually realise the popup.

## Status of Files

Files and folders on a mounted volume have a status icon overlay in File Explorer (Windows) and Finder (macOS).

```{note}
Please make sure to enable the Mountain Duck [Integration](../installation/index.md) in *System Preferences → Extensions → Finder* on macOS. For macOS Ventura and later, the setting can be found in *System Settings → Privacy & Security → Extensions → Added Extensions*.
```

### ![](../_images/overlay_infinite.png) Online Only
The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

### ![](../_images/overlay_error.png) Sync Error
There was an error updating the file after changes. You are missing permission to write to the file or another problem occured. Please contact your web hosting service provider for assistance. To resolve the error, move the file to your local disk, and reload the directory or use the _Retry_ option within the context menu. Refer to [Sync Conflicts](sync.md#sync-conflicts) for possible error scenarios.

### ![](../_images/overlay_ignored.png) Ignored
The file is only saved in a local [temporary](../issues/index.md#temporary-files) location and never synced to the server or cloud storage.

## Sync paused

You can manually pause uploads and indexing by selecting *Pause Sync* in the submenu for the sync status. Syncing is also paused automatically when your network connection to the server is interrupted but resumed automatically when a connection is restored.

```{warning}
As long as the sync status is paused, uncached files marked as [Online Only](#online-only) can't be opened. An error message will be shown by the application attempting to open the file and a *Access Denied* notification will show up.
```

## Sync Errors

Files that failed to sync get a sync error badge. You can try to repeat the failed transfer by selecting *Mountain Duck → Retry* in the context menu.

### Resolve Errors

If a sync error cannot be solved using *Mountain Duck → Retry* because the server does not allow the operation (i.e. due to a permission issue), you can resolve the error state on the file or folder by

- Move the file or folder to another location on the volume
- Delete the file or folder 

To upload files to a target directory no longer existing on the server, you have to move the files to a location found on the server.

## Sync Limitations

Specific file types are excluded from sync operations per default. Files matching those criteria won't be synced from or to the server and marked with the *ignored* badge icon.

### New Files and Folders

New files created via context menu are created as 0-byte files and therefore not transfered to the server. The same goes for new folders with default name.
* In Finder.app: *Untitled folder* and localized variants
* In Windows Explorer: *New folder* and localized variants

The files and folders will be synchronized after being renamed.

### Files excluded by Name

Some file types especially temporary files are excluded from sync processes per default. They are listed in the following [hidden configuration options](../../cyberduck/preferences.md#hidden-configuration-options).

	fs.filenames.temporary.regexp=\.nfs\..* \.VolumeIcon.icns \.DS_Store .*~$ .*~\..* \._~\$.* \.~(?!lock).*[^#] .*\.tmp ~.*\.tmp .*~.*\.TMP .*\.swap .*\.swp Word\sWork\sFile.*\.tmp \._Word\sWork\sFile.*\.tmp (.*)\.sb-[\w]{8}-[\w]{6} \._.*\.(doc|docx)\.sb-.* \.TemporaryItems \.dat\.nosync.* TestFile[\d]+-[\d]+$ .*~[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}$ Adobe\ Photoshop\ [\d]+$ DBTmp.* .*\.lck [0-9A-Z]+\.tmp .*\.idlk Desktop\.ini desktop\.ini Thumbs\.db \(A\ Document\ Being\ Saved\ By\ .*\) ai[\d]{10}.* AI\ Temp.* .*\.crdownload .*\.part .*\.onetmp \.goutputstream-.* Adobe\ Premiere\ Pro\ Auto-Save

### Files excluded by Pattern

Files matching the following default pattern won't be synced from the server or remote storage as they are excluded from the listing process: `.`, `..`, `*/*`, `*\*`, `*:*`

You can exclude additional file types from the listing by using following [hidden configuration options](../../cyberduck/preferences.md#hidden-configuration-options).

	fs.filenames.filter.name.regexp=[\\.]{1,2} .*[:\\/\\\\].*

## Notifications

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
