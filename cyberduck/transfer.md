File Transfers
====

```{contents} Content
:depth: 2
:local:
```

The *Transfers* window lists pending and completed transfers. The list is retained when the application is closed and can be retrieved after restarting so that the transfer can be restarted at a later time.

- [Download](download.md)
- [Upload](upload.md)
- [Synchronize Folders](sync.md)
- [Copy between Servers](copy.md)

## Resume and Reload

*Resume* will try to finish a transfer previously interrupted.

```{note}
Some servers may not support resumable transfers and the file will be reloaded instead.
```

```{image} _images/Transfers.png
:alt: Transfers
:width: 700px
```

## Interrupt

You can interrupt a transfer using the *Stop* toolbar button.

## Open downloaded files

Use the *Open* toolbar button to open a downloaded file or folder.

```{admonition} macOS only
:class: tip

A warning might be displayed before opening the file. See the [download quarantine](download.md#quarantine).
```

## Show Downloaded Files

Using the *Show in Finder* or *Show* toolbar button, files are shown in *Finder.app* or *Explorer*.

## Progress

````{admonition} Windows only
:class: tip

If the *Transfers* window is closed, progress is also visible in the application icon in the Taskbar.

```{image} _images/Transfer_Progress.png
:alt: Transfer Progress
:width: 100px
```
````

## Bandwidth

Limit the maximum bandwidth that is allowed for transfers. Useful when you don't want transfers to take all the bandwidth available on your internet connection that would slow down other connections. 

`````{tabs}
````{group-tab} macOS

Select *Bandwidth* from the toolbar in the transfer window and set the maximum bandwidth allowed by the selected transfer from the drop-down window. The default setting is configurable in the [Preferences](preferences.md).

````
````{group-tab} Windows

Use the drop-down menu in the lower right of the transfer window to set the maximum bandwidth allowed by the selected transfer. The default setting is configurable in the [Preferences](preferences.md).

````
`````

## Connections

You can choose to use single or multiple connections for file transfers. Choose *Preferences → Transfers → Transfer Files* to set the default or for a bookmark in *Bookmark → Edit Bookmark → Transfer Files*.

**Use browser connection:** Use the browser connection to transfer files.<br/>
**Open single connection:** Use a single connection additionally to the browser connection to transfer files from a transfer sequentially.<br/>
**Open multiple connections:** Use multiple connections to transfer files from a transfer concurrently.

```{image} _images/Transfer_Options.png
:alt: Transfer Options
:width: 300px
```

### Limit Number of Parallel Connections

The maximum number of connections for transfers using multiple connections can be limited using the toggle in the lower right of the *transfer window* on Windows or the *toolbar dropdown* on macOS.

```{image} _images/Limit_Connections.png
:alt: Limit Connections
:width: 500px
```

The setting limits
* The number of parallel transfers in progress the _Transfers_ window. Transfers awaiting will show _Maximum allowed connections exceeded. Waiting…_.
* The number of connections used to download multiple parts using [segmented downloads](download.md#segmented-downloads).
* The number of connections used when downloading or uploading multiple files in a transfer with the option _Use multiple connections_.

## Overwrite Prompt

A prompt is displayed if files already exist at the target location (on your local hard disk for downloads or on the server for uploads) and you have selected *Prompt* in *Transfers → General → Downloads/Uploads → Existing Files*. The prompt allows choosing the action for existing files. You can exclude selected files and folders from the transfer action by unchecking the checkbox next to it. If the checkbox is not selected, these files will be skipped.

```{image} _images/Overwrite_Prompt.png
:alt: Overwrite Prompt
:width: 700px
```

**Exclamation mark triangle:** File size is zero or differs from the existing file.

### Overwrite

Replace any existing file restarting the transfer from scratch. Existing files are moved to the trash.

```{image} _images/Overwrite_Options.png
:alt: Overwrite Options
:width: 600px
```

### Compare

Skip existing files that match a checksum if available. If a checksum is not available or differs the modification date is compared to determine if a file should be replaced.

### Resume

Append to existing files and skip files that match the file size and checksum if available. The following protocols support resume for uploads:

- [FTP](../protocols/ftp.md)
- [SFTP](../protocols/sftp/index.md)
- [WebDAV](../protocols/webdav/index.md)
- [S3](../protocols/s3/index.md) (for multipart uploads)

The following protocols support resume for downloads:

- [FTP](../protocols/ftp.md)
- [SFTP](../protocols/sftp/index.md)
- [WebDAV](../protocols/webdav/index.md)
- [S3](../protocols/s3/index.md)
- [Openstack](../protocols/openstack/index.md)

### Rename

Rename transferred file appending a timestamp to the filename.

### Rename Existing

Rename existing file at the destination appending a timestamp to the filename.

### Skip 

Skip transfer of files that already exist.

## Preferences

### Browser connection for file transfers

If your server only allows one single connection to be opened for a given user, you'll have to transfer files using the browser connection. This will cause you to stop browsing files and folders while the transfer is in progress. You can choose to *Use the browser connection* or to a *Open a new connection* for file transfers in the [bookmark](bookmarks.md#edit-bookmark) setting. The default setting is configurable in the *Transfers* tab of [Preferences](preferences.md).

### Download/Upload setting for Existing Files

- **Prompt:** Asks what action to take for each transfer.
- **Overwrite:** Overwrite existing files at the destination.
- **Resume:** Skip existing files with the same file size and append if file size differs.
- **Rename:** Rename transferred file appending a timestamp to the filename.
- **Rename existing:** Rename existing file at the destination appending a timestamp to the filename.
- **Skip:** Skip all existing files.

### Transfers → Filter

Files and folders matching the regular expression in *Preferences → Preferences → Advanced* will be excluded. Standard PERL regular expressions are used, see Google for more help. The most important qualifiers are:

`.		Any character`<br/>
`\d		A digit: [0-9]`<br/>
`\D		A non-digit: [^0-9]`<br/>
`\s		A whitespace character: [ \t\n\x0B\f\r]`<br/>
`\S		A non-whitespace character: [^\s]`<br/>
`\w		A word character: [a-zA-Z_0-9]`<br/>
`\W		A non-word character: [^\w]`<br/>
`XY		X followed by Y`<br/>
`X|Y		Either X or Y`<br/>
`X?		X, once or not at all`<br/>
`X*		X, zero or more times`<br/>
`X+		X, one or more times`

The default pattern excludes metadata files from common revision control software.

`.*~\..*|\.DS_Store|\.svn|CVS`

### Transfers → General → Transfers

Files can be transferred using either the connection from the browser or by opening a new dedicated transfer connection. Using the setting *Open new connection* will add files to be transferred to the *Transfer* Window and open a new connection to the server to initiate the transfer. The option *Use browser connection* will transfer files using the connection from the browser. The file transfer is only reported at the bottom of the browser window without any detailed progress indicator. The transferred files will not get added to the *Transfer* Window. This setting is a also available per [bookmark](bookmarks.md).

Manage the behavior of the *Transfer* Window during active transfers and decide if you want to delete the file once the transfer is complete.

### Transfers → General → Downloads

Downloads can be performed in segments to increase the download speed. Segmented downloads requires server sided support for concurrent connections as the parts will be downloaded simultaneously. Once all segments are downloaded the parts will be merged to the actual file. Note that only the actual file is usable.

Additionally, you can choose the default directory to save the downloads to and decide if you always want to open the files after the download is finished.

### Transfers → Permissions → Downloads

Choose between a default permission mask to apply to downloaded files or to apply the same mask the file has on the server. If unchecked, downloaded files have the default mask for new files created on the local filesystem.

### Transfers → Permissions → Uploads

Adjust the permission mask of uploaded files or leave it to the default mask chosen by the server. The setting for permissions apply when connected to a UNIX host using [FTP](../protocols/ftp.md) or [SFTP](../protocols/sftp/index.md). When connected to [S3](../protocols/s3/index.md) and [Azure](../protocols/azure.md) this will update the access control list (ACL).

```{note}
Enabling change of permissions slows down the transfer rate when uploading many files with [FTP](../protocols/ftp.md).
```

### Transfers → Timestamps

Preserve modification date when uploading or downloading files. For [synchronization](sync.md) to work, these options must be enabled.

```{note}
Enabling change of modification date slows down the transfer rate when uploading many files with [FTP](../protocols/ftp.md).
```

## Hidden Preferences

### Bandwidth Throttle Options

A [hidden configuration option](preferences.md#hidden-configuration-options). Edit the available options (in bytes).

    defaults write ch.sudo.cyberduck queue.bandwidth.options 102400,1073741824

### Badge Dock Icon

A [hidden configuration option](preferences.md#hidden-configuration-options). Add a badge with the number of currently running transfers to the dock icon.

    defaults write ch.sudo.cyberduck queue.dock.badge true

### Prioritize Files in Transfers

A [hidden configuration option](preferences.md#hidden-configuration-options). Use `queue.upload.priority.regex` and `queue.download.priority.regex` to determine order of files transferred in folders. For example:

    defaults write ch.sudo.cyberduck queue.upload.priority.regex ".*\.html"

will prioritize files ending with `.html` and transfer before any other files in a folder.