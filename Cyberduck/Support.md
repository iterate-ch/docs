Support
===

# Application Support Folder

Inside the application support folder, the application saves files needed for their operations e.g. settings, log data, history files, etc.

`````{tabs}
````{group-tab} macOS

You can reach the application support folder by choosing `Go → Go to folder` within the *Finder* menu, copying the path below into the appearing window, and clicking on the *Open* button afterward.

`~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/`

````
````{group-tab} Windows

You can reach the application support folder by navigating to `%AppData%\Cyberduck` by copying the path into the address bar of the Explorer and press *Return* afterward.

````
`````

# Bug Reports and Feature Requests

[Open a new ticket]() using the issue tracker with a description of what you have done and what went wrong or describing the missing functionality in detail. Make sure to look or search for existing tickets first.

## Logging Output

```````{tabs}
``````{group-tab} macOS

`````{tabs}
````{tab} Log

**Cyberduck 7.9 or later required.**<br/>
Log output can be found in the `cyberduck.log` file in `~/Library/Logs/Cyberduck`. You can easily reach this file in *Console.app* (Open from `/Applications/Utilities`) under `Reports → Log Reports → cyberduck.log`.

````
````{tab} Console.app

Additionally, log output can be found in *Console.app* (Open from `/Applications/Utilities`).

- **macOS 10.8 or later:** Log output can be found in the `system.log`.
- **macOS 10.12 or later & Cyberduck 7.2 or later:** Log output can be found in *Console.app* under *Devices*. When requested, enable info and debug messages from *Action → Include Info Messages* and *Action → Include Debug Messages* respectively. Filter output by pasting `Cyberduck`in the search input field in the toolbar of the window and choose *Process* in the small dropdown menu. Choose *Edit → Select All and Edit → Copy* to copy the output to the clipboard.

```{image} _images/Console.app.png
:alt: Send Command
:width: 600px  
```

Alternatively, if you are familiar with *Terminal.app* you can get the current log output streamed while using Cyberduck with

`log stream --predicate '(process =="Cyberduck")' --level info`

You can filter for the connection transcript only by using

`log stream --predicate '(process =="Cyberduck") && (category == "transcript")' --level info`

```{image} _images/Cyberduck_Transcript.png
:alt: Send Command
:width: 600px
```

Alternatively, to show previous log events use

`log show --predicate '(process =="Cyberduck")' --info`

````
`````

**Transcript**<br/>
You can only access the transcript which will log protocol request and responses. It's particular useful for protocols using HTTP. Open a *Terminal.app* window and enter 

`log stream --predicate '(process == "Cyberduck") && (category == "transcript")' --level info`

**Debug Log**<br/>
To enable debug logging open a *Terminal.app* window and enter

`defaults write ~/Library/Preferences/ch.sudo.cyberduck.plist logging debug`

Reset the logging configuration with

`defaults delete ~/Library/Preferences/ch.sudo.cyberduck.plist logging`

Restart Cyberduck for any logging configuration change to take effect.


**Heap Dump**<br/>
To create a heap dump of the Cyberduck process on macOS (in case of excessive memory usage for example) you can use `jmap` from the {download}`OpenJDK 13<https://github.com/AdoptOpenJDK/openjdk13-binaries/releases/download/jdk-13.0.2%2B8/OpenJDK13U-jdk_x64_mac_hotspot_13.0.2_8.pkg>`.

`jmap -dump:file=cyberduck-dump.hprof [PID of Cyberduck process]`

``````
``````{group-tab} Windows

Log output can be found in the `cyberduck.log` file in `%AppData%\cyberduck`.


**Debug Log**<br/>
Debug logging can be enabled with a [hidden setting](Preferences#hidden-configuration-options). As there is no user interface for this yet you need to add the setting manually. If not existing yet you have to create the file [`%AppData%\Cyberduck\default.properties`](FAQ#preferences-and-application-support-files-location) and then add the property as follows:

`logging=debug`

``````
```````

## Feature Requests

If you have a feature request please make sure to include a detailed and comprehensible description of the requested function in [the ticket](). Make sure to check if someone already requested a similar feature.

# Crash Reports

`````{tabs}
````{group-tab} macOS

Crash reports are saved to `~/Library/Logs/DiagnosticReports/Cyberduck_*.crash`.

````
````{group-tab} Windows

Crash reports are saved to `%AppData%\cyberduck\CrashReporter`.

````
`````

# Get Support

For issues with your remote storage user account credentials, please instead write to your hosting service provider. For bug reports or a feature request you can [open a ticket]() in our public issue tracker. Discuss features and issues you are having in the [Cyberduck Google Group](http://groups.google.com/group/cyberduck).