Integrated
====

```{toctree}
:hidden:
:titlesonly:
```

```{image} ../_images/Disk_Syncing.png
:alt: Disk Syncing
:width: 200px
```

> Local storage is managed by the operating system. The mount is not seen as a remote volume by applications but as a regular folder on disk. This option uses the tightly integrated _File Provider_ (macOS) and _Cloud Files_ (Windows) APIs. Directories can be browsed when offline and files opened are made available for later offline access. You can choose to make selected files and folders available for offline use. Changes to files are uploaded in the background as soon as a connection is available.

```{tip}
You can access files in _Integrated_ connect mode without being always connected the server or cloud storage.
```


## Status of Files

Files and folders on a mounted volume have a status icon overlay in _File Explorer_ (Windows) and _Finder_ (macOS).

```{admonition} macOS only
:class: tip
Please make sure to enable the Mountain Duck [Integration](../installation/index.md) in *System Preferences → Extensions → Finder* on macOS. For macOS Ventura and later, the setting can be found in *System Settings → Privacy & Security → Extensions → Added Extensions*.
```
`````{tabs}
````{group-tab} macOS

An additional icon next to the filename is displayed in Finder denoting the synchronization status in _Integrated_ connect mode.

 - ![](../_images/File_Provider_Online_Only.png) **Online Only**
 - ![](../_images/File_Provider_Ignored.png) **Ignored**
 - ![](../_images/File_Provider_Error.png) **Sync Error**


````
````{group-tab} Windows


````
`````

## Sync Progress

Changes to files are uploaded in the background as soon as a connection is available. Progress is reported by animating the status bar icon and a menu item titled *Sync in Progress*.

```{admonition} macOS only
:class: tip
Progress is shown when downloading or uploading a file with a progress bar over the file icon or circular progress indicator adjacent the filename.
```

### Keep Offline

Choose *Mountain Duck → Keep Offline on Local Disk* to make files and folders available offline. The status of the file will change to *In Sync*. The action is recursive for all contained files when a folder is selected and applies to new files found on the remote storage.

```{admonition} macOS only
:class: tip

Choose _Download Now_ when using _Integrated_ connect mode to download the file but allow it to be removed from cache on low disk space. 
```


### Delete on Local Disk

Choose *Mountain Duck → Delete on Local Disk* to delete the offline copy. The status of the file will change to *Online Only*. The action is recursive for all contained files when a folder is selected and allows you to quickly free up space used in the cache on your local disk.

```{admonition} macOS only
:class: tip

Choose _Remove Download_ instead when using _Integrated_ connect mode.
```

