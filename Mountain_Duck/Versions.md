File Versions
===

Mountain Duck supports opening and reverting previous versions of files. You can get a list of previous versions by right-clicking on a file in *Finder* on macOS or *File Explorer* on Windows and choosing *Versions*.

# Supported Providers

Support is currently limited to connections to [Amazon S3](../Protocols/S3/index.md) with buckets that have versioning enabled.

## Amazon S3

### Enable Versioning

Versioning can be enabled per bucket in by choosing *Info → S3* in *Finder* on macOS or *File Explorer* on Windows. Alternatively, enable versioning in AWS Console or [Cyberduck](../Cyberduck/index.md).

## Quick Look

You can open a previous version of a file by choosing *Versions → ... → Quick Look*. This will open a *Quick Look preview* on macOS or open the previous version of the file in the defailt application on Windows.

```{image} _images/Revert_File_Context_Menu_Option_Windows.png
:alt: Send Command
:width: 900px
```

## Revert

You can revert to a previous version of a file by choosing *Versions → ... → Revert*. Wait for the *File Updated* notification which notifies the previous version has been restored.

```{image} _images/File_Updated_Notification_Windows.png
:alt: Send Command
:width: 400px
```