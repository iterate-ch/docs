Smart Synchronization History
===

# Sync Progress

The sync progress shows the files that currently get synchronized and pending changes after the current transfer.

```{image} _images/Sync_Progress.png
:alt: Send Command
:width: 800px
```

Shown for the current transfers are transfer rate, remaining data, and already transferred data. If Mountain Duck synchronizes files in a badge, the file state might differ from the state within the file browser. The sync progress display is limited to 5 entries.

## Reveal file

Selecting an item reveals the file in the Finder (macOS) or File Explorer (Windows).

# Recent Files

The *Recent Files* area shows the last 20 items that Mountain DUck uses for one of the following operations:

### Delete

```{image} _images/delete.png
:alt: Send Command
:width: 50px
```

A file or folder has been deleted either *by you* or *on the server*

### Create

```{image} _images/plus.png
:alt: Send Command
:width: 50px
```

A file or folder was created or updated *on the server*.

### Upload

```{image} _images/transfer_upload.png
:alt: Send Command
:width: 50px
```

A file or folder was added or changed and is uploaded to the server.

### Download

```{image} _images/transfer_download.png
:alt: Send Command
:width: 50px
```

A file or folder is downloaded to the local cache to be available for offline use. This state also occurs if a file that is marked as *Keep offline* has updated on the server.

### Error

```{image} _images/alert.png
:alt: Send Command
:width: 50px
```

The sync operation failed for the file.

```{image} _images/Recent_Files.png
:alt: Send Command
:width: 600px
```

A file may show up with an error state indicating an issue while synchronizing. Further details are available through the [sync option menu item](Sync#sync-errors).

## Application display

```{admonition} Windows Only
:class: tip

The application that was used for editing the file is displayed within the *Recent Files* area.
```

## Reveal file

Selecting an item in the *Recent Files* section reveals the file in the Finder (macOS) of File Explorer (Windows).

## Clear menu

Clear out all entries of the list by clicking on the *Clear Menu* button at the bottom of the menu.