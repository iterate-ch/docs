Installation
===

`````{tabs}
````{group-tab} macOS

Move the unzipped application bundle *Cyberduck.app* from the *Downloads* to the */Applications* folder on your harddisk.

````
````{group-tab} Windows

**EXE Installer**

Run the *Cyberduck Installer* executable. For an unattached installation, use the silent option (command line option `/s`).


**MSI Installer**

Download *MSI Installer* for corporate environments. Requires prior installation of [Microsoft .NET Framework 4.5.1](https://www.microsoft.com/en-us/download/details.aspx?id=40779).


**Chocolatey**

There is also a [Chocolatey](http://chocolatey.org/packages?q=cyberduck) package maintained.

````
`````

## System Requirements

`````{tabs}
````{group-tab} macOS

- Cyberduck [8.1](https://trac.cyberduck.io/milestone/8.1) or later requires *Mac OS X 10.12* or later and a [64Bit Intel](http://support.apple.com/kb/ht3696) or [Apple silicon](https://support.apple.com/en-us/HT211814) architecture
- Cyberduck [7.7](https://trac.cyberduck.io/milestone/7.7.0) or later requires *Mac OS X 10.9* or later and a [64Bit Intel](http://support.apple.com/kb/ht3696) architecture
- Cyberduck 7.1 or later requires *Mac OS x 10.8* or later and a [64Bit Intel](http://support.apple.com/kb/ht3696) architecture
- Cyberduck 4.7 or later requires *Mac OS X 10.7* or later and a [64Bit Intel](http://support.apple.com/kb/ht3696) architecture
- Cyberduck 4.4 or later requires *Mac OS X 10.6* or later and a [64Bit Intel](http://support.apple.com/kb/ht3696) architecture
- Cyberduck [3.3](https://trac.cyberduck.io/milestone/3.3) or later requires *Mac OS X 10.5* or later.
- Cyberduck [3.0](https://trac.cyberduck.io/milestone/3.0) or later requires *Mac OS X 10.4* or later. The latest version [available](http://cyberduck.ch/changelog) is [3.2.1](http://update.cyberduck.ch/Cyberduck-3.2.1.dmg) supporting *Mac OS X 10.4*.
- Cyberduck 2.5 or later requires *Mac OS X 10.3.9* or later. The latest version [available](http://cyberduck.ch/changelog) is [2.8.5](http://update.cyberduck.ch/Cyberduck-2.8.5.dmg) supporting *Mac OS X 10.3.9*.
- Cyberduck 2.3 or later requires *Mac OS X 10.2* or later. The latest version [available](http://cyberduck.ch/changelog) is [2.3.3](http://update.cyberduck.ch/Cyberduck-2.3.3.dmg) supporting *Mac OS X 10.2*.

````
````{group-tab} Windows

Requires *.NET Framework 4.7.2*. If the [.NET Framework installation](https://dotnet.microsoft.com/download/dotnet-framework/net472) fails, download it manually.

- Cyberduck [7.1](https://trac.cyberduck.io/milestone/7.1) or later requires *Windows 7 SP1, Windows 8.1, or Windows 10 (14393)* or later on 64bit.
- Cyberduck [5.3](https://trac.cyberduck.io/milestone/5.3) or later requires *Windows 7* or later
- Cyberduck [4.8](https://trac.cyberduck.io/milestone/4.8) or later requires *Windows Vista* or later.
- Cyberduck [4.0](https://trac.cyberduck.io/milestone/4.0) or later requires *Windows XP or Windows 7* or later.

````
`````

## Complete Uninstall

Follow the steps below to uninstall Cyberduck completely.

`````{tabs}
````{group-tab} macOS

1. Close the application and navigate to the application folder using the shortcut `⌘⇧A`. Select *Cyberduck.app* and delete the application by choosing *File → Move to Trash*.
2. Navigate to the *Group Containers* folder within *~/Library/* and delete the folder *G69SCX94XU.duck*.
3. **Optional:** Delete all saved login credentials in *Keychain Access.app*.

````

````{group-tab} Windows

1. Close the application and open the start menu using the shortcut `Ctrl Esc`. Search for *Apps & Features* and move to the entry *Cyberduck*. Click on the application, choose *Uninstall*, and confirm your intentions by clicking *Uninstall* again.
2. Navigate to the `%AppData%`and delete the folder *Cyberduck*
3. Navigate to `%LocalAppData%`and delete the folder *Cyberduck*
4. **Optional:** Delete all saved login credentials in *Windows Credential Manager*.

````

`````