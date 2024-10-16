Support
====

## Application Support Folder

Inside the application support folder, the application saves files needed for their operations e.g. settings, log data, history files, etc.

::::{tabs}
:::{group-tab} macOS

You can reach the application support folder by choosing `Go → Go to folder` within the *Finder* menu, copying the path below into the appearing window, and clicking on the *Open* button afterward.

`~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/`

:::
:::{group-tab} Windows

You can reach the application support folder by navigating to `%AppData%\Cyberduck` by copying the path into the address bar of the Explorer and press *Return* afterward.

:::
::::

## Bug Reports and Feature Requests

[Open a new ticket](mailto:support@mountainduck.io) to report bugs you experience or features you'd like to have added. Make sure to add a detailed description of the issue including the operating system, the used protocol, the used version of Mountain Duck, and the [connection mode](preferences.md#connect-mode).

### Logging Output

::::{tabs}
:::{group-tab} macOS

Log output can be found in the `mountainduck.log` file in`~/Library/Logs/Mountain Duck` or `~/Library/Containers/io.mountainduck/Data/Library/Logs/Mountain Duck` when installed from the Mac App Store respectively.  

Select _Show_ in _Mountain Duck → Preferences → Connection_ to reveal the log file. In addition to the current log file, compressed versions of the latest five cycled log files named `mountainduck-*.log.zip` are available. You can also reach this file in _Console.app_ (Open from `/Applications/Utilities`) under `Reports → Log Reports → mountainduck.log`.

:::
:::{group-tab} Windows

Log output can be found in the `mountainduck.log` file in `%AppData%\cyberduck`. 

Select _Show_ in _Mountain Duck → Preferences → Connection_ to reveal the log file named *mountainduck.log*. In addition to the current log file, there are compressed versions of the latest five cycled log files named `mountainduck-*.log.zip` are available.

:::
::::

#### Debug Log

To enable verbose log output select _Enable debug log_ in _Mountain Duck → Preferences → Connection_.

#### Error Log

An error log is a record of critical errors that occur during the operation of the application or server. It can be a useful tool for troubleshooting.

It can be reached by clicking on the Show button within _Mountain Duck → Preferences → Connection_. The file is named *mountainduck.error*.

#### Installation Log

:::{admonition} Windows only
The installation log contains records of all actions performed by the setup program and by other executable files related to installation. It is required for troubleshooting if you encounter errors during the installation process. The installation log file prefixed `Mountain Duck_` can be found in `%Temp%`.
:::

### Feature Request

Please make sure to include a detailed description of the feature you'd like to request within [your ticket](mailto:support@mountainduck.io).

## Crash Reports

::::{tabs}
:::{group-tab} macOS

Crash reports are saved to `~/Library/Logs/DiagnosticReports/Mountain Duck_*.crash`. On macOS 12 or later crash reports are saved to `~/Library/Logs/DiagnosticReports/Mountain Duck_*.ips`.

:::
:::{group-tab} Windows

Crash reports are saved to `%AppData%\cyberduck\CrashReporter`.

:::
::::

## Get Support

For bug reports, feature requests, or issues regarding purchase and upgrade mail to [support@mountainduck.io](mailto:support@mountainduck.io) to open a ticket.
