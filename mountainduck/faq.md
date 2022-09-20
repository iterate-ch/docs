FAQ
====

## Usage

### Synchronization

#### Resolving synchronization errors

To synchronize files with *Error* badge, use the *Retry* option in the context menu.
If you intend to upload files to a target directory not existing on the server, you have to move the file to a location that does exist on the server.

To upload files marked as *Ignored* successfully, you have to rename the file.

#### How to cancel upload in progress

To abort active sync processes, use the following steps:
1. Select *Pause Synchronization* in the Mountain Duck dropdown menu.
2. Select *Delete on local Disk* within the Mountain Duck context menu.
3. *Resume Synchronization* in the dropdown menu.

You can use the steps as well to cancel *Keep Offline* processes.

#### Reload

Mountain Duck doesn't have the ability to monitor changes on the remote server. You have to manually refresh the file listing by choosing [*Reload*](interface.md#reload) within the context menu.

#### Indexer

Using the *Smart Synchronization* mode, an [indexer](preferences.md#index-files) can be enabled to detect and sync changes from the remote server every 10 minutes. Without using the indexer you can only dectect new files by refreshing the file listing manually.
Please note that files won't be updated in background while indexing is paused.

This feature is not available for the *Online* mode. You won't be able to browse files and folders as soon as the server connection gets interrupted.

### Disk space

Mountain Duck uses disk space for every cached file. A [cache limitation feature](preferences.md#cache-limitations) is available for Mountain Duck version 4.12 and later.

To free some space use the cache management option to purge unused files from the cache or use the synchronization option *[Delete on local Disk](sync/index.md#delete-on-local-disk)* on white space on the mounted drive.

#### File Caching

Files will be cached as soon as you work with them: e.g. open, save, upload, [*Keep Offline on Local Disk*](sync/index.md#keep-offline).

Using the *Smart Synchronization* mode, the cached data are saved within the [sync cache](preferences.md#cache-location). Using the *Online* mode, cached files will be saved in the temporary system cache.

#### Auto cache management

Cache management options were added in version 4.12. You can choose a limit for the synchronization cache per bookmark and can select a timeframe for unused files to be purged.

Note that files marked as *Keep Offline* are not affected by cache size limit. The files won't be purged from the cache until you choose *Delete on local Disk*.

#### Temporary files lifecycle



#### How does *Enable Buffer* affect disk space usage?

With buffering enabled, Mountain Duck will use more disk space. To allow you faster read access for buffered files, Mountain Duck saves temporary copies of the files.

#### Disk usage in *Online* mode

Using the *Online* mode, metadata and temporary copies of files you work with will be stored within the _temp_ folder. Depending on the connection profile in use, the cached data will be removed from the temp cache once you disconnect the bookmark.

### Run as a Windows Service

It is not possible to run Mountain Duck as a Service as it needs an interactive user session to mount drives. As the mounts are also limited to the user session there isn't any way to mount a drive once and share it with all other users.

### Web URL

Using Cyberduck, you have an additional panel to include a Web URL. This Web URL will replace your server address using the *Copy URL* feature. Using Mountain Duck, there is no such feature but the setting from Cyberduck are taken over.
