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

```{image} _images/Sync_Preferences_Win.png
:alt: Sync Preferences
:width: 700px
```

### Index Files
Index files on the server for a mounted connection in the background after connecting to ensure you can browse all directories when offline. Enabling this option will make sure new files available on the remote storage are detected without [manually](interface.md#reload) choosing *Reload* in the context menu. When enabled, remote directories previously opened are polled for changes and new files periodically every 10 minutes. 

```{warning}
This feature is not available in *Online* connect mode. You cannot browse folders or open files as soon as the server connection gets interrupted.
```

### Enable Buffering
Choose whether the file contents should be buffered. The option allows buffering file contents in a temporary location which is only deleted when quitting the application.
- Allows faster access when reading or writing files with random access patterns from applications in _Online_ [mode](interface.md#connect-mode).
- With the option enabled in _Smart Synchronization_ [mode](interface.md#connect-mode), buffered file contents will be copied to the cache and the file can be opened when offline. Refer to [Status of Files](connect/sync.md#status-of-files).

### Lock Files
Enable to prevent conflicting edits when accessing documents from a shared environment. Refer to [File Locking](locking.md).

### Mount Location 

````{admonition} macOS only
:class: tip

Volumes are mounted in the *Volumes* folder in the [application support directory](support.md). You can change the default to another folder that is writable.

**Note:** You **cannot** set it to `/Volumes` on macOS Mojave (10.14 or later) where the directory is not writable. The setting is not available in the version from the Mac App Store. 

The default is set to `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Volumes.noindex`.
````

### Cache Location

`````{tabs}
````{group-tab} macOS
Change the location where to store cache files required for offline access. By default the *Cache* folder is in the [application support directory](support.md). The disk must be formatted as HFS+ or APFS.
````

````{group-tab} Windows
Change the location where to store cache files required for offline access. By default the *Cache* folder is in `%LocalAppData%\Cyberduck`. You must select NTFS formatted drives with support for *NTFS Alternate Data Stream (ADS)*. FAT, FAT32, exFAT, and similar formatted drives are not supported. Network drives may not support alternate data streams as well.
````
`````

```{warning}
Do not manually move, delete or modify files in the obfuscated local cache location.
```

#### Cache Limitations

Periodically free up space with cache limitations to purge unused files from the cache at regular intervals in the background keeping only a placeholder with metadata. You can choose a limit for the synchronization cache per bookmark and can select a timeframe for unused files to be purged.

The following options are available:
- **Limit by size**. Limit cache size per bookmark by selecting a maximum folder size within the preference. Exceeding the maximum cache size, larger files are purged first.
- **Limit by time**. Purge files not accessed within a selected period of time automatically.

```{tip}
Files selected to always keep offline are never automatically removed from the cache.
```

By default, files are kept in cache for 30 days and the cache is limited to a maximum size of 5GiB.

```{attention}
The settings apply separately for each bookmark which must be connected for the cache management to run.
```

## Notifications

Set which type of notifications you want to receive. Alternatively, you can choose *Open System Preferences* to disable the notifications all together. The following types of notifications can be toggled:
- **Filesystem mounted**. The volume is now connected. 
- **Filesystem unmounted**. The volume has been disconnected.
- **Pause Sync**. Synchronization has paused due to the server not reachable because of a network or login error.
- **Resume Sync**. Synchronization has automatically resumed as after reachability change.
- **File Added**. New file has been found on the server not previously synced.
- **File Deleted**. File has been deleted on the server previously synced.
- **File Updated**. File has been updated on the server previously synced.
- **File Uncached**. File previously cached for offline access has been purged.
- **Download complete**. File download completed in the background.
- **Upload complete**. File upload completed in the background.
- **Sync Error**. Error synchronizing file because of a server error response.
- **Sync Conflict**. Error synchronizing file because of a sync conflict.

```{image} _images/Notification_Preferences.png
:alt: Notification Preferences
:width: 700px
```

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

## Cryptomator
Choose wheather or not your [Cryptomator vaults](../cryptomator/index.md) should be auto detected and unlocked while browsing the parent folder or not by using the *Auto detect and open vault in browser* option.

```{note}
Without saving the vaults passwords using keychain, you will receive passwords prompts for the vaults after reconnecting to the server or cloud storage.
``` 

### Use Keychain
Specify if you want the *Save Password* option enabled by default while entering the password to unlock your vault. With the option disabled you have to check the checkbox to save the password in keychain manually. 

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