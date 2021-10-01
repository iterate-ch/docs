Preferences
===

# Updates

An auto-update feature will alert you when a new version is available and self updates the application. Choose *Preferences → Automatically check for updates*. You can also choose to update to snapshot or beta builds.

- **Snapshot builds:** Include the latest changes and are published continuously. These builds are not manually tested.
- **Beta builds:** Published before a release and include the latest features and have been tested but might not have release quality yet.

```{admonition} Windows only
:class: tip
You receive no update notification if your user is missing administrator permission.
```

# General

## Login Item

Reconnect after restarting the computer. If you choose *Enable Login Item* and *Save Workspace* in *Preferences → General* and do not manually eject the volume prior to reboot it will reconnect after login.

## Bookmarks

Change the size of the menu items in the status bar menu. Choose between *Small, Medium,* and *Large* icons.

# Connection

## Mount Location 

````{admonition} macOS only
:class: tip

Volumes are mounted in the *Volumes* folder in the [application support directory](Support.md). You can change the default to another folder that is writable.

**Note:** You **cannot** set it to `/Volumes` on macOS Mojave (10.14 or later) where the directory is not writable. The setting is not available in the version from the Mac App Store.

The default is set to `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Volumes`.
````

## Cache

### Enable Cache

Allow buffering file contents in a temporary location which is only deleted when quitting the application. If unchecked, opened files will not automatically be available for offline usage when using connect mode *Smart Synchronization*.

## Locking

### Lock Files

Enable to prevent conflicting edits when accessing documents from a shared environment. Refer to [File Locking](Locking.md).

# Sync

## Connect Mode

Change the default synchronization option. You can disable synchronization by default for all bookmarks by switching to *Online*.

```{image} _images/Sync_Preferences.png
:alt: Send Command
:width: 700px
```

## Index Files

Index files on the server for a mounted connection in the background after connecting to ensure you can browse all directories when offline. Enabling this option will make sure new files available on the remote storage are detected without [manually](Interface.md#reload) choosing *Reload* in the context menu.

## Cache Location

`````{tabs}
````{group-tab} macOS
Change the location where to store cache files required for offline access. By default the *Cache* folder is in the [application support directory](Support.md).

The disk must be formatted as HFS+ or APFS.
````

````{group-tab} Windows
Change the location where to store cache files required for offline access. By default the *Cache* folder is in `%LocalAppData%\Cyberduck`.

You must select NTFS formatted drives with support for *NTFS Alternate Data Stream (ADS)*. FAT, FAT32, exFAT, and similar formatted drives are not supported. Network drives may not support alternate data streams as well.
````
`````

# Profiles

```{note}
Prelimitary documentation for Mountain Duck version 4.8
``` 

Select connection profiles to be installed. Either scroll through the list or use the search function to look for a specific profile. The connection profiles will be installed after ticking the corresponding checkboxes. Installed protocols are displayed in the protocol dropdown menu in the bookmark window. To disable the connection profile simply untick the checkbox. The profile will be disabled after closing the application.


## Default Connection Profiles

The following connection profiles are installed by default and can’t be deleted:

- [FTP (File Transfer Protocol)](../Protocols/FTP.md)
- [FTP-SSL (Explicit AUTH TLS)](../Protocols/FTP.md)
- [SFTP (SSH File Transfer Protocol)](../Protocols/SFTP.md)
- [WebDAV (HTTP)](../Protocols/WebDAV/index.md)
- [WebDAV (HTTPS)](../Protocols/WebDAV/index.md)
- [Amazon S3](../Protocols/S3/index.md)
- [Google Cloud Storage](../Protocols/Google_Cloud_Storage.md)
- [OpenStack Swift (Keystone 2.0)](../Protocols/OpenStack/index.md)
- [OpenStack Swift (Keystone 3)](../Protocols/OpenStack/index.md)
- [Windows Azure Blob Storage](../Protocols/Azure.md)
- [Backblaze B2 Cloud Storage](../Protocols/B2.md)
- [Dropbox](../Protocols/Dropbox.md)
- [Google Drive](../Protocols/Google_Drive.md)
- [Microsoft OneDrive](../Protocols/OneDrive.md)
- [Microsoft Sharepoint](../Protocols/SharePoint.md)
- [Microsoft Sharepoint Site](../Protocols/SharePoint.md)
- [DRACOON (OAuth)](../Protocols/Dracoon.md)
- [Files.com](../Protocols/Files.com.md)
- [Nextcloud](../Protocols/WebDAV/Nextcloud.md)
- [Rackspace Cloud Files (US)](../Protocols/OpenStack/CloudFiles.md)

# Notifications

`````{tabs}
````{group-tab} macOS

You can disable notifications in *System Preferences → Notifications*. Choose *None* for alert style and keep checked *Show* in *Notification Centre*. This way you will no longer be disturbed by any notification displays, but can still check back the notifications in *Notification Centre* anytime if required.
````
````{group-tab} Windows

You can disable notifications in *Settings → System → Notifications and Actions*. Uncheck *Show notification banners* and *Play a sound when a notification arrives*. Keep *Show notifications in action center* to see the notifications in Windows action center anytime if required.
````
`````

# Hidden Configuration Options

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