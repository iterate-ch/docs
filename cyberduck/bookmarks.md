Bookmarks
====

## Toggle Bookmarks

`````{tabs}
````{group-tab} macOS

You can toggle between the bookmarks and the browser using *Bookmarks → Toggle Bookmarks (`⌘B`)* or by clicking the bookmarks icon in the navigation toolbar. Depending on the bookmark icon size chosen in *Cyberduck → Preferences → Browser → Bookmarks*, the nickname, URL, username, and comment are shown per bookmark.

````
````{group-tab} Windows

You can toggle between the bookmarks and the browser using *Bookmarks → Toggle Bookmarks (`Strg+B`)* or by clicking the bookmarks icon in the navigation toolbar. Depending on the bookmark icon size chosen in *Edit → Preferences → Browser → Bookmarks*, the nickname, URL, username, and comment are shown per bookmark.

````
`````

## Sorting 

You can manually sort bookmarks by dragging a row to a different location.

## Filter

Use the search field *(macOS `⌘/` Windows `Strg+F`)* to filter bookmarks by nickname, hostname, and labels. Only bookmarks that match the search string are displayed in the bookmark list. Search is case insensitive.

## Labels & Groups

```{note}
Currently macOS only, Cyberduck 7.3 or later required
```

### Edit Labels for Bookmarks

Assign multiple labels to a bookmark to group them in folders in the menu.

```{image} _images/Edit_Labels_for_Bookmark.png
:alt: Edit Labels for Bookmark
:width: 500px
```

### Groups in Bookmarks Menu

Bookmarks are grouped in folders in the menu by their assigned labels. Groups in bookmark view forthcoming.

```{image} _images/Groups_in_Bookmarks_Menu.png
:alt: Groups in Bookmarks Menu
:width: 400px
```

## Add new Bookmark

### From Current Connection

`````{tabs}
````{group-tab} macOS

Select *Bookmarks → Toggle Bookmarks (`⌘B`)*. Click the + button in lower left corner to add the server that's currently connected to this browser window to the Bookmarks. An editor window will open where you can adjust the bookmark properties (i.e. nickname) further.

```{image} _images/Add_Bookmark.png
:alt: Add Bookmark
:width: 400px
```

Drag the proxy icon in the browser window title bar to the bookmark drawer or to the *Finder.app*. You can double-click this file in the *Finder.app* to open a new connection.

```{image} _images/Proxy_Icon.png
:alt: Proxy Icon
:width: 400px
```

````
````{group-tab} Windows

Select *Bookmarks → Toggle Bookmarks (`Strg+B`)*. Click the + button in lower left corner to add the server that's currently connected to this browser window to the Bookmarks. An editor window will open where you can adjust the bookmark properties (i.e. nickname) further.

```{image} _images/Add_Bookmark.png
:alt: Add Bookmark
:width: 400px
```

````
`````

### From a Third-Party Application

Drag an URL from a third-party application to the bookmark table to create a new bookmark. This can be a link embedded in a web page or from any text source.

## Edit Bookmark

Select *Bookmark → Edit Bookmark (macOS `⌘E` Windows `Strg+E`)*. A panel where you can edit the bookmark's properties will appear. If the server configured is not reachable, an alert icon is displayed next to the URL. Clicking it opens *Network Diagnostics*.

```{image} _images/WebDAV_Bookmark_Client_Certificate.png
:alt: WebDAV Bookmark Client Certificate
:width: 600px
```

### Bookmark Options

| Setting | Description |
| :--- | :--- |
| Protocol | Your hosting service provider will let you know what protocol to use. Change the [protocol](connection.md#supported-protocols) in the<br/>topmost popup menu. |
| Nickname | Any name for the bookmark describing it for easy access using the bookmark filter. You can<br/>also type this name in the bookmark view to select it by name. |
| Server | The hostname of the server. This is not editable if you have chosen a protocol with a predefined,<br/>non-configurable hostname. |
| Username | The login credentials from your service provider. |
| SSH Private<br/>Key | For [SFTP](../protocols/sftp.md) connections only. Choose a private key for public key authentication instead of a<br/>password. If the key is password-protected, you are prompted to enter the passphrase to<br/>decrypt the key. |
| Client<br/>Certificate | For [HTTPS](../protocols/webdav/index.md#mutual-tls-mtls) connections only. Choose a client certificate for mutual transport level security (TLS). |
| Path | The initial working directory when connecting to the server. This must be the document root of<br/>the webserver if you want to configure HTTP URLs ([see below](#http-url)) to work. |
| Download<br/>Folder | Default location for files downloaded from this server. |
| Transfer<br/>Files | Choose to open a new connection for transfers in the [transfers](transfer.md#connections) window or to use the existing<br/>browser connection. When using the browser connection, transfers block other operations. |
| Connect<br/>Mode | For [FTP](../protocols/ftp.md) connections only. Refer to [FTP Connect Mode](../protocols/ftp.md#ftp-connect-mode). |
| Encoding | For [FTP](../protocols/ftp.md) connections only. Character encoding of filenames on the server. You can also change<br/>the encoding used when the connection is open using *View → Text Encoding* if characters<br/>are not displayed properly. Try `UTF-8` (the default), `ISO-8859-1`, and `Windows-1252`.<br/>Refer to [Character Encoding](../protocols/ftp.md#character-encoding). |
| Timezone | For all protocols except [FTP](../protocols/ftp.md), timestamps are reported in [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) from the server and there is no<br/>need for configuration. All timestamps in the browser are automatically converted to the timezone<br/>you have configured in the *System Preferences* and displayed in local time. For [FTP](../protocols/ftp.md)<br/>however, the local timezone is assumed for timestamps in directory listings If the server<br/>is configured with a different timezone that your Mac and returning the local time for<br/>modification dates, there will be an offset by the timezone difference. To get the correct local<br/>time for modification dates in the browser, you can choose the timezone of the server in the<br/>bookmark settings. Select *Bookmark → Edit Bookmark*. |

### Passwords

`````{tabs}
````{group-tab} macOS

Manage your passwords with *Keychain Access.app*. Refer to [Keychain for Mac: Kexchain Access overview](https://support.apple.com/kb/PH20093?locale=en_US).

````
````{group-tab} Windows

Passwords are saved in the *Credential Manager*. You can view and delete your saved login information in *Control Panel → User Accounts → Credential Manager → Windows Credentials*.

````
`````

## HTTP URL

With a valid configuration, you can open the corresponding HTTP URL of a file selected with your default web browser or copy the URL to the clipboard. You can select multiple files in the browser for a list of URLs.

Enter the HTTP URL of the web server using a different hostname than what you connect to using FTP. You also have to specify a reasonable default path in your bookmark (e.g. `/home/dkocher/public_html/`). That must be the directory accessed by the web server as your document root. Using an Apache web server this is equivalent to the `DocumentRoot` directive.

Example configuration:

| Server | sudo.ch | *Hostname configured in bookmark to<br/>connect to* |
| :--- | --- | ---: |
| Bookmark<br/>Path | `/usr/home/dkocher/public_html/` | *The Web Server Document Root* |
| Selected File | `/home/dkocher/public_html/stylsheet.css` | *A file selected in the browser* |
| HTTP URL | [http://sudo.ch/stylesheet.css](http://sudo.ch/stylesheet.css) | *Accessible in the web browser* |

```{image} _images/HTTP_URL.png
:alt: HTTP URL
:width: 600px
```

See also [Open or copy HTTP URL](browser.md#open-or-copy-http-url).

## Exporting Bookmarks

Drag the bookmark from the Bookmark Drawer anywhere to the *Finder.app/ Explorer* (e.g. the Desktop). You can double-click the document in the file browser to open a new connection to the server specified in the bookmark. To back up all bookmarks, refer to [this FAQ entry](faq.md#preferences-and-application-support-files-location).

```{image} _images/Drag_Bookmark.png
:alt: Drag Bookmark
:width: 300px
```

```{note}
You can share bookmarks between Mac & Windows as the file format is the same on both platforms.
```

## Importing Bookmarks

### From Exported Bookmark File

Just drag the `.duck` bookmark file from the *Finder.app/ Explorer* to the list of bookmarks.

### From Third-Party Applications

You are asked if you want to import bookmarks from the following list of applications if the application is still installed on your system and bookmarks configured with the application are found. There is no manual import functionality available.

- *Transmit 4* from `~/Library/Application Support/Transmit/Favorites/Favorites.xml`
- *Transmit 5* from `~/Library/Application Support/Transmit/Metadata`
- *Filezilla* from `~/.config/filezilla/sitemanager.xml`
- *Fetch* from `~/Library/Preferemces/com.fetchsoftworks.Fetch.Shortcuts.plist`
- *Flow* from `~/Library/Application Support/Flow/Bookmarks.plist`
- *Interarchy* from `~/Library/Application Support/Interarchy/Bookmark.plist`
- *SmartFTP*
- *FlashFXP*
- *WS_FTP*
- *FlashFXP 3/4*
- *CrossFTP* from `~/.crossftp/sites.xml`
- *FireFTP* from `~/Library/Application Support/Firefox/Profiles`
- *CloudBerry Explorer for Amazon S3*
- *CloudBerry Explorer for Google Storage*
- *CloudBerry Explorer for Azure Blob*
- *WinSCP* (as of <del>[4.1.1](https://trac.cyberduck.io/milestone/4.1.1)</del> for [INI file to store configuration](http://winscp.net/eng/docs/ui_pref_storage#configuration_storage))
- *Expandrive 3* from `~/Library/Application Support/ExpanDrive/favorites.js`
- *Expandrive 4* from `~/Library/Application Support/ExpanDrive/expandrive4.favorites.js`
- *Expandrive 5* from `~/Library/Application Support/ExpanDrive/expandrive5.favorites.js`
- *Expandrive 6* from `~/Library/Application Support/ExpanDrive/expandrive6.favorites.js`
- *Total Commander*
- *Cloud Mounter* from `~/Library/Preferences/com.eltima.cloudmounter.plist`

```{image} _images/Filezilla_Import.png
:alt: FileZilla Import
:width: 600px
```

## Sharing Bookmarks between Different Computers

You can share bookmarks between different computers and users by uploading the *Bookmarks* and *Profiles* folder to a Cloud Storage of your liking and creating a symbolic link to it.

**Step by step instructions using Dropbox as an example:**</br>
`````{tabs}
````{group-tab} macOS

1. Install the Dropbox app, log into your Dropbox account and synchronize the folder where you want to have the bookmarks to the local disk.
2. Quit *Cyberduck* and/or *Mountain Duck*.
3. Navigate to `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` and move the folders *Bookmarks* and if available *Profiles* to the desired location on Dropbox.
4. Open *Terminal.app* and execute the command `ln -s <AppSupportDirectory/foldername> <CloudDirectory>` to create the symbolic link.

````
````{group-tab} Windows

1. Install the Dropbox app, log into your Dropbox account and synchronize the folder where you want to have the bookmarks to the local disk.
2. Quit *Cyberduck* and/or *Mountain Duck*.
3. Navigate to `%AppData%\Cyberduck` and move the folders *Bookmarks* and if available *Profiles* to the desired location on Dropbox.
4. Use one of the options below to create the symbolic link:
	- Open *CMD* and execute the command `mklink /J <AppSupportDirectory\foldername> <CloudDirectory>`.
	- Open *PowerShell* and execute the command `New-Item -Type Junction -Target <CloudDirectory> -Path <AppSupportDirectory\foldername>`

````
`````

## Preferences

### Open Default Bookmark

Choose a default bookmark to open after opening the application. Choose *Preferences → General → Open new browser window on startup → Connect to bookmark ...*.

### Do not Read favicon.ico from HTTP URL

A [hidden configuration option](preferences.md#hidden-configuration-options). Displayed in the bookmark edit window.

`defaults write ch.sudo.cyberduck bookmark.favicon.download false`

### Open Bookmark View after Disconnecting

A [hidden configuration option](preferences.md#hidden-configuration-options).

`defaults write ch.sudo.cyberduck browser.disconnect.bookmarks.show true`
