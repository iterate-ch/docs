Known Issues
====

```{toctree}
:hidden:
:titlesonly:

fastcgi
```

```{contents} Content
:depth: 2
:local:
```

## Performance Considerations

To reduce the number of requests to the remote server for mounted volumes, we recommend the following settings when running in *Online* connect mode.

`````{tabs}
````{group-tab} macOS
**Finder.app**<br/>

- Choose *View → Hide Preview* (⌘⇧P)
- Disable *View → Show View Options → Show icon preview*

````
````{group-tab} Windows
**Windows Explorer**<br/>
Choose *File Explorer → Folder Options*.

- Check *Always show icons, never thumbnails*
- Check *Display File Icon on thumbnails*
- Uncheck *Show preview handlers in preview pane*
````

`````

## Temporary Files
When opening files with status _Online only_ or when connected with _Online_ connect mode, it may be required to temporarily cache contents depending on the read pattern of the application opening the file. Data ist stored in the temporary file location of the operating system and allows for faster access when repeatedly reading the file. Temporary files are deleted as soon as the application closes the file after reading, unless the option _Enable buffering_ checked in _Preferences → Sync_. 

```{tip}
When enabled _Preferences → Sync → Enable buffering_ is enabled:
* In _Online_ connect mode, buffered content in temporary files is kept until disconnecting the bookmark.
* In _Smart Synchronization_ connect mode, the buffer contents is moved from the temporary folder to the local cache and the status of the file changes to _Up to Date_.
```

## Filenames

The following characters should be avoided within file and folder names.

`````{tabs}
````{group-tab} macOS

- `:` (colon)
- `/` (forward slash)
- `\` (backslash)

````
````{group-tab} Windows

- `<` (less than)
- `>` (greater than)
- `:` (colon)
- `"` (double quote)
- `/` (forward slash)
- `\` (backslash)
- `|` (vertical bar or pipe)
- `?` (question mark)
- `*` (asterik)

````
`````

## Known Issues

### `Download trial failed.` Error

This is a known bug appearing from time to time while downloading the trial version of Mountain Duck. Please reach out to the [Mountain Duck support](mailto:support@mountainduck.io) to receive a trial license file.

### `Not a valid registration key` Error

This error appears if you try to use a license key for older versions of Mountain Duck for a new major version. Registration keys are valid for the current major version at the time of purchase and for previous versions. To use the latest major version you will have to [upgrade](https://mountainduck.io/buy/upgrade/) your license. Alternatively, install an older version of Mountain Duck from the [changelog](https://mountainduck.io/changelog/).

### Can only open single PDF in Adobe Acrobat Reader

This is a known bug in Adobe Acrobat Reader when opening documents from a network volume. As a workaround uncheck *edit → Preferences... → Security (Enhanced) → Enable Protected Mode at startup*.

- Adobe Documentation: [Protected mode (Windows)](https://helpx.adobe.com/reader/11/using/protected-mode-windows.html)

### rsync fails with error

If your server does not accept the creation of `.` temporary files you might need to add the `--inplace` when running `rsync`.

### High CPU usage when working with Sublime Text

- When working with Sublime Text we recommend turning off indexing by adding the following setting to your user preferences in Sublime Text. <br/>
`"index_files": false`
- You might want to [turn off Git support in Sublime](https://www.sublimetext.com/docs/git_integration.html) which has caused high CPU usage for some users when scanning `.git` folders. <br/>
`"show_git_status": false`

### Sharing a mounted drive in local network

It is not possible to share a mounted drive within the local network.

### Changes from server not immediately visible

In _Smart Synchronization_ connect mode changes from the server must be synced with cached contents on your computer. The directory listing in *Finder.app* or *File Explorer* may become out of date when another application is adding, removing, or modifying files on the server. No push notifications are received for changes on the server. Thus, the following strategies are in place to detect changes to existing and new files as soon as possible:
* With [_Preferences → Sync → Index Files_](../preferences.md#index-files) enabled, remote directories previously opened are polled for changes and new files.
* When browsing a directory in Finder.app or Windows Explorer will attempt to sync with contents with the server.
* You can explicitly request to look for changes on the server in a directory by choosing [*Reload*](../interface.md#reload) within the context menu.

### New folder not uploaded to remote server

Folders that weren't renamed after creation don't get uploaded to the server. Change the folder name to something else than *Untitled Folder* on macOS or *New Folder* on Windows, and the folder should be uploaded to the server and be visible on the server.

### Cache uses a lot of disk space

Disk space is used on your computer for every cached file marked as _Up to Date_ or _In Sync_ in Smart Synchronization [connect mode](../sync/index.md). Files are cached as soon as accessed (e.g. open in any application or previewing in _Finder.app_ or _Windows Explorer_) or explicitly with [*Keep Offline on Local Disk*](../sync/index.md#keep-offline).

The cache size can be limited per bookmark in *Preferences → Sync*. Also files not accessed within a chosen period of time can be purged. Refer to [Cache Limitations](../preferences.md#cache-limitations).

The cache directory is located in `%LocalAppData%\Cyberduck\Cache` on Windows or within *Application Support folder* on macOS by default. You can [change the cache location](../preferences.md#cache-location) to any writable location. You can clear cached files from the local disk with the *Delete on local disk* [context menu](../sync/index.md#delete-on-local-disk) option.

```{image} ../_images/Custom_Location_Sync_Cache.png
:alt: Send Command
:width: 600px
```

### Insufficient disk space 

If the available disk space on the mounted volume is below 100MB a soft quota notification will be displayed saying *Insufficient space*. 
Synchronization is paused when the soft quota is reached.

```{image} ../_images/Soft_Quota_Disk_Space.png
:alt: Soft Quota Insufficient disk space
:width: 400px
```

This quota information is only available for the following protocols:
- [WebDAV](../../protocols/webdav/index.md)
- [Google Drive](../../protocols/google_drive.md)
- [Dropdox](../../protocols/dropbox.md)
- [Microsoft OneDrive](../../protocols/onedrive.md)
- [Microsoft Sharepoint](../../protocols/sharepoint.md)
- [SFTP](../../protocols/sftp.md)

### View files from Synplogy Drive 

*Synology Drive* is not supported natively. You can try to view your *Synology Drive* files by connecting to your *Synology NAS*. To do that connect to your *Synology NAS* using the protocol **SFTP, FTP,** or **WebDAV** with the path `home/Drive`.

```{note}
This won't allow you to view and access shared files and folders.
```

### Missing Sync Status Icons

`````{tabs}
````{group-tab} macOS

**Finder**<br/>
When you have other applications installed that register a Finder Extension (macOS) for the volume mounted, the status icon may not appear. This has been reported for the following applications:

- [*Araxis Merge*](https://www.araxis.com/merge/index.en)
- [*BetterZip*](https://macitbetter.com/)
- [*Sophos*](https://www.sophos.com/en-us). Documented in [SAV for Mac OS - Sophos Finder Extension Known Issues](https://community.sophos.com/kb/en-us/132136)
- [*Keka*](https://www.keka.io/en/)

Please check in *System Preferences → Extension → Finder* for other applications that may override the badge icons.

```{note}
If none of those applications are in use, a Finder re-launch can make the badge icons appear again.
```

````
````{group-tab} Windows

**Explorer**<br/>
Windows has a limitation on the number of applications that can register for bagde icons in File Explorer. You will need to either uninstall other applications or edit your registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers`.
You can find this well documented by Microsoft at [Sync icon overlays are missing](https://support.office.com/en-us/article/sync-icon-overlays-are-missing-from-onedrive-and-onedrive-for-business-b25070ab-2226-4ad8-b1fc-ae28cc44ecd2).
````
````` 

### Operating System specific Issues

`````{tabs}
````{group-tab} macOS

**Mount is not Visible within the Media Browser (Adobe Premiere)**<br/>
Bookmarks mounted by Mountain Duck aren't visible within the *Media Browser* of Adobe Premiere. The mount location needs to be [changed](../preferences.md#mount-location) (e.g. to the desktop) to make the mount visible.

**Finder.app Does not Show Files Prefixed with `.` on Remote Volumes**<br/>
You can work around this by setting `defaults write com.apple.finder AppleShowAllFiles YES` in a *Terminal.app* window and restart *Finder.app* using *→ Force Quit ... → Finder → Relaunch*. If you are running macOS Sierra (10.12) you can choose `⌘⇧.` to toggle files starting with a dot to show in Finder.app.

**Original Document can't be Changed (Preview.app)**<br/>
Files opened in Preview.app and edited cannot be saved at the original location but the message "The original document can't be changed, so a duplicate with your changes has been created" is displayed in the title bar. As a workaround, you can set a custom mount point in *Preferences → Connection → Mount Location* for volumes such as a `~/Volumes/` folder in your home directory.

**Enable Application Icon in Dock**<br/>
As a utility application with no application windows, no icon is displayed in the Dock but only in the system status bar. If you want to enable the application icon to appear in the Dock set the following property:

    defaults write io.mountainduck application.dock.icon.enable true

**Mounted Volumes do not Appear on the Desktop**<br/>
Navigate to volumes using `⌘⇧C` in a *Finder.app* window or choose *Finder → Preferences ... → General → Show these items on the desktop: Connected Servers* to make the volume appear on the desktop. Mounted volumes are also listed in the *Finder.app* sidebar in *Favorites*.

**Search in Finder.app (Spotlight)**<br/>
The Spotlight indexer does not work on remote volumes.

**Multiple Mountain Duck Finder Extensions Processes**<br/>
The system may launch additional copies of *Mountain Duck Finder Extension* whenever an Open or Save dialog is displayed. This means there may be multiple copies of the extension running at once, and some may be very short-lived.

**Connection Interrupted**<br/>
It may be that Finder closes the connection because Mountain Duck hasn't answered fast enough on the request of Finder. Although Finder indicates that the server connection is interrupted it isn't as Mountain Duck is still connected to the server.

This is an issue within the operating system that can occur to any network drive.

<del> **Additional `._*` Files Saved on Remote Volumes** </del> <br/>
<del> The `._*` files contain metadata about the files some applications write in additional to the file content. On macOS, this metadata can be stored alongside the file on the filesystem, but on remote volumes, with no metadata suppport, an auxiliary file is created to contain this information. You can delete metadata on files using `xattr -d <filename>`. </del>

As of version [2.1](https://mountainduck.io/changelog/), extended attributes are only saved in a temporary location and not stored on the mounted remote volume. If you want to revert to saving extended attributes to the server, enter in a *Terminal.app* window:

    defaults write io.mountainduck fs.filenames.metadata.enable false

If you want to delete metadata files, you can open a *Terminal.app* window and enter `dot_clean -m <folder>`.

````
````{group-tab} Windows

**File System Driver isn't set up Properly**<br/>
Error: `A volume has been accessed for which a file system driver is required that has not yet been loaded`

If you get this error message you most likely haven't restarted your system after the installation or update of Mountain Duck. Restart your system to resolve this error. If a system restart doesn't resolve the error try to repair Mountain Duck followed by an application reinstall if this doesn't work either. Additionally, make sure no antivirus software is interfering with the operation of Mountain Duck.

**Missing Files in Windows Explorer**<br/>
Windows has a limitation on the maximum path length. It might happen that Mountain Duck exceeds this maximum for long file names when trying to create placeholders in the local cache. If Mountain Duck is unable to create a placeholder file for a remote file it will not appear in the Windows Explorer listing.

To work around this Windows limitaion you can enable long path support in Windows 10 as of version 1607.

1. Open the *Local Group Policy editor* (search for *Edit Group Policy*)
2. Navigate to *Local Computer Policy → Computer Configuration → Administrative Templates → System → Filesystem*
3. Double-click the *Enable NTFS long paths* option and select *Enabled*

Please refer to [Maximum Path Length Limitation](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).

**Multiple File Versions**<br/>
This is expected behavior within the *Online* mode as Windows Explorer will first create an empty file followed by writing to the file. Due to this process, you'll see two versions within the versioning on your server. Within the *Smart Synchronization* mode the empty file won't be synced and the upload is deferred until the file has been fully copied.

**Windows Search Indexer**<br/>
The Windows Search indexer does not work on networks drives.

**Windows Sessions**<br/>
Mountain Duck requires an interactive user logon session. This separation is done to ensure that each in a multi-user scenario has access to all available Windows drive letters (Otherwise this would be limited to 26 drive letters, shared across all users). Bookmarks are mounted in your regular and elevated user session only - there is no way for other logged-in users or non-interactive services to access your drive. There are no persistent mounts created for anyone to use and cannot work across user sessions - mounts for user A are not visible nor accessible by user B even on the same machine.

**Windows Service has no Access to a Mounted Drive**<br/>
See Windows sessions above. It is not possible to run Mountain Duck as a Service as it needs an interactive user session to mount drives. As the mounts are also limited to the user session there isn't any way to mount a drive once and share it with all other users. Please make sure you have not checked `Run whether user is logged on or not` on the scheduled task configuration.

**Mountain Duck Tooltip Persists on Screen**<br/>
You can close that overlay by holding your mouse cursor for about 3 seconds on the Mountain Duck icon within the Tray area.

**Dot files are not hidden**<br/>
By default, files starting with `.` aren't hidden by Windows Explorer. You can change the default by using a [hidden configuration option](../preferences.md#hidden-configuration-options).

    browser.hidden.regex=\\..*

````

`````

## Interoperability

### Hosting Service Providers

A list of known providers that fail to work with Mountain Duck due to interoperability issues.

- *OwnCube:* Their deployment does not work and we discourage this product.
- *Bitnami ownCloud:* PHP-FPM is enabled by default in virtual machines and Ubuntu-based cloud images but must be disabled for uploads to complete. Refer to [How to disable PHP-FPM](https://docs.bitnami.com/general/infrastructure/lamp/administration/disable-phpfpm/) and [0 byte files on WebDAV server](../../protocols/webdav/index.md#0-byte-files-on-webdav-server).

### Third-Party Software

#### Kaspersky Internet Security

Make sure to uninstall Kaspersky Internet Security with its kernel extensions causing kernel panics prior to mounting a volume.

#### Eset Cyber Security Pro

Make sure not connections on the loopback interface are blocked.

#### Bitdefender

Be aware that Bitdefender may interfere with connections.

#### Sophos Endpoint Protection

May interfere with installation.

### Backups

`````{tabs}
````{group-tab} macOS

**Time Machine**<br/>
Backups to Time Machine do not work with volumes mounted from Mountain Duck. Time Machine requires disks mounted using Apple File Protocol (AFP). See [Backup disks you can use with Time Machine](https://support.apple.com/en-us/HT202784).

````
````{group-tab} Windows

**Windows Backup**<br/>
Volumes mounted with Mountain Duck cannot be used by *Windows Backup*. It can only save backups on destinations that are located within your local system or within your local network.

````
`````

## Bug Reports and Feature Requests

To get help with bugs, feature requests, or other issues please refer to [support](../support.md). 
