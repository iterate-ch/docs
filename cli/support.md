Support
===

# Application Support Directory

`````{tabs}
````{group-tab} macOS

You can reach the application support folder by choosing `Go → Go to folder` within the *Finder* menu, copying the path below into the appearing window, and clicking on the *Open* button afterward.

`~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/`

````
````{group-tab} Windows

You can reach the application support folder by navigating to `%AppData%\Cyberduck` by copying the path into the address bar of the Explorer and press *Return* afterward.

````
````{group-tab} Linux

The support directory is `~/.duck/`.

````
`````

## Profiles

The directory location is printed with `--help` following the list of supported protocols.

`````{tabs}
````{group-tab} macOS

You can install third party [profiles](../protocols/profiles) in `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Profiles`.

````
````{group-tab} Windows

Install additional profiles in `%AppData%\Cyberduck\Profiles` on Windows.

````
````{group-tab} Linux

You can install third party [profiles](../protocol/profiles) in `~/.duck/profiles/`.

````
`````

# Logging Output

The logging output is written directly into the command line:

- **macOS:** Open *Terminal.app* and type `-v`
- **Windows:** Open *cmd.exe* and type `-v`

## Enable Debug Logging

To enable debug logging use the parameter `--debug`. Alternatively, set the [environment variable](index.md#preferences) `logging` to the level `debug`, `info`, `warn`, or `error`.
