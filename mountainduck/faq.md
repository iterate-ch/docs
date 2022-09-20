FAQ
====

## Synchronization

### Resolve synchronization errors
To synchronize files with *Error* badge, use the *Retry* option in the context menu.
If you intend to upload files to a target directory not existing on the server, you have to move the file to a location that does exist on the server.
To upload files marked as *Ignored* successfully, you have to rename the file.

### Cancel upload in progress
To abort the upload of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Delete the file
3. *Resume Synchronization* in the dropdown menu.

You can use the steps as well to cancel *Keep Offline* processes.

### Cancel download in progress
To abort the download of a file, follow these steps:
1. Choose *Pause Synchronization* in the Mountain Duck _Synchronization_ menu.
2. Select *Delete on local Disk* within the Mountain Duck [context menu](interface.md#context-menu-in-finder-and-windows-file-explorer).
3. *Resume Synchronization* in the dropdown menu.


### Reload changes from server
In _Smart Synchronization_ connect mode changes from the server must be synced with cached contents on your computer.

Mountain Duck doesn't have the ability to receive push notifications for change on the server. Thus, the following strategies 
are in place to detect changes to existing and new files as soon as possible.
* **Index Files**. When enabled in _Preferences → Sync_, remote directories previously opened are polled for changes and new files periodically every 10 minutes. This includes only folders previously opened.
```{warn}
This feature is not available in *Online* connect mode. You cannot browse folders or open files as soon as the server 
connection gets interrupted.
```
* When browsing a directory in Finder.app or Windows Explorer will attempt to sync with contents with the server.

```{warning}
When synchronization is paused by selecting _Pause Sync_ in the menu or caused by a connectivity problem, no changes from the server will be detected.
```
You can explicitly request to look for changes on the server in a directory by choosing [*Reload*](interface.md#reload) within the context menu.

### Disk Space Usage
Mountain Duck uses disk space on your computer for every cached file marked as _Up to Date_ or _In Sync_ in Smart Synchronization [connect mode](sync/index.md). 

#### Smart Synchronization Cache
Free up space using
* [Cache Limitations](../preferences.md#cache-limitations) to purge unused files from the cache periodically in the background. You can choose a limit for the synchronization cache per bookmark and can select a timeframe for unused files to be purged. Files marked as *Keep Offline* are not affected by cache size limit. These files won't be purged from the cache until you choose *Delete on local Disk*.
* Use the option *[Delete on local Disk](sync/index.md#delete-on-local-disk)* in the [context menu](interface.md#context-menu-in-finder-and-windows-file-explorer).

Files are cached as soon as accessed (e.g. open in any application or previewing in _Finder.app_ or _Windows Explorer_) or 
explicitly with [*Keep Offline on Local Disk*](sync/index.md#keep-offline).

Using the *Smart Synchronization* connect mode, the cached data is saved in the [sync cache](preferences.md#cache-location). 

```{warning}
Do not manually move, delete or modify files in the obfuscated local cache location.
```

#### Temporary Files
When opening files with status _Online only_ or when connected with _Online_ connect mode, it may be required to temporarily cache contents depending on the read pattern of the application opening the file. Data ist stored in the temporary file location of the operating system and allows for faster access when repeatedly reading the file.

Temporary files are deleted as soon as the application closes the file after reading, unless the option _Enable buffering_ checked in _Preferences → Sync_. When enabled,
* In _Online_ connect mode, buffered content in temporary files is kept until disconnecting the bookmark.
* In _Smart Synchronization_ connect mode, the buffer contents is moved from the temporary folder to the local cache and the status of the file changes to _Up to Date_.
