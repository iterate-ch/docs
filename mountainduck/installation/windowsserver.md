Windows Server, Terminal Services & Citrix
====

Installation and operation of Mountain Duck 5 or later in multi-user environments: Remote Desktop Services (RDS), Citrix Virtual Apps & Desktops, and Windows Server installations.

## MSIX Installer Package

As of version 5.0, Mountain Duck is distributed as an *MSIX* package (Windows app) and no longer as a classic program installation. For multi-user environments this means:

- Installation for all users is performed with *app provisioning* using PowerShell (`Add-AppxProvisionedPackage`) instead of the graphical installer.
- [Sideloading of trusted apps](#sideloading) must be permanently allowed on the server.
- The downloadable `.exe` installer is a bootstrapper installing the same MSIX package in the background. On terminal servers it may briefly start and exit without displaying a message. Always use the *MSIX Installer Package* directly on servers.

## Supported Windows Server Versions

Mountain Duck 5 requires *Windows 10 1809 (17763)* or later. For server operating systems:

| Operating System | Status | Notes |
| --- | --- | --- |
| Windows Server 2022 / 2025 | Recommended | Fully supported, including context menu items and *Integrated* connect mode. Recommended basis for terminal servers and Citrix. |
| Windows Server 2019 | Limited | Installation is only reliable using [PowerShell provisioning](#machine-wide-installation). Context menu items in *Windows Explorer* are not available because the operating system lacks *PackagedCom* support for MSIX apps; core functionality (mounted volume, synchronization) is not affected. Use Mountain Duck *5.3.1* or later — earlier versions have a known defect when updating or provisioning on Server 2019. |
| Windows Server 2016 | No 5.x | Build 14393 is below the minimum requirement of version 5. The last usable product line is Mountain Duck 4.x (4.13 or later, requires *.NET Framework 4.7.2*). |
| Windows Server 2012 / 2012 R2 | Not supported | The operating system is end-of-life. The last runnable version was Mountain Duck 4.12.5. |

:::{note}
The *Desktop Experience* installation option (graphical user interface) is required on all servers. *Server Core* installations are not supported.
:::

## Prerequisites

### Sideloading

Sideloading of trusted apps must be allowed to install the MSIX package *and* to allow the app to launch for all users afterwards. Whether any action is required depends on the operating system — sideloading is enabled by default since *Windows 10 2004*:

| System | Sideloading by Default | Required Action |
| --- | --- | --- |
| Windows Server 2019 (Build 1809) | Disabled | The policy must be explicitly enabled (see below). *Not configured* effectively means *disabled* here. |
| Windows Server 2022 / 2025 | Enabled | None — verify that no enterprise policy disables sideloading. |
| Windows 10 (2004 or later) / Windows 11 | Enabled | None — verify that no enterprise policy disables sideloading. |

Enable sideloading on *Windows Server 2019* using one of the following options:

- **Group Policy:** `gpedit.msc` → *Computer Configuration → Administrative Templates → Windows Components → App Package Deployment → Allow all trusted apps to install*
- **Registry** (for scripts, in an elevated PowerShell):

```
Set-ItemProperty HKLM:\Software\Policies\Microsoft\Windows\Appx -Name AllowAllTrustedApps -Value 1 -Type DWord
```

In managed environments (GPO/Intune) the default can be overridden on any system: a policy enforcing [`AllowAllTrustedApps=0`](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-applicationmanagement#allowalltrustedapps) blocks installation and launch on *Windows 11* and *Server 2022/2025* as well. When in doubt, verify the effective value:

```
Get-ItemProperty HKLM:\Software\Policies\Microsoft\Windows\Appx -Name AllowAllTrustedApps
```

:::{warning}
Do not reset the setting after the installation. If `AllowAllTrustedApps` is set back to `0`, users can no longer launch the installed app (it is listed in *Windows Settings* with a size of 0). In environments where this policy must remain disabled, version 5 can currently only be deployed from the *Microsoft Store* or as an Intune line-of-business (LOB) app.
:::

### Unsupported Configurations

- **RemoteApp / published single applications:** Mountain Duck is a tray application. RemoteApp sessions do not transfer the notification area — deployment as a single RemoteApp or published Citrix app is not supported. Deploy Mountain Duck in full desktop sessions only.
- **FSLogix profile containers:** Microsoft explicitly does not support MSIX/Store apps in FSLogix containers. FSLogix environments show corrupted app package folders and crashes on launch. If FSLogix is in use, refer to [Troubleshooting AppX/MSIX with FSLogix](https://learn.microsoft.com/en-us/fslogix/troubleshooting-appx-issues); compatibility cannot be guaranteed.

## Installation

### Preparation

1. Uninstall an existing Mountain Duck 4.x installation using *Apps & Features*.
2. Verify [sideloading](#sideloading) and enable it if necessary (mandatory on Server 2019).
3. **Sign out all other users from the server.** Provisioning fails while other users are signed in — the most common cause of failure on terminal servers.
4. Download the *MSIX Installer Package* from the official download page (do not use the `.exe` installer).

### Machine-wide Installation

In an elevated PowerShell:

```
Add-AppxProvisionedPackage -Online -SkipLicense -LogPath "$env:Temp\MountainDuck-msix.log" -PackagePath "Mountain Duck_x.x.x.xxxxx_x64.msix"
```

This provisions the package for all user profiles. The actual registration takes place per user at the next sign-in — the app appears in the Start menu with a short delay.

**Citrix with gold/master image:** Perform the provisioning in the image (interactively with `-Online` as above, or offline against the mounted image):

```
Add-AppxProvisionedPackage -Path "X:\Mount" -SkipLicense -PackagePath "Mountain Duck_x.x.x.xxxxx_x64.msix"
```

### Support Package (Driver & Shell Extension)

Connecting using [*Online*](../connect/online.md) or [*Smart Synchronization*](../connect/sync.md) connect mode additionally requires a file system driver and *Windows Explorer* integration. The package is included in the MSIX and is installed machine-wide:

```
msiexec /i "$((Get-AppxPackage -AllUsers io.mountainduck).InstallLocation)\Setup\Mountain Duck Support.msi" /qn /l*v "$env:Temp\MountainDuck-support.log" ALLUSERS=1 REBOOT=ReallySuppress
```

:::{note}
No driver is required in [*Integrated*](../connect/integrated.md) connect mode (Windows Cloud Files API) — the support package can be omitted in this case. This makes *Integrated* the least invasive option on terminal servers.
:::

### Verify Installation

```
Get-AppxPackage -AllUsers io.mountainduck
```

Manual launch (e.g. from a logon script):

```
start shell:AppsFolder\$((Get-AppxPackage io.mountainduck).PackageFamilyName)!App
```

Sign in with a test user, wait for the app registration to complete, and verify that a connection can be configured and the mounted volume is accessible.

## Updates

- Do not use the built-in update function or the `.exe` installer on terminal servers. Install updates like the initial installation: provision the new MSIX using `Add-AppxProvisionedPackage` with no users signed in.
- In Citrix environments, update the gold image and redeploy.
- When upgrading from 4.x to 5.x, the automatic updater also installs the support package without asking. To control this (e.g. for *Integrated* connect mode without the driver), uninstall 4.x and install 5.x manually using the MSIX package.
- On *Windows Server 2019*, always use version *5.3.1* or later.

## Recommendations

- **Keep the drive letter set to *Auto*.** In Citrix environments, fixed drive letter assignments have been observed to cause connection drops that disappeared after switching to *Auto*.
- **Choose the [connect mode](../connect/index.md) deliberately:** *Integrated* requires no driver; *Online* and *Smart Synchronization* require the support package and the file system driver.
- **Never create package folders manually.** Creating missing folders below `%LocalAppData%\Packages\` by hand results in incorrect permissions (ACLs) and crashes of the app. Such errors indicate a provisioning or profile problem that must be fixed at its cause.
- **Antivirus/security agents:** Third-party real-time scanners can significantly degrade *Windows Explorer* performance on the mounted volume. Add the Mountain Duck volume and the local cache to the exclusions.
- **Roaming profiles:** Configuration and logs are stored in the user profile (the `%AppData%` part roams).

## Troubleshooting

| Symptom | Cause / Resolution |
| --- | --- |
| Installer briefly starts and exits without a message | The `.exe` bootstrapper fails at the MSIX deployment. Install the MSIX directly using [`Add-AppxProvisionedPackage`](#machine-wide-installation). |
| `Add-AppxProvisionedPackage` fails | Other users are signed in to the server — sign out all sessions and retry. |
| App only launches for the installing administrator; listed with a size of 0 for other users | `AllowAllTrustedApps` was reset after the installation or is overridden by a policy. Set the value permanently to `1`. |
| App does not start automatically after signing out and back in | Verify the autostart of the app in desktop sessions; in special cases launch it from a logon script: `start shell:AppsFolder\<PackageFamilyName>!App` |
| Error code `0x24C` when loading the file system driver | Uninstall the client, reboot the server, and reinstall. |
| Crash with event log entry `Microsoft-Windows-AppModel-State`, error `-2147024809 (E_INVALIDARG)` | Corrupted app package folder in the user profile (typical with FSLogix or manually created folders). Clean up the user profile; verify FSLogix compatibility. |

### Logs for Support

- **MSIX deployment:** *Event Viewer → Applications and Services Logs → Microsoft → Windows → AppXDeployment(-Server) → Operational*, plus the log created with `-LogPath`.
- **Support package:** the log created with `msiexec /l*v`; installation logs prefixed `Mountain Duck_` in `%Temp%`.
- **Application logs:** in the user profile (with roaming profiles, in the roaming part on the terminal server). Refer to the [support page](../support/index.md).
