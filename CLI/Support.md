Support
===

# Application Support Directory

## Profiles

The directory location is printed with `--help` following the list of supported protocols.

`````{tabs}
````{group-tab} macOS

The support directory is `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` on Mac. You can install third party [profiles](../Cyberduck/Profiles) in `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Profiles`.

````
````{group-tab} Windows

Install additional profiles in `%AppData%\Cyberduck\Profiles` on Windows.

````
````{group-tab} Linux

The support directory is `~/.duck/` on Linux. You can install third party [profiles](../Cyberduck/Profiles) in `~/.duck/profiles/`.

````
`````

# Logging Output

The logging output is written directly into the command line:

- **macOS:** Open *Terminal.app* and type `-v`
- **Windows:** Open *cmd.exe* and type `-v`

## Enable debug logging

To enable debug logging use the parameter `--debug`. Alternatively set the [environment variable](index#preferences) `logging` to the level `debug`, `info`, `warn`, or `error`.