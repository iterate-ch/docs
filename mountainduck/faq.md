FAQ
====

## General

### What is Mountain Duck?

Mountain Duck is a client application that lets you mount various server and cloud storage as a disk in Finder on macOS and the File Explorer on Windows. Open remote files with any application and work like on a local volume.

### Is Mountain Duck free to use?

You can test Mountain Duck for free using the [14-days trial](https://mountainduck.io/). Once the trial expired you have to buy a license via website or Mac AppStore to keep on using the application.

## License files

Each license is valid for one person. Purchasing more than one seat, you receive a single multi-user license file to be used for all users.

### Trial license

If you receive a `Download trial failed` error while intending to trial Mountain Duck, you're experiencing bug occurring from time to time. Please reach out to the [Mountain Duck support](mailto:support@mountainduck.io) to receive a trial license file.

### No license file received

You won't receive a license file after purchasing via AppStore because the application is registered to the store account in use while purchasing.

Additional reasons for a missing license file can be:
- A key is sent when the payment is no more pending.
- Verify that your email address registered with PayPal is still valid.
- Check the spam folder of your email application.

### Not a valid registration key

Your license file is valid for an older version of Mountain Duck. Please upgrade your license file to use the latest version of the application or revert to an older version.

An additional reason might be, that your email application changed the license file while downloading. Make sure that the filename of the registration key ends with `.mountainducklicense`. In this case please try the following:
- If you are using a webmail provider, try using a different browser or email client application to access your mail.
- Contact you hosting service provider how to download attachments.
- Forward the mail to a different mail account where you possibly don’t have an issue downloading attachments.
- Change the file extension of the license file back to `.mountainducklicense`.

### Recover license files

Registration keys can be [recovered](https://mountainduck.io/help/) using the email address you registered while purchasing.

## Installation

### Finder Extension

Using macOS, you'll have to enable the Finder Extension manually. Refer to the [documentation](installation.md) for further information.

### Switching from Trial to AppStore

To use the App Store version of Mountain Duck after testing the application, you have to uninstall the current installed version prior to install the App Store version.

### Application Support folder

The [application support folder](support.md#application-support-folder) contains files and folders for settings, log data, history files and more. 

## Usage

### Reload

Mountain Duck doesn't have the ability to monitor changes on the remote server. You have to manually refresh the file listing by choosing [*Reload*](interface.md#reload) within the context menu.

### Indexer

Using the *Smart Synchronization* mode, an [indexer](preferences.md#index-files) can be enabled to detect and sync changes from the remote server every 10 minutes. This feature doesn't work using the *Online* mode.

### File Caching

Files will be cached as soon as you work with them: e.g. open, save, upload, [*Keep Offline on Local Disk*](sync/index.md#keep-offline).

Using the *Smart Synchronization* mode, the cached data are saved within the [sync cache](preferences.md#cache-location). Using the *Online* mode, cached files will be saved in the temporary system cache.

#### Disk space

Mountain Duck uses disk space for every cached file. A [cache limitation feature](preferences.md#cache-limitations) is available for Mountain Duck version 4.12 and later.

### Web URL

Using Cyberduck, you have an additional panel to include a Web URL. This Web URL will replace your server address using the *Copy URL* feature. Using Mountain Duck, there is no such feature but the setting from Cyberduck are taken over.