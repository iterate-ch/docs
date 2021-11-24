Download
===

See also [Transfers](transfer.md) in general.

# Segmented Downloads

Increase the download speed by enabling the segmented downloads option within *Preferences → Transfers → General → Downloads → Segmented download with multiple connections for file*. Files larger that `100MB` will be split into segments and downloaded over multiple connections.

The segments will be merged automatically after all parts are downloaded. Merging the segments may take a considerable amount of time.

```{note}
The segments can only be merged successfully if all parts are downloaded. If some parts are missing the downloaded segments are saved within a folder and the file can't be restored unless you redownload the file or try to _Resume_ the failed transfer.
```

# Double-Click

Double click a file in the browser window to download to the default download location as configured in *Cyberduck → Preferences → Transfers*.

# Download Using Drag and Drop

Drag the files or folders to the desired download location in the *Finder.app* or *Explorer*.

# Toolbar Button

Customize the browser toolbar using menu *View → Customize Toolbar...* to add the *Download* toolbar button to the default configuration.

```{image} _images/Download_Toolbar_Button.png
:alt: Send Command
:width: 500px
```

# The Download Menu

Select *File → Download* or right-click the file in the browser to select *Download* in the context menu. If you are not connected to a server in a browser you can still choose *File → New Download* if you know the exact URL of the file or folder.

# Queue a File to be Downloaded Later

Drag the file from the browser to the *Transfers* window to be downloaded later.

# Where From 

```{admonition} macOS only
:class: note

Downloaded files have added metadata of its origin URL. *Finder.app* displays this information in *File → Get Info*.
```

# Hidden Preferences

## Quarantine

```{admonition} macOS only
:class: note

Downloaded files are flagged with the `com.apple.quarantine` attribute. The attributes associate basic information with the file, such as its type, when it was received, and the URL from which it came. When the Finder or any other program uses Launch Services to open a quarantined file, Launch Services inspects the file to see if it appears to be an application, script, or other executable file types. If so, the system displays an alert informing the user that the file is an application and asking for confirmation that it should be executed. The alert lets the user open the URL from which the file was downloaded, launch the program, or cancel. If the user proceeds to open the file, Launch Services removes the quarantine attributes from that file.

A [hidden configuration option](preferences.md#hidden-configuration-options).

`defaults write ch.sudo.cyberduck queue.download.quarantine false`

Files downloaded to edit do not have a quarantine flag set by default.
```

## Temporary Document Icon

Don't change the document icon while downloading. A [hidden configuration option](preferences.md#hidden-configuration-options).

`defaults write ch.sudo.cyberduck queue.download.icon.update false`