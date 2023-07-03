Installation
====

```{toctree}
:hidden:
:titlesonly:

licensing
```

`````{tabs}
````{group-tab} macOS

**Download**<br/>
Move the unzipped application bundle *Mountain Duck.app* from the Downloads to the `/Applications` folder on your computer.

```{note}
No admin privileges for installation is required.
```

**Mac App Store**<br/>
Mountain Duck is installed through the Mac App Store in `/Applications`. You can always reinstall Mountain Duck on any Mac you own from the Mac App Store in *→ App Store... → Purchased*.

**Login Item**<br/>
You can choose to open Mountain Duck when you log into your computer. Tha application will appear in *Login Items* of the *User & Groups* system preferences panel.

![Login Item](_images/Login_Item.png)

**Finder Extension**<br/>
Enable the Mountain Duck Finder Extension in *System Preferences → Extensions → Finder* by selecting the checkbox. This will enable:

- **Context menu items** for files selectec on a mounted volume with options to *Reload* the folder listing and copy & open URLs of files
- **Badges** on file icons to display sync status when *Smart Synchronization* is enabled for the bookmark

```{note}
For **macOS Ventura and later**, the setting can be found in *System Settings → Privacy & Security → Extensions → Added Extensions*.
```

![Mountain Duck Finder Integration](_images/Mountain_Duck_Finder_Integration.png) 

````

````{group-tab} Windows

**Installer**<br/>
[Download](https://mountainduck.io/changelog/) the *Mountain Duck Installer.exe* and install Mountain Duck with administrator privilege.

![Mountain Duck Windows Installer](_images/Mountain_Duck_Windows_Installer.png)

**MSI**<br/>
[Download](https://mountainduck.io/changelog/) MSI Installer for corporate environments. Requires prior installation of *Microsoft .NET Framework 4.5.2*.

```{note}
Using the MSI Installer, you'll have to install the *MSI Package Shell Extension for 32bit applications* **and** *MSI Package Shell Extension for 64bit applications* separatly. Both packages are needed to enable the explorer extension.
```

````
`````

## System Requirements

`````{tabs}
````{group-tab} macOS

- Mountain Duck 3.3.5 or later requires *macOS 10.12* or later
- Mountain Duck 3.0.1 or later requires *macOS 10.11* or later
````

````{group-tab} Windows

Requires *.NET Framework 4.7.2.* If the {download}`.Net Framework installation<https://dotnet.microsoft.com/download/dotnet-framework/net472>` fails, download it manually.

- Mountain Duck 4.13.0 or later requires *Windows 10 (14393) or Windows Server 2016* or later on 64 Bit.
- Mountain Duck 3.2.0 or later requires *Windows 7, Windows 8.1, Windows 10 (14393)* or later on 64Bit.
- Mountain Duck 3.0.1 or later requires *Windows 7* or later.
````
`````

## Registration Key

Double-click the file `.mountainducklicense` to apply the license and register Mountain Duck. Alternatively, you can copy the key file to the [application support folder](../support.md#application-support-folder).

`````{tabs}
````{group-tab} macOS

You can manually install the registration key in

- `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/`

````

````{group-tab} Windows

You can install the registration key either in:

- `%AppData%\Cyberduck`
- `C:\Program Files\Mountain Duck`

````
`````

### Known Issues

#### Not a Valid Registration Key

This error message appears if you try to use an old license key for a newer version.
[Upgrade](https://mountainduck.io/buy/upgrade/) your license to the latest version of Mountain Duck or download an older version from [Mountain Duck changelog](https://mountainduck.io/changelog/).

#### Upgrade Issues

After upgrading a license, a new license file will be generated.

1. Delete the current license file from the application support folder.
2. Download the new license file from the email attachment.
3. Apply the new license file using double-click or copy the file into the application support folder.

### Windows Installation
#### Error Code 0x24C
If you're experiencing the error code `0x24C` `A volume has been accessed for which a file system driver is required that has not yet been loaded.`, please uninstall the client, reboot the system, and reinstall the client.

#### Installer goes haywire
In some cases, the windows gets confused over the installed product and goes haywire. As a result the product can't be modified anymore. To fix the state, run the following command:
	`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" /s /f "Product Name"`
	`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products" /s /f "Product Name"`

You should get an output like this:
	`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{23067521-119B-4B0A-BCDD-38835D58077B}
    DisplayName    REG_SZ    Cyberduck`

Delete the key using the following command: 
	`reg delete "output" /f`

Based on the example output it should look like this:
	`reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{23067521-119B-4B0A-BCDD-38835D58077B}" /f`

After restarting the system, the installer shouldn't complain anymore.

## Uninstall

Using Windows Command Line:

* Regular uninstall:
	`Mountain Duck Installer-<version>.exe /uninstall`
* Silent uninstall:
	`Mountain Duck Installer-<version>.exe /uninstall /quiet`

### Complete Uninstall

Follow the steps below to uninstall Mountain Duck completely.

`````{tabs}
````{group-tab} macOS

1. Close the application and navigate to the application folder using the shortcut `⌘⇧A`. Select *Mountain Duck.app* and delete the application by choosing *File → Move to Trash*.
2. Navigate to the *Group Containers* folder within *~/Library/* and delete the folder *G69SCX94XU.duck*. If you changed the cache location you will have to delete that folder as well.
3. **Optional:** Delete all saved login credentials regarding Mountain Duck within *Keychain Access.app*.

````

````{group-tab} Windows

1. Close the application and open the start menu using the shortcut `Ctrl Esc`. Search for *Apps & Features* and move to the entry *Mountain Duck*. Click on the application, choose *Uninstall*, and confirm your intentions by clicking *Uninstall* again.
2. Navigate to the `%AppData%`and delete the folder *Cyberduck*
3. Navigate to `%LocalAppData%`and delete the folder *Cyberduck*
4. **Optional:** Delete all saved login credentials regarding Mountain Duck within *Windows Credential Manager*.

````

`````