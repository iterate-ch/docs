Support
====

## Get Support

### Feature Requests

If you have a feature request please make sure to include a detailed and comprehensible description of the requested feature in [the ticket](https://github.com/iterate-ch/cyberduck/issues/new/choose). Make sure to check if someone already requested a similar feature.

:::{warning}
For issues with your remote storage user account credentials, please instead write to your hosting service provider. 
:::

### Bug Reports

[Open a new ticket](https://github.com/iterate-ch/cyberduck/issues/new/choose) with a description of what you have done and what went wrong. Make sure to look or search for existing issues first. If you have trouble connecting to a server or your login credentials are not valid, try to resolve the issue with the assistance of your hosting service provider.

:::{note}
Discuss features and issues you are having in [GitHub Discussions](https://github.com/iterate-ch/cyberduck/discussions). For issues with the registration key, please send an email to [support@cyberduck.io](mailto:support@cyberduck.io).
:::

:::{warning}
Please be aware that you are possibly using our software at no charge if you have not purchased a registration key. Thus the support provided here is best effort only.
:::

## Logging Output

:::::{tabs}
::::{group-tab} macOS

Log output can be found in the `cyberduck.log` file in`~/Library/Logs/Cyberduck`. Select _Show_ in _Cyberduck → Preferences → Connection_ to reveal the log file. Alternatively, you can find `cyberduck.log` in *Console.app* (Open from `/Applications/Utilities`) under `Reports → Log Reports → cyberduck.log`.

:::{image} _images/Console.app.png
:alt: Console.app
:width: 600px  
:::

**Transcript**

You can access the transcript which will log protocol request and responses from the command line particularly useful for protocols using HTTP. Open a *Terminal.app* window and enter 

`log stream --predicate '(process == "Cyberduck") && (category == "transcript")' --level info`

:::{note}
The transcript will be written in the *Terminal.app* window. Make sure to keep the window open after executing the command.
:::

::::
::::{group-tab} Windows

Log output can be found in the `cyberduck.log` file in `%AppData%\cyberduck`. Select _Show_ in _Cyberduck → Preferences → Connection_ to reveal the log file named *cyberduck.log*.

::::
:::::

### Debug Log

To enable verbose log output select _Enable debug log_ in _Cyberduck → Preferences → Connection_.

## Application Support Folder

Inside the application support folder, the application saves files needed for their operations e.g. settings, log data, history files, etc.

::::{tabs}
:::{group-tab} macOS

You can reach the application support folder by choosing `Go → Go to folder` within the *Finder* menu and paste the path `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` into the window.

:::
:::{group-tab} Windows

You can reach the application support folder by navigating to `%AppData%\Cyberduck` by copying the path into the address bar of the Explorer and press *Return* afterward.

:::
::::

### Crash Reports

::::{tabs}
:::{group-tab} macOS

Crash reports are saved to `~/Library/Logs/DiagnosticReports/Cyberduck_*.crash`. On macOS 12 or later crash reports are saved to `~/Library/Logs/DiagnosticReports/Cyberduck_*.ips`.

:::
:::{group-tab} Windows

Crash reports are saved to `%AppData%\cyberduck\CrashReporter`.

:::
::::
