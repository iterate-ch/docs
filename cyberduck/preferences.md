Preferences
====

:::{toctree}
:hidden:
:titlesonly:
../tutorials/hidden_properties
:::

:::{contents} Content
:depth: 2
:local:
:::
 
In general, user adjustable preferences are discussed in the context of the topic in all wiki pages.

## General

### Save Workspace

Save open connections when quitting and restore when opening the application.

### Bookmarks

Change the row height of bookmarks displayed in the browser window. Choose between *Small, Medium,* and *Large* icons.

## [Browser](browser.md)

Choose a bookmark you want to connect upon startup and manage general settings for files and folders like shortcuts to open files or hidden file settings.

## [Transfers](transfer.md)

Manage transfer settings for uploads and downloads as well as the connection typ to use.

## Editor

Select the text editor you want to use a as default application to open with if no other file association with an installed application can be found. Decide if you want to always use the selected application to open files regardless of the default application determined by the operating system for the file type.

## [Profiles](../protocols/profiles/index.md)

Select connection profiles to be installed. Either scroll through the list or use the search function to look for a specific profile. The connection profiles will be installed after ticking the corresponding checkboxes. Installed protocols are displayed in the protocol dropdown menu in the bookmark window. To disable the connection profile simply untick the checkbox. 

## Protocols

Manage protocol specific settings.

### FTP

Choose the text encoding you want to use to convert characters in filenames. The default setting is UTF-8.

### S3

Set a default bucket region as well as the storage class, encryption, and ACL for uploads or newly created files and buckets.

### Google Storage

Specify the default bucket location, storage class, and ACLs for uploads or newly created files and buckets.

## Bandwidth

Limit the maximum bandwidth that is allowed for transfers. Useful when you don't want transfers to take all the bandwidth available on your internet connection that would slow down other connections. 

## [Connection](connection.md#connection)

Manage general connection settings like the default protocol, timeouts, and proxy settings. Choose whether you want to save your credentials using macOS Keychain or Windows Credential Manager. Activate debug logging and reach the log file in case it is requested for troubleshooting purposes.

## Cryptomator

Choose whether your [Cryptomator vaults](../cryptomator/index.md) should be auto detected and unlocked while browsing the parent folder or not by using the *Auto detect and open vault in browser* option.

:::{note}
Without saving the vaults passwords using keychain, you will receive passwords prompts for the vaults after reconnecting to the server or cloud storage.
::: 

### Use Keychain

Specify if you want the *Save Password* option enabled by default while entering the password to unlock your vault. With the option disabled you have to check the checkbox to save the password in keychain manually. 

## Language

Choose the language of the user interface. It defaults to the system language when set to *Default*. Thirty localizations are included.

- On macOS, the first matching language is chosen according to the *Languages* list within System *Preferences → International*. To change your preferred language for all applications, change the preset hierarchy.

:::{image} _images/Language_Preference.png
:alt: Send Command
:width: 500px
:::

## Update

An auto update feature will alert you when a new version is available and self update the application. Choose *Preferences → Update → Automatically check for updates*. You can also get the latest builds by a [manual download](https://update.cyberduck.io/nightly/).

### Snapshot Builds

Snapshot builds include the latest changes and are published regularly. These builds are not tested.

:::{image} _images/Update.png
:alt: Update
:width: 500px
:::

### Beta Builds

Beta builds are published before a release and include the latest features and have been tested but haven't release quality yet.

## Hidden Configuration Options

::::{tabs}
:::{tab} Cyberduck

Refer to [Add Hidden Configuration Options to Mountain Duck and Cyberduck](../tutorials/hidden_properties.md)

:::
:::{tab} CLI

Refer to [Preferences](../cli/index.md#preferences)

:::
::::