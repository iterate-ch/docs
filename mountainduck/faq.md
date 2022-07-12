FAQ
====

## General

### What is Mountain Duck?

Mountain Duck is a client application that lets you mount various server and cloud storage as a disk in Finder on macOS and the File Explorer on Windows. Open remote files with any application and work like on a local volume.

### Is Mountain Duck free to use?

You can test Mountain Duck for free using the [14-days trial](https://mountainduck.io/). Once the trial expired you have to buy a license via website or Mac AppStore to keep on using the application.

## License files

Each license is valid for one person. Purchasing more than one seat, you receive a single multi-user license file to be used for all users.

Refer to the [documentation](installation/licensing.md) for further information.

## Installation

### Finder Extension

Using macOS, you'll have to enable the Finder Extension manually. Refer to the [documentation](installation/index.md) for further information.

### Switching from Trial to AppStore

To use the App Store version of Mountain Duck after testing the application, you have to uninstall the current installed version prior to install the App Store version.

### Application Support folder

The [application support folder](support.md#application-support-folder) contains files and folders for settings, log data, history files and more. 

### Windows Installation

If you're experiencing the error code `0x24C` `A volume has been accessed for which a file system driver is required that has not yet been loaded.`, please uninstall the client, reboot the system, and reinstall the client.

## Usage

### Synchronization

#### Reload

Mountain Duck doesn't have the ability to monitor changes on the remote server. You have to manually refresh the file listing by choosing [*Reload*](interface.md#reload) within the context menu.

#### Indexer

Using the *Smart Synchronization* mode, an [indexer](preferences.md#index-files) can be enabled to detect and sync changes from the remote server every 10 minutes. This feature doesn't work using the *Online* mode.

### File Caching

Files will be cached as soon as you work with them: e.g. open, save, upload, [*Keep Offline on Local Disk*](sync/index.md#keep-offline).

Using the *Smart Synchronization* mode, the cached data are saved within the [sync cache](preferences.md#cache-location). Using the *Online* mode, cached files will be saved in the temporary system cache.

#### Disk space

Mountain Duck uses disk space for every cached file. A [cache limitation feature](preferences.md#cache-limitations) is available for Mountain Duck version 4.12 and later.

#### Temporary files lifecycle



#### How does *Enable Buffer* affect disk space usage?



#### Disk usage in *Online* mode

Using the *Online*, metadata and temporary copies of files you work with will be stored within the _temp_ folder. Depending on the connection profile in use, the cached data will be removed from the temp cache once you disconnect the bookmark.

### Run as a Windows Service

It is not possible to run Mountain Duck as a Service as it needs an interactive user session to mount drives. As the mounts are also limited to the user session there isn't any way to mount a drive once and share it with all other users.

### Web URL

Using Cyberduck, you have an additional panel to include a Web URL. This Web URL will replace your server address using the *Copy URL* feature. Using Mountain Duck, there is no such feature but the setting from Cyberduck are taken over.
