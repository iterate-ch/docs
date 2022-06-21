Preferences
====

```{contents} Content
:depth: 2
:local:
```

## General
### Save Workspace
Save all mounted volumes when quitting to be restored while relaunching.

### Bookmarks
Change the size of the menu items in the status bar menu. Choose between *Small, Medium,* and *Large* icons.

## Sync
### Connect Mode
Change the default synchronization option. You can disable synchronization by default for all bookmarks by switching to *Online*. Refer to [Connect Mode](interface.md#connect-mode)

```{image} _images/Sync_Preferences.png
:alt: Sync Preferences
:width: 700px
```

### Index Files
Index files on the server for a mounted connection in the background after connecting to ensure you can browse all directories when offline. Enabling this option will make sure new files available on the remote storage are detected without [manually](interface.md#reload) choosing *Reload* in the context menu.

### Enable Buffering
Choose whether the file contents should be buffered. The option allows buffering file contents in a temporary location which is only deleted when quitting the application.
- Allows faster access when reading or writing files with random access patterns from applications in _Online_ [mode](interface.md#connect-mode).
- With the option enabled in _Smart Synchronization_ [mode](interface.md#connect-mode), buffered file contents will be copied to the cache and the file can be opened when offline. Refer to [Status of Files](sync/index.md#status-of-files).

### Lock Files
Enable to prevent conflicting edits when accessing documents from a shared environment. Refer to [File Locking](locking.md).

### Mount Location 

````{admonition} macOS only
:class: tip

Volumes are mounted in the *Volumes* folder in the [application support directory](support.md). You can change the default to another folder that is writable.

**Note:** You **cannot** set it to `/Volumes` on macOS Mojave (10.14 or later) where the directory is not writable. The setting is not available in the version from the Mac App Store.

The default is set to `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Volumes`.
````

### Cache Location

`````{tabs}
````{group-tab} macOS
Change the location where to store cache files required for offline access. By default the *Cache* folder is in the [application support directory](support.md).

The disk must be formatted as HFS+ or APFS.
````

````{group-tab} Windows
Change the location where to store cache files required for offline access. By default the *Cache* folder is in `%LocalAppData%\Cyberduck`.

You must select NTFS formatted drives with support for *NTFS Alternate Data Stream (ADS)*. FAT, FAT32, exFAT, and similar formatted drives are not supported. Network drives may not support alternate data streams as well.
````
`````

#### Cache Limitations

```{note}
This feature is available for Mountain Duck version 4.12 and later.
```

Cache limitation allows cached files to be deleted from the cache at regular intervals, keeping only a placeholder with metadata. The following options are available:
- Limit cache size per bookmark by selecting a maximum folder size within the preference. Exceeding the maximum cache size, larger files are purged first. Available limits: 500MB, 1GB, 5GB, and 10GB.
- Purge files not accessed within a selected period of time automatically. Available periods: 1 day, 7 days, 30 days, and 60 days.

An indexer runs every hour to determine whether purging is required based on the set preferences.

## Notifications
Set which notifications you want to receive.

```{image} _images/Notification_Preferences.png
:alt: Notification Preferences
:width: 700px
```

Alternatively, you can choose *Open System Preferences* to disable the notifications completely.

`````{tabs}
````{group-tab} macOS

You can disable notifications in *System Preferences → Notifications*. Choose *None* for alert style and keep checked *Show* in *Notification Centre*. This way you will no longer be disturbed by any notification displays, but can still check back the notifications in *Notification Centre* anytime if required.
````
````{group-tab} Windows

You can disable notifications in *Settings → System → Notifications and Actions*. Uncheck *Show notification banners* and *Play a sound when a notification arrives*. Keep *Show notifications in action center* to see the notifications in Windows action center anytime if required.
````
`````

## Profiles
Select connection profiles to be installed. Either scroll through the list or use the search function to look for a specific profile. The connection profiles will be installed after ticking the corresponding checkboxes. Installed protocols are displayed in the protocol dropdown menu in the bookmark window. To disable the connection profile simply untick the checkbox. 

```{image} _images/Profiles_Preferences.png
:alt: Profiles Preferences
:width: 700px
```

### Default Connection Profiles
The connection profiles for [default protocols](../protocols/index.md) are always enabled.

## Login Item
Reconnect after restarting the computer. If you choose *Enable Login Item* and *Save Workspace* in *Preferences → General* and do not manually eject the volume prior to reboot it will reconnect after login.

## Updates
An auto-update feature will alert you when a new version is available and self updates the application. Choose *Preferences → Automatically check for updates*. You can also choose to update to snapshot or beta builds.

- **Snapshot builds:** Include the latest changes and are published continuously. These builds are not manually tested.
- **Beta builds:** Published before a release and include the latest features and have been tested but might not have release quality yet.

```{admonition} Windows only
:class: tip
You receive no update notification if your user is missing administrator permission.
```

## Hidden Configuration Options

`````{tabs}
````{group-tab} macOS

- Type the `defaults` command given in a *Terminal.app* (in `/Applications/Utilities`) window and restart Mountain Duck.
`defaults write io.mountainduck <property> <value>`
- Alternatively, create a file `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/default.properties` with the content formatted as `property=value`
````
````{group-tab} Windows

If not existing yet you need to create the file `%AppData%\Cyberduck\default.properties`. Add the setting as follows:<br/>
`property=value`

These settings are shared with Cyberduck.
````

`````