Browser
===

# Navigation

## List and Outline View

`````{tabs}
````{group-tab} macOS

Select *View → as List (`⌘1`)* or *View → as Outline (`⌘2`)* for expandable folders. You can expand and collapse folders using the right and left arrow keys in the outline view.

Navigate into a folder with a double-click *(`⌘↓`)* or one level up by using the ▲ button next to the path-field *(`⌘↑`)*.

````
````{group-tab} Windows

You can expand and collaps folders using the right and left arrow keys in the outline view.

Navigate into a folder with a doubl-click *(`Ctrl+Down`)* or one level up by using the ▲ button next to the path-field *(`Ctrl+Up`)*.

````
`````

## Tabs

```{admonition} macOS only
:class: tip

Enable tabs by default when choosing *File → New Browser (`⌘N`)* by selecting in System Preferences the checkbox *Dock → Prefer tabs when opening documents: Always*. New browser windows and the transfer window will then be displayed in a single window frame with a tab bar. You can merge windows with *View → Show Tab Bar and Window → Merge all Windows*

```

## Spring-loaded folders

Spring-loaded folders are a feature that allows you to move a file or even another folder, into a folder deeply nested within several other folders using drag and drop. To enable, choose *Preferences → Browser → Use spring-loaded folders when dragging files* and adjust the delay for the folder to expand when hovering over with the mouse. Note that spring-loaded folders are only supported in the outline view.

## Filter & Search

Use the search field (macOS `⌘/` Windows `Ctrl+F`) to display only files that match the search string in the browser. Search is case insensitive and does look for matching sequences in the filename. To search recursively, hit the return key (`⏎`). The following protocols have a server-side index that is used to give fast results without recursively descending into folders.

- [Google Drive](../Protocols/Google_Drive)
- [Dropbox](../Protocols/Dropbox)
- [Amazon S3](../Protocols/S3/index)
- [Backblaze B2](../Protocols/B2)
- [Microsoft OneDrive](../Protocols/OneDrive)

## Sorting

You can sort the file listing by clicking the table column header. Choose *View → Column* to add more headers such as *Kind* to allow sorting by file type including folders appearing first in the list.

## Local disk file browser

Choose your computer name forom the protocol selection popup button in the *New Connection* window.

ALternatively, you can use drag and drop or Menu *File → Upload (macOS `⌥↑` Windows `Alt+Up`)*. You can also copy *(macOS `⌘C` Windows `Ctrl+C`)* files in your file browser and paste them into Cyberduck using Menu *Edit → Paste (macOS `⌘V` Windows `Ctrl+V`)* afterward.

See other [upload](Upload) methods.

# Working with files and folders

## Edit

You can edit any file on the server using your preferred application. See [Edit Files](Edit).

## Create new folder or file

Use *File → New Folder... (macOS `⇧⌘N` Windows `Ctrl+Shift+N`)* or *File → New File... (macOS `⌘F` Windows `Ctrl+Shift+F`)* to create a new folder or file on the server.

## Move or duplicate files and folders

You can move files in the browser as you would in the *Finder.app/ Explorer* using drag and drop. Use the `⌥` modifier key on macOS or the Ctrl key on Windows to duplicate files. If connected to the same server, you can also move files between different browser windows.

The following protocols allow duplicating files on the server without downloading and uploading but copying in place:

- [S3](../Protocols/S3/index)
- [WebDAV](../Protocols/WebDAV/index)
- [Azure](../Protocols/Azure)
- [Dropbox](../Protocols/Dropbox)

To move a file, use *Edit → Cut (macOS `⌘X` Windows `Ctrl+X`)* followed by *Edit → Paste (macOS `⌘V` Windows `Ctrl+V`)*. To duplicate a file, use *Edit → Copy (macOS `⌘C` Windows `Ctrl+C`)* followed by *Edit → Paste (macOS `⌘V` Windows `Ctrl+V`)*.

## Copy files and folders to different server

You can copy files between arbitrary servers when connected to with two open browser windows. Drag files from one browser to the other to transfer files between servers.

```{image} _images/Copy.png
:alt: Send Command
:width: 700px
```

## Rename a file or folder

Select the file in the browser and press the *Return key*. Type the new name and press *Return* again to exit the editing mode. You can also rename fiels by choosing *File → Info (macOS `⌘I` Windows `Alt+Return`) or press the *Get [Info](Info)* toolbar button. Simply enter the new name in the very top field. THe field must lose focus (e.g. by hitting Return or Tab) to commit the filename change.

```{image} _images/Inline_Rename.png
:alt: Send Command
:width: 300px
```

## Create a symbolic link

Choose *File → New Symbolic Link...* to create a symbolic link. This is supported on UNIX systems with a [SFTP](../Protocols/SFTP) connection and some [FTP](../Protocols/FTP) with `SITE SYMLINK` extension.

## Info Window

Select the file in the browser and choose *File → Info (macOS `⌘I` Windows `Alt+Return`) to display [detailed attributes](Info)* of a file in a tool window. It allows to change permissions, manage content distributions for cloud services, and settings specific to the [Amazon S3](../Protocols/S3/index) service.

## Quick Look

```{admonition} macOS only
:class: tip

You can toggle Quick Look in a Cyberduck browser for any file using *Space Bar*. A preview is rendered depending on a Quick Look Plugin available on your system for the given file type. Many file types like different image formats can be previewed with the bundled plugins in OS X and HTML is even rendered in the Quick Look preview panel.

```

```{image} _images/quicklook.png
:alt: Send Command
:width: 500px
```

## Open or copy HTTP URL

See bookmark [Web URL configuration](Bookmarks#HTTPURL) for HTTP URLs. You can select multiple files to open/copy all URLs.

- **Open Web URL:** The *Web URL* can be found in the *File → Open URL* menu and as an optional toolbar item in the browser window. Use *View → Customize Toolbar...* to add the *Open in Browser* button to your default browser toolbar.
- **Copy Web URL:** The *Web URL* can be found in the *Edit → Copy URl* menu.

## Share Files

Refer to [Share](Share).

## Open in Terminal

Refer to [Open in Terminal](../Protocols/SFTP#OpeninTerminal).

## Print browser folder listing

Use the *File → Print* option where you can open a PDF from the browser listing or print it.

## Folder icon badges

Folder icons are badged for paticular access permissions.

```{image} _images/privatefolderbadge.png
:alt: Send Command
:width: 50px
```

Folder with no permission to access.

```{image} _images/readonlyfolderbadge.png
:alt: Send Command
:width: 50px
```

Folder with read-only permissions. Uploading or editing files to this folder is not possible.

```{image} _images/dropfolderbadge.png
:alt: Send Command
:width: 50px
```

Drop Folder where you can only upload files to bu are not allowed to view its content.

## Versions 

You can view all revisions of a file in the browser by choosing *View → Show Hidden Files*. The following protocols support verisoning

- [S3](../Protocols/S3/index)
- [Backblaze B2](../Protocols/B2)
- [Google Drive](../Protocols/Google_Drive)

### Revert

To revert to a previous version and make it the current, choose *File → Revert*.

# Activity

Use *Window → Activity (macOS `⌘0` Windows `Ctrl+0`)* to toggle the activity window. It lists the currently running background tasks at the top and all queued activities subsequently.

```{image} _images/Activity.png
:alt: Send Command
:width: 500px
```

# Problems

## Special characters such as Umlaute

If characters aren't displayed correctly in the browser, try to change the character encoding used. See *View → Text Encoding* or edit the [bookmark](Bookmarks#EditBookmark) *Encoding* setting. Try `UTF-8` (the default), `ISO-8859-1`, and `Windows-1252`.

## The folder size isn't displayed correctly

This is not the size of its content but the size of the folder itself. Use *File → Info (macOS `⌘I` Windows `Alt+Return`)* to [calculate the size](Info#Calculatefoldersize) of all contained files recursively.

# Preferences

## General → Browser → Save Workspace

Restore browser sessions that were left open when the application was last closed.

## General → Browser → Open new browser window on startup

Open new browser window after application launch.

## Browser → General → Show Hidden Files

Display files in the browser that start with `.` and [previous revisions (S3)](../Protocols/S3/index#Versions). Use *View → Show Hidden Files* to toggle the mode of a current browser window.

## Browser → General → Info window always sshows current selection

Use only one *Info* window which updates with the selection change in the browser. If unchecked, open multiple Info windows to compare files.

# Hidden Preferences

## Adjust the browser font size

A [hidden configurationi option](Preferences#Hiddenconfigurationoptions).

`defaults write ch.sudo.cyberduck browser.font.size 18`

## Duplicate filename format

A [hidden configurationi option](Preferences#Hiddenconfigurationoptions). Define a different format using 

`defaults write ch.sudo.cyberduck browser.duplicate.format "{0} ({1}){2}"`

where the plaseholders will be replaced with

- {0} with the base filename
- {1} with the timestampof the file
- {2} with the extension in the format `.extension` if present in the original filename.

## Warning before renaming or moving files

A [hidden configurationi option](Preferences#Hiddenconfigurationoptions). A confirmation is shown before renaming or moving files.

`defaults write ch.sudo.cyberduck browser.move.confirm true`