Edit Files
===

# How to edit a file in an external editor

You can edit a file just as a local file by clicking the Edit toolbar button or by choosing *File → Edith With*. The file will be downloaded to a temporary directory and opened with the preferred editor. Set your preferred editor in *Preferences*. The file will be uploaded to the server every time you choose *File → Save* in the Editor application. The file is not changed on the server if you just close the document without saving it or if the content has not changed.

# Which editor for what files

`````{tabs}
````{group-tab} macOS

The default editor of a file is selected using the default application for a given file typeset. If the default application is not one of the supported editors, the editor chosen in the Preferences is used instead.

```{image} _images/Edit_With_Application.png
:alt: Send Command
:width: 700px
```
<br/>
<br/>

To edit file type associations choose *File → Info* for a given file type in the *Finder.app*.

````
````{group-tab} Windows

The default editor of a file is selected using the default application for a given file typeset. If the default application is not one of the supported editors, the editor chosen in the Preferences is used instead.

```{image} _images/Edit_With_Application.png
:alt: Send Command
:width: 700px
```
<br/>
<br/>

To edit file type associations choose *File → Info* for a given file type in the *Finder.app*.

````
`````

# Preferences

Select *Always use default editor* in *Preferences → Editor* if you always want to use the default editor set regardless of the file type.

```{image} _images/Editor_Preferences.png
:alt: Send Command
:width: 500px
```

# Hidden Preferences

## Disable upload of temporary file on save

A [hidden configuration option](Preferences#hidden-configuration-options).

`defaults write ch.sudo.cyberduck editor.upload.temporary false`

# Problems

## No external editor available

```{admonition} macOS X only
:class: tip

If the editor does not show up as a choice in *File → Edit With* (the only submenu item is *No external editor available*), you may have to rebuild the `LaunchServices`database of OS X using Terminal.app:

`/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister \ -kill -r -domain local -domain system -domain user`

```