Online
===

```{toctree}
:hidden:
:titlesonly:
```

> In _Online_ connect mode, changes to a file are immediately uploaded and in sync when an application has finished saving a file. Files are accessed on demand from the remote when opened and do not take up any local disk space. Files are not synchronized on local disk but only saved temporarily when required and deleted at the latest when the bookmark is disconnected. 

```{tip}
You can only access volumes in _Online_ connect mode when a connection is possible to the server or cloud storage.
```

```{contents} Content
:depth: 1
:local:
```

## Status of Files

Files and folders on a mounted volume have a status icon overlay in _File Explorer_ (Windows) and _Finder_ (macOS).

```{admonition} macOS only
:class: tip
Please make sure to enable the Mountain Duck [Integration](../installation/index.md) in *System Preferences → Extensions → Finder* on macOS. For macOS Ventura and later, the setting can be found in *System Settings → Privacy & Security → Extensions → Added Extensions*.
```

### ![](../_images/overlay_infinite.png) Online Only
The file can only be opened when a connection to the server or cloud storage can be made. The file does not take any space on your computer. The file is downloaded on demand when you open it.

### ![](../_images/overlay_ignored.png) Ignored
The file or folder is only saved in a local [temporary](../issues/index.md#temporary-files) location and not uploaded. This includes files matching a [temporary filename pattern](../issues/index.md#filenames), empty files and new folders.


## Transfer progress

While transferring files and folders, a transfer [progress](../interface.md#copying-files) window shows in _Finder.app_ or _Windows Explorer_. When completed, the file(s) have been uploaded to the server.


## Notifications

Notifications can be posted for the following events:
- **Filesystem mounted**. The volume is now connected.
- **Filesystem unmounted**. The volume has been disconnected.
- **Download complete**. File download completed in the background.
- **Upload complete**. File upload completed in the background.


You can adjust which notifications you want to receive in [*Preferences → Notifications*](../preferences.md#notifications).

## Connectivity Issues

Server-side issues like general network problems, quota mismatches, or authentication failures will cause the mounted volume to be disconnected. If enabled in *Preferences → Connection → Confirm disconnect* a disconnect prompt is shown.

### Auto Unmount on Connection Error

To disable the unmount upon failure use a [hidden configuration option](../preferences.md#hidden-configuration-options) `unmount.auto=false`.
