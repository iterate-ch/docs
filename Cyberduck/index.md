Cyberduck 
===

```{toctree}
:hidden:

Bookmarks
Browser
Connection
Copy
Download
Edit
FAQ
Info
Logging
Notifications
Preferences
Profiles
Share
Spotlight
Support
Sync
Transfer
Upload
```
# Quick Reference Cheat Sheet

Download the {download}`Cyberduck Quick Reference<https://trac.cyberduck.io/raw-attachment/wiki/help/en/howto/cyberduck/Cyberduck%20Quick%20Reference.pdf>` PDF.

```{image} _images/Cyberduck_Quick_Reference_Page_1.png
:alt: Send Command
:width: 700px
```

```{image} _images/Cyberduck_Quick_Reference_Page_2.png
:alt: Send Command
:width: 700px
```

# [Opening Connections](Connection)

FTP, SFTP, WebDAV, OpenStack Swift, Google Storage, Amazon S3, and many more protocols are supported. There are several options to open a [connection](Connection) depending on the workflow.

# [Browser](Browser)

[Browser](Browser) remote files in a list or hierarchical outline view.

- **[Info Window](Info):** Edit access permissions and configure [CDN](../CDN/index) options
- **QuickLook:** Preview files in the browser window
- **Open Web URL:** Configuration steps to open HTTP URL of selected file
- **[Create and expand ZIP/TAR Archives](../Protocols/SFTP#create-and-expand-zip-tar-archives)**
- **[Send custom commands](../Protocols/SFTP#remote-commands):** Send commands to a server not available in the graphical user interface.
- **[Activity](Browser#activity):** The activity window shows a list of all pending background tasks.

```{note}
_Send custom commands_ and _Create and expand ZIP/TAR Archives_ are limited to FTP and SFTP. 
```

## [Edit Files](Edit)

Editing files on the server using an [external editor](Edit).

## [Share Files](Share)

Share files with others using signed or temporary URLs.

# [Bookmarks](Bookmarks)

Create and edit [bookmarks](Bookmarks) for your favorite servers.

- [Spotlight](Spotlight) support for bookmark files

# [File Transfers](Transfer)

- **[General](Transfer)** information about transfers. 
- **[Download](Download)** files and folders to your computer.
- **[Upload](Upload)** files and folders to a server.
- **[Synchronize](Sync)** folders between your computer and a server.
- **[Copy](Copy)** files and folders between servers.

# [Content Distribution (CDN)](../CDN/index)

- [Memset Memstore](../Protocols/OpenStack/Memset)
- [Amazon CloudFront](../CDN/CloudFront) content delivery options.
- [Akamai](../CDN/Akamai) content delivery options.
- [KeyCDN](../CDN/KeyCDN) content delivery options.

# [Notifications](Notifications)

- [Notifications](Notifications) configuration

# [Preferences](Preferences)

- Settings available in the [Preferences](Preferences) window.

# Incompatibilities

- *WindowDragon*. Cyberduck is [not compatible](http://sourceforge.net/tracker/index.php?func=detail&aid=1942730&group_id=208546&atid=1006129) with WindowDragon.
- Sophos Anti-Virus *On-access Scanning*.
- Opening the web browser to authenticate using OAuth does not work with [Browser Chooser 2](https://browserchooser2.com/).