Add Hidden Configuration Options to Mountain Duck and Cyberduck
===

:::{tip}
For Cyberduck CLI refer to [Preferences](../cli/index.md)
:::

:::{contents} Content
:depth: 2
:local:
:::

## Using `default.properties`

There are some settings which aren't yet available in the *Preferences* either because they are not considered stable
yet or not of general interest. For [Mountain Duck](../mountainduck/index.md) and [Cyberduck](../cyberduck/index.md) you
can add the property line in the format `property=value` to the `default.properties` file within
the [application support folder](../cyberduck/support.md#application-support-folder) on Windows and macOS.

1. Navigate into the [application support folder](../cyberduck/support.md#application-support-folder).
   :::{note}
   The application support folder is the same for Mountain Duck and Cyberduck.
   :::

2. Check for a file named `default.properties`
   :::{important}
   The file `default.properties` does not exist by default and must be created manually.
   :::
    - If it already exists, open it with the text editor of your choice, add the desired property line and save the
      file.
    - If the file does not exit, follow the remaining steps.
3. Open a text editor of your choice, for example, _TextEdit.app_ (macOS) or _Notepad.exe_ (Windows), and add the desired property
   line.
4. Save the file as a text file (txt) to
   the [application support folder](../cyberduck/support.md#application-support-folder) as `default.properties`.

   :::{attention}
   Avoid saving the file in any other format such as rich text format (RTF) when opening in _TextEdit_.
   :::

5. Make sure the filename is `default.properties` with no additional extension. In case you don't see the file
   extensions in the file explorer you can reveal them by following the instructions for your respective
   operating system.

   ::::{tabs}
   :::{group-tab} macOS
   
   You can reveal the file extensions for all files by ticking the checkmark `Show all filename extensions` within
   `Finder → Preferences → Advanced`. Alternatively, you can reveal the file extension for a specific file by opening
   the Finder info window on the wanted file and removing the checkmark `Hide extension` within the `Name & Extension`
   section.
   :::
   :::{group-tab} Windows
   1. Open the *Folder Options* window.
   2. Select the *View* tab.
   3. Deselect the `Hide extensions for known file types` checkbox under *Advanced Settings*
   4. Click on *Apply* and *OK*.
   
   You can also open the *Folder Options* window by searching for `File Explorer Options` within the *Start* search box.
   :::
   ::::
   
6. Restart Cyberduck and Mountain Duck.

## Using `Terminal.app`

:::::{admonition} macOS only
:class: note

::::{tabs}
:::{tab} Mountain Duck

Type the `defaults` command in the format below in a *Terminal.app* (in `\Applications\Utilities`) window and restart
Mountain Duck.

* Overwrite default preference with custom setting

```
defaults write io.mountainduck <property> <value>
```

* Revert to default setting

```
defaults delete io.mountainduck <property>
```

:::
:::{tab} Cyberduck

Type the `defaults` command in the format below in a *Terminal.app* (in `\Applications\Utilities`) window and restart
Cyberduck.

* Overwrite default preference with custom setting

```
defaults write ch.sudo.cyberduck <property> <value>
```

* Revert to default setting

```
defaults delete ch.sudo.cyberduck <property>
```

:::
::::
:::::


## In `.cyberduckprofile` Connection Profiles

You can override defaults in specific [connection profiles](../protocols/profiles/index.md) only affecting connections that use the profile. 

1. Open the `.cyberduckprofile` file in a text editor.
2. Add a child element to `<dict>` with a `key` named `Properties` and the configuration options inside an `array` as follows:

   ```{code-block}
   <key>Properties</key>
   <dict>
      <key>property</key>
      <string>value</string>
   </dict>
   ```
   
## In `.duck` Bookmark Files

You can override defaults in specific [bookmarks](../cyberduck/bookmarks.md) only affecting a single connection.

1. Open the `.duck` file in a text editor.
2. Add a child element to `<dict>` with a `key` named `Custom` and the configuration options inside an `dict` as follows:

   ```{code-block}
   <key>Custom</key>
   <dict>
      <key>property</key>
      <string>value</string>
   </dict>
   ```
