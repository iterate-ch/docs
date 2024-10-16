FAQ
====

:::{contents} Content
:depth: 2
:local:
:::

## General

### What is Cyberduck?

Cyberduck is an open-source server and cloud storage browser for Mac and Windows with support for FTP, SFTP, WebDAV, Amazon S3, OpenStack Swift, Backblaze B2, Microsoft Azure & OneDrive, Google Drive, and Dropbox licensed under the [GPL](https://github.com/iterate-ch/cyberduck/blob/master/LICENSE.txt).

### Is Cyberduck Free?

Cyberduck is free software. Free software is a matter of the users' freedom to run, copy, distribute, study, change, and improve the software. If you find this program useful, please consider making a [donation](http://cyberduck.ch/donate). A donation would not only demonstrate your appreciation of this software but also help to advance development in the future. You receive a registration key, and it will help to make Cyberduck even better!  Alternatively, you can purchase Cyberduck via App Store.

:::{image} _images/Donation_Prompt.png
:alt: Donation Prompt
:width: 600px
:::

#### Mac App Store

The presence of Cyberduck is important for the visibility of the project in particular for new and average users on the Mac platform. The caveat is that the donation key model is not supported in the App Store per the developer agreement. Software asking for voluntary contributions does not get approved. We have therefore opted to distribute Cyberduck in the App Store for a fixed price with no donation prompt. It is your choice to buy the version from the App Store or download from the website and opt in for a payment if you feel like. Cyberduck is libre (FLOSS) software and will remain so in the future.

#### Windows App Store

The Windows Store does not support the donation key model. We have therefore opted to distribute Cyberduck in the Windows Store for a fixed price with no donation prompt. It is your choice to buy the version from the Windows Store or download from the website and opt-in for a payment if you feel like. Cyberduck is libre (FLOSS) software and will remain so in the future.

##### Troubleshooting

If you bought Cyberduck on Windows Store, but you are not allowed to use Cyberduck due to a Trial Expired error message, please execute the following steps to ensure that your local app license cache is up-to-date – a reinstall of Cyberduck via Windows Store does not refresh your license.

1. Press the Windows Key + R which opens the “Run” function.
2. Type in “WSReset” and press enter
3. Open the Windows Store
4. Select the user icon (top right)
5. Select the very top option (where the user profile picture is listed)
6. Select the account
7. Select Sign Out
8. Select the user icon (top right)
9. Select Sign In

If these steps are not resolving the trial expired message please follow these additional steps to ensure all packages are registered correctly.

1. Open Start, type `PowerShell` and open it as Administrator (Ctrl+Shift+Enter, Right-click "Run as Administrator")
2. Copy `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Paste it into the window
4. Run it and wait for completion.

### What are the System Requirements for Cyberduck?

The system requirements are listed in the [installation section](installation.md#system-requirements).

#### Can I Install Older Version if Necessary?

The recent release can be found on our [website](https://cyberduck.io/download/). In case your operating system requires an older version of Cyberduck you can download installers for previous versions in our [changelog](https://cyberduck.io/changelog/).

## Registration Keys

As a contributor to Cyberduck, you receive a registration key that disables the donation prompt that is displayed when quitting Cyberduck.

### Recover a Registration Key

Registration keys can be [recovered](https://cyberduck.io/help#recover) using the email address you registered within the donation process.

### No Registration Key Received

- A key is sent when the payment is no more pending.
- Verify that your email address registered with PayPal is still valid.
- Check the spam folder of your email application.

### The Registration Key Received Cannot be Opened

The registration key is sent to you by email automatically after the transaction has been completed. Make sure the filename of the registration key ends with `.cyberducklicense`. Some email applications change the extension to `.xml` when saving the attachment. If the key is invalid, the file must have been modified when saving it from your email application. Try the following:

- If you are using a webmail provider, try using a different browser or email client application to access your mail.
- Contact you hosting service provider how to download attachments.
- Forward the mail to a different mail account where you possibly don't have an issue downloading attachments.

### Preferences and Application Support Files Location

::::{tabs}
:::{group-tab} macOS

Preferences are saved in `~/Library/Preferences/ch.sudo.cyberduck.plist`. Bookmarks, history, and [connection profiles](../protocols/profiles/index.md) are saved in the application support directory. These settings are shared with [Cyberduck CLI](../cli/index.md) and [Mountain Duck](../mountainduck/index.md).

- `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/`

Navigate to the *Library* folder using `⌘⇧-L` or use *Go → Go to Folder...* in Finder.

:::
:::{group-tab} Windows

Bookmarks, history, [connection profiles](../protocols/profiles/index.md), and workspace information are saved in the application data directory. You can navigate to the `AppData` folder by opening a *File Explorer* window and paste `%AppData%\Cyberduck` in the Quick access location field.

- `%AppData%\Cyberduck`

For the Windows Store version refer to 

- `%LocalAppData%\Packages\iterate.37637C3DE32E5_gr99yradmgg3r\LocalCache\Roaming\Cyberduck`

Preferences are stored in `%AppData%\Cyberduck\cyberduck.user.config`. Please note that settings in `%AppData%\Cyberduck\default.properties` takes precedence over `user.config`.

:::
::::

## Where can I Issue Bug Reports and Feature Requests?

To get help with bugs, feature requests, or other issues please refer to the [support page](support.md).

## Snapshot and Beta builds

See _[Preferences → Update](preferences.md#update)_ to switch the update feed.

## Incompatibilities

- *WindowDragon*. Cyberduck is [not compatible](http://sourceforge.net/tracker/index.php?func=detail&aid=1942730&group_id=208546&atid=1006129) with WindowDragon.
- Sophos Anti-Virus *On-access Scanning*
- Opening the web browser to authenticate using OAuth does not work with [Browser Chooser 2](https://browserchooser2.com/).
