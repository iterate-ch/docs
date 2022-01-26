Upload
====

See also [Transfers](transfer.md) in general.

## Menu File → Upload...

Select *File → Upload...* to select files to upload.

## Toolbar

There is a toolbar button available that you can add using *View → Customize Toolbar...*.

```{image} _images/Toolbar_Upload.png
:alt: Toolbar Upload
:width: 300px
```

## Using Drag & Drop

Note that dragging files is not limited to the *Finder.app*, but also works i.e. with attachments *Mail.app* or any other application supporting file promises.

### Drag to a Folder

Drag the file from the *Finder.app* or *Windows Explorer* to the [browser](browser.md) window to upload to the current working directory or the folder hovered over.

### Drag to a Bookmark

Upload files without first opening a connection to a server by dropping the file(s) onto a [bookmark](bookmarks.md) item in the bookmark source list.

### Local Disk Browser

You can browse your local hard disk within Cyberduck and drag files to the remote browser opened in another window or tab.

```{image} _images/Connection_Popup.png
:alt: Connection Popup
:width: 400px
```

### Drag to the Dock

```{admonition} macOS only
:class: tip

Drag files to the application icon in the `Dock` which will upload to the frontmost browser. A prompt is displayed to choose the bookmark to upload the files to (with the bookmark of the current browser selected by default if any).
```

```{image} _images/Bookmark_Upload_Selection.png
:alt: Bookmark Upload Selection
:width: 400px
```

## Using Copy & Paste

Copy a file in the *Finder.app* or *Explorer* with *Edit → Copy (macOS `⌘C` Windows `Ctrl+C`)* and paste it to a browser window in Cyberduck to upload with *Edit → Paste (macOS `⌘V` Windows `Ctrl+V`)*.

```{image} _images/Paste_Files.png
:alt: Paste Files
:width: 300px
```

## The Service Menu

````{admonition} macOS only
:class: tip

When selecting files in the *Finder* or another application with references to files and folders, choose the item *Services → Upload* (with the Cyberduck icon) in the application menu to launch Cyberduck and upload the items selected to the bookmark you choose. This action is also available in the context menu (right-click on files or folders) in the *Finder*.

```{image} _images/Services_Upload.png
:alt: Services Upload
:width: 300px
```
````

```{note}
Make sure in *System Preferences → Keyboard → Keyboard Shortcuts → Services → Files and Folders* the item *Upload with Cyberduck* is selected.
```

```{image} _images/Upload_from_Finder.png
:alt: Upload from Finder
:width: 600px
```

## Preferences

### Transfers → General → Uploads → Upload with temporary filename

An option to upload with a temporary name and rename the file after the transfer is complete. An upload that is not complete, will not be renamed. This is useful for uploading to watch folders, that should only pick up a file once the upload is complete. To specify a different temporary filename pattern, use the [hidden configuration option](preferences.md#hidden-configuration-options)

    defaults write ch.sudo.cyberduck queue.upload.file.temporary.format "'{0}-{1}'"

where `{0}` is the original filename and `{1}` is a random UUID. The default setting uses a temprary filename of `filename-uuid`.