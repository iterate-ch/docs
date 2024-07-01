Edit Files
====

You can edit a file just as a local file in an external editor by clicking the Edit toolbar button or by choosing *File → Edit With*. The file will be downloaded to a temporary directory and opened with the preferred editor. The file will be uploaded to the server every time you choose *File → Save* in the Editor application. The file is not changed on the server if you just close the document without saving it or if the content has not changed.

## Default Editor
The default editor opened for a file is selected depending on the file type. If no application is found to handle the file type the default eidtor chosen in *Preferences* is used instead.

```{image} _images/Edit_With_Application.png
:alt: Edit with Application
:width: 700px
```

```{admonition} macOS only
:class: tip
To edit file type associations choose *File → Info* for a given file type in the *Finder.app*.
```
```{admonition} Windows only
:class: tip
To edit file type associations choose *Properties → General → Type of file → Change…* for a given file type in Windows Explorer.
```

## Preferences

Set your preferred editor in *Preferences*. Select *Always use default editor* in *Preferences → Editor* if you always want to use the default editor set regardless of the file type.

```{image} _images/Editor_Preferences.png
:alt: Editor Preferences
:width: 700px
```

## Versioning

```{important}
Cyberduck [9.0](https://cyberduck.io/changelog/) or later required
```

Enable the custom versioning option in *Preferences → Editor* to store previous versions of a file. The versions can be previewed, deleted or restored in *Edit → Info → Versions*.

The versions are stored in a hidden folder named `.duckversions` in each folder on the mount. The versions are named like the following pattern: `filename.extension → filename-20230906102017.762.extension`

### Versions while transferring

Enable versioning for [overwriting](transfer.md#overwrite-prompt) existing files by using a [hidden configuration option](preferences.md#hidden-configuration-options).

    versioning.enable=true

### Exclude files

Files can be excluded from versioning by using a [hidden configuration option](preferences.md#hidden-configuration-options).

    versioning.include.regex=.*

### Number of saved versions

Per default, the number of saved versions is limited to 5. The oldest version will be deleted once a new version is uploaded exceeding the limit.

The number of saved versions can be customized by using a [hidden configuration option](preferences.md#hidden-configuration-options).

    versioning.limit=5

## Hidden Preferences

### Disable Upload of Temporary File on Save

A [hidden configuration option](preferences.md#hidden-configuration-options).

    defaults write ch.sudo.cyberduck editor.upload.temporary false

## Problems

### No External Editor Available

```{admonition} macOS only
:class: tip

If the editor does not show up as a choice in *File → Edit With* (the only submenu item is *No external editor available*), you may have to rebuild the `LaunchServices`database of OS X using Terminal.app:

`/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister \ -kill -r -domain local -domain system -domain user`

```