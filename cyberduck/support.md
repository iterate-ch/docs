Support
====

## Get Support

### Feature Requests

If you have a feature request please make sure to include a detailed and comprehensible description of the requested feature in [the ticket](https://github.com/iterate-ch/cyberduck/issues/new/choose). Make sure to check if someone already requested a similar feature.

```{warning}
For issues with your remote storage user account credentials, please instead write to your hosting service provider. 
```

### Bug Reports

[Open a new ticket](https://github.com/iterate-ch/cyberduck/issues/new/choose) with a description of what you have done and what went wrong. Make sure to look or search for existing issues first. If you have trouble connecting to a server or your login credentials are not valid, try to resolve the issue with the assistance of your hosting service provider.

```{note}
Discuss features and issues you are having in the [Cyberduck Google Group](https://github.com/iterate-ch/cyberduck/discussions). For issues with the registration key, please send an mail to [support@cyberduck.io](mailto:support@cyberduck.io).
```

```{warning}
Please be aware that you are possibly using our software at no charge if you have not purchased a registration key. Thus the support provided here is best effort only.
```

## Logging Output

`````{tabs}
````{group-tab} macOS

Log output can be found in the `cyberduck.log` file in`~/Library/Logs/Cyberduck`. You can also reveal the file by clicking on the _Show_ button within the Cyberduck preferences _Connection_ tab.

Alternatively, you can find `cyberduck.log` in *Console.app* (Open from `/Applications/Utilities`) under `Reports → Log Reports → cyberduck.log`.

```{image} _images/Console.app.png
:alt: Console.app
:width: 600px  
```

````
````{group-tab} Windows

Log output can be found in the `cyberduck.log` file in `%AppData%\cyberduck`. You can also reveal the file by clicking on the *Show* button within the Mountain Duck *Preferences Connection* tab. The file is named *cyberduck.log*.

````
`````

### Debug Log

To enable debug logging tick the corresponding checkmark in the Cyberduck *Preferences Connection* tab. You can reach the logging output by clicking on the *Show* button within the same Cyberduck *Preferences* section. The file is called *cyberduck.log*.

Alternatively this can be configured using the following command line options.

````{tabs}
```{group-tab} macOS

To enable debug logging open a *Terminal.app* window and enter

    defaults write ~/Library/Preferences/ch.sudo.cyberduck.plist logging debug

Reset the logging configuration with

`defaults delete ~/Library/Preferences/ch.sudo.cyberduck.plist logging`

Restart Cyberduck for any logging configuration change to take effect.

```
```{group-tab} Windows

Debug logging can be enabled with a [hidden setting](preferences.md#hidden-configuration-options). As there is no user interface for this yet you need to add the setting manually. If not existing yet you have to create the file [`%AppData%\Cyberduck\default.properties`](faq.md#preferences-and-application-support-files-location) and then add the property as follows:

`logging=debug`

```
````

### Additional Log Outputs

`````{tabs}
````{tab} Transcript

You can only access the transcript which will log protocol request and responses. It's particular useful for protocols using HTTP. Open a *Terminal.app* window and enter 

`log stream --predicate '(process == "Cyberduck") && (category == "transcript")' --level info`

```{note}
The transcript will be written in the *Terminal.app* window. Make sure to keep the window open after executing the command.
```
````

````{tab} Heap Dump

To create a heap dump of the Cyberduck process on macOS (in case of excessive memory usage for example) you can use `jmap` from the {download}`OpenJDK 13<https://github.com/AdoptOpenJDK/openjdk13-binaries/releases/download/jdk-13.0.2%2B8/OpenJDK13U-jdk_x64_mac_hotspot_13.0.2_8.pkg>`.

`jmap -dump:file=cyberduck-dump.hprof [PID of Cyberduck process]`

````
`````

## Application Support Folder

Inside the application support folder, the application saves files needed for their operations e.g. settings, log data, history files, etc.

`````{tabs}
````{group-tab} macOS

You can reach the application support folder by choosing `Go → Go to folder` within the *Finder* menu and paste the path `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` into the window.

````
````{group-tab} Windows

You can reach the application support folder by navigating to `%AppData%\Cyberduck` by copying the path into the address bar of the Explorer and press *Return* afterward.

````
`````

### Crash Reports

`````{tabs}
````{group-tab} macOS

Crash reports are saved to `~/Library/Logs/DiagnosticReports/Cyberduck_*.crash`. On macOS 12 or later crash reports are saved to `~/Library/Logs/DiagnosticReports/Cyberduck_*.ips`.

````
````{group-tab} Windows

Crash reports are saved to `%AppData%\cyberduck\CrashReporter`.

````
`````
