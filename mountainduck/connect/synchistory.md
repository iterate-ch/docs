Smart Synchronization History
====

## Sync Progress

The sync progress shows the files that currently get synchronized and pending changes after the current transfer.

```{image} ../_images/Sync_Progress.png
:alt: Sync Progress
:width: 800px
```

Shown for the current transfers are transfer rate, remaining data, and already transferred data. If Mountain Duck synchronizes files in a badge, the file state might differ from the state within the file browser. The sync progress display is limited to 5 entries.

### Reveal file

Selecting an item reveals the file in the Finder (macOS) or File Explorer (Windows).

## Recent Files

The *Recent Files* area shows the last 20 changes to files by you or on the server:
```{image} ../_images/Recent_Files.png
:alt: Recent Files
:width: 600px
```

### File Changes
#### ![Delete](../_images/delete.png) Delete
A file or folder has been deleted either *by you* or *on the server*

#### ![Create](../_images/plus.png) Create
A file or folder was created or updated *on the server*.

#### ![Upload](../_images/transfer_upload.png) Upload
A file or folder was added or changed *by you* and uploaded to the server.

#### ![Download](../_images/transfer_download.png) Download
A file is downloaded to the local cache to be available for offline use. This state also occurs if a file that is marked as *Keep offline* has updated on the server.

#### ![Error](../_images/alert.png) Error
The sync operation failed for the file. A file may show up with an error state indicating an issue while synchronizing. Further details are available through the [sync option menu item](index.md#sync-errors).

### Application Display

```{admonition} Windows Only
:class: tip

The application that was used for editing the file is displayed within the *Recent Files* area.
```

### Reveal file

Selecting an item in the *Recent Files* section reveals the file in the Finder (macOS) of File Explorer (Windows).

### Clear Menu

Clear out all entries of the list by clicking on the *Clear Menu* button at the bottom of the menu.