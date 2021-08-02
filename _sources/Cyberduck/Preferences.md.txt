Preferences
===

In general, user adjustable preferences are discussed in the context of the topic in all wiki pages.

# Language

Choose the language of the user interface. It defaults to the system language when set to *Default*. Thirty localizations are included.

- On macOS, the first matching language is chosen according to the *Languages* list in System *Preferences → International*. To change your preferred language for all applications, change the order there.

```{image} _images/Language_Preference.png
:alt: Send Command
:width: 500px
```

# Update

An auto update feature will alert you when a new version is available and self update the application. Choose *Preferences → Update → Automatically check for updates*. You can also get the latest builds by [manual download](https://update.cyberduck.io/nightly/).

## Snapshot Builds

Snapshot builds include the latest changes and are published regularly. These builds are not tested.

```{image} _images/Update.png
:alt: Send Command
:width: 500px
```

## Beta Builds

Beta builds are published before a release and include the latest features and have been tested but haven't release quality yet.

# Hidden configuration options

There are some settings which aren't yet available in the *Preferences* either because they are not considered stable yet or not of general interest. Follow these steps to enable a hidden preference referenced in the wiki:

`````{tabs}
````{group-tab} macOS

Type the `defaults` command given in a *Terminal.app* (in `/Applications/Utilities`) window and restart Cyberduck.

`defaults write ~/Library/Preferences/ch.sudo.cyberduck.plist <property> <value>`

Alternatively you can create a file `default.properties` in the [application support folder](FAQ#Wherearepreferencesandapplicationsettingssavedto). Add the setting as follows:

`...`<br/>
`<property>=<value>`<br/>
`...`

````
````{group-tab} Windows

If not existing yet you need to create the file [%AppData%](FAQ#Wherearepreferencesandapplicationsettingssavedto)`\Cyberduck\default.properties`. To do that create a new text file within `%AppData%\Cyberduck` and replace the preconfigured name including the file extension by *default.properties*.

Add the setting as follows:

`...`<br/>
`<property>=<value>`<br/>
`...`
````
````{group-tab} CLI

Refer to [Preferences](../CLI/index#Preferences)
````
`````