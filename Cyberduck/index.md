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

# [Opening Connections](Connection.md)

FTP, SFTP, WebDAV, OpenStack Swift, Google Storage, Amazon S3, and many more protocols are supported. There are several options to open a [connection](Connection.md) depending on the workflow.

# [Browser](Browser.md)

[Browser](Browser.md) remote files in a list or hierarchical outline view.

- **[Info Window](Info.md):** Edit access permissions and configure [CDN](../CDN/index.md) options
- **QuickLook:** Preview files in the browser window
- **Open Web URL:** Configuration steps to open HTTP URL of selected file
- **[Create and expand ZIP/TAR Archives](../Protocols/SFTP.md#create-and-expand-zip-or-tar-archives)**
- **[Send custom commands](../Protocols/SFTP.md#remote-commands):** Send commands to a server not available in the graphical user interface.
- **[Activity](Browser.md#activity):** The activity window shows a list of all pending background tasks.

```{note}
_Send custom commands_ and _Create and expand ZIP/TAR Archives_ are limited to FTP and SFTP. 
```

## [Edit Files](Edit.md)

Editing files on the server using an [external editor](Edit.md).

## [Share Files](Share.md)

Share files with others using signed or temporary URLs.

# [Bookmarks](Bookmarks.md)

Create and edit [bookmarks](Bookmarks.md) for your favorite servers.

- [Spotlight](Spotlight.md) support for bookmark files

# [File Transfers](Transfer.md)

- **[General](Transfer.md)** information about transfers. 
- **[Download](Download.md)** files and folders to your computer.
- **[Upload](Upload.md)** files and folders to a server.
- **[Synchronize](Sync.md)** folders between your computer and a server.
- **[Copy](Copy.md)** files and folders between servers.

# [Content Distribution (CDN)](../CDN/index.md)

- [Memset Memstore](../Protocols/OpenStack/Memset.md)
- [Amazon CloudFront](../CDN/CloudFront.md) content delivery options.
- [Akamai](../CDN/Akamai.md) content delivery options.
- [KeyCDN](../CDN/KeyCDN.md) content delivery options.

# [Notifications](Notifications.md)

- [Notifications](Notifications.md) configuration

# [Preferences](Preferences.md)

- Settings available in the [Preferences](Preferences.md) window.

# Incompatibilities

- *WindowDragon*. Cyberduck is [not compatible](http://sourceforge.net/tracker/index.php?func=detail&aid=1942730&group_id=208546&atid=1006129) with WindowDragon.
- Sophos Anti-Virus *On-access Scanning*.
- Opening the web browser to authenticate using OAuth does not work with [Browser Chooser 2](https://browserchooser2.com/).
