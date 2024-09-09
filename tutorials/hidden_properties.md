Add Hidden Configuration Options to Mountain Duck and Cyberduck
===

:::{tip}
For Cyberduck CLI refer to [Preferences](../cli/index.md)
:::

There are some settings which aren't yet available in the *Preferences* either because they are not considered stable yet or not of general interest. 

For [Mountain Duck](../mountainduck/index.md) and [Cyberduck](../cyberduck/index.md) you can add the property line in the format `property=value` to the `default.properties` file within the [application support folder](../cyberduck/support.md#application-support-folder) on Windows and macOS.

:::{important}
You'll have to create the `default.properties` file manually if it isn't present yet!
:::

## Step-by-Step Instructions
1. Quit Mountain Duck/Cyberduck
2. Navigate into the [application support folder](../cyberduck/support.md#application-support-folder). 
    
    :::{note}
    The application support folder is the same for Mountain Duck and Cyberduck.
    :::

3. Check if there is a `default.properties` file available
    - If it is available, open it within a text editor of your choice, add the desired property line and save the file.
    - If the file isn't available, follow the remaining steps.
4. Open a text editor of your choice, for example, TextEdit (macOS) or Notepad (Windows), and add the desired property line.
5. Save the file as a text file (txt) into the [application support folder](../cyberduck/support.md#application-support-folder).

    :::{attention}
    Avoid saving the file within the rich text format (rtf), as this causes Mountain Duck/Cyberduck to not recognize the property file after changing the file extension.
    :::

6. Close the text editor.
7. Replace the file name **and** extension with `default.properties`.
8. Confirm that you want to change the file extension if your operating system warns you about it.

In case you don't see the file extensions you can reveal them by following the instructions for your respective operating system.

::::{tabs}
:::{tab} macOS

You can reveal the file extensions for all files by ticking the checkmark `Show all filename extensions` within `Finder → Preferences → Advanced`. 

Alternatively, you can reveal the file extension for a specific file by opening the Finder info window on the wanted file and removing the checkmark `Hide extension` within the `Name & Extension` section.

:::
:::{tab} Windows

1. Open the *Folder Options* window.
2. Select the *View* tab.
3. Deselect the `Hide extensions for known file types` checkbox under *Advanced Settings*
4. Click on *Apply* and *OK*.

You can also open the *Folder Options* window by searching for `File Explorer Options` within the *Start* search box.

:::
::::

## Activate Hidden Configuration Options Through `Terminal.app`

:::::{admonition} macOS only
:class: note

::::{tabs}
:::{tab} Mountain Duck

Type the `defaults` command in the format below in a *Terminal.app* (in `\Applications\Utilities`) window and restart Mountain Duck.

```
defaults write io.mountainduck <property> <value>
```

:::
:::{tab} Cyberduck

Type the `defaults` command in the format below in a *Terminal.app* (in `\Applications\Utilities`) window and restart Cyberduck.

```
defaults write ch.sudo.cyberduck <property> <value>
```

:::
::::
:::::