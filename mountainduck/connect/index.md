Connect mode
===

```{toctree}
:hidden:
:titlesonly:
sync
online
```

When connecting to a server, you can choose between *[Online](online.md)* and *[Smart Synchronization](sync.md)* connect
mode.

```{admonition} Online
In _Online_ connect mode, changes to a file are immediately uploaded and in sync when an application has finished saving a file.
```

```{admonition} Smart Synchronization
In _Smart Synchronization_ connect mode, files are copied to a local cache for faster access prior synchronization with the server in the background.
```

## Feature Comparison

|                         | **Online**                                | **Smart Synchronization**                                                       |
|-------------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| **Offline Access**      | -                                         | Save files in the sync cache for file access once the internet connection drops |
| **Lock Files**          | Depending on the protocol in use          | Depending on the protocol in use                                                |
| **Index Files**         | -                                         | Index the files in folders you open for faster access                           |
| **Buffering**           | Temporary save opened files faster access | -                                                                               |
| **Background Sync**     | -                                         | Synchronize changes between cloud and local cache automatically                 |
| **Transfer Window**     | Popup during activ transfers              | -                                                                               |
| **Recent File History** | -                                         | Available in the dropdown menu                                                  |
| **Caching**             | Temporary caching in th system temp cache | Cache files in the sync cache for offline Access                                |	