Microsoft SharePoint
====

:::{image} _images/onedrive.png
:alt: Microsoft OneDrive
:width: 128px
:::

:::{tip}
Download [Mountain Duck](https://mountainduck.io/) to access in Finder on macOS & Windows Explorer.
:::

## SharePoint Online

:::{admonition} OAuth 2.0
:class: note
Microsoft SharePoint uses a OAuth 2.0 authorization code flow to grant access.
:::

### Microsoft SharePoint Connection Profile

Connect to *SharePoint Online* with the bundled *Microsoft SharePoint* connection profile. Follow these steps to connect to your *SharePoint Online libraries*:

1. Choose _[Open Connection…](../cyberduck/connection.md)_ or add a _[New Bookmark](../cyberduck/bookmarks.md)_ to save the connection settings and select the _Microsoft SharePoint_ connection profile.
2. No credentials must be entered for opening a connection, but instead after choosing _Connect_ you need to log in to `login.microsoftonline.com` with your `onmicrosoft.com` account in your web browser.
3. Grant permission to *Cyberduck* to access your *SharePoint* library.
4. Allow to _"Open Cyberduck"_ in your web browser to submit the authorization code used to retrieve the access token for authenticating with Microsoft SharePoint. Subsequent connections will not require authorization, unless the refresh token expired due to inactivity.
5. You are now able to access all sites, subsites, and document libraries thereof as well as all groups you are a member of.

### Microsoft SharePoint Site Connection Profile

:::{note}
Connection profiles not bundled by default can be installed from *Preferences → Profiles*.
:::

In case you are trying to access a site that is not listed when connecting with the *Microsoft SharePoint* connection profile,
you can try to access the missing site with help of the *Microsoft SharePoint Site* connection profile. When using the *Microsoft SharePoint Site* connection profile, you are required to enter the SharePoint hostname (such as `contoso.sharepoint.com`) and the URL prefix path configured for your SharePoint site. 

### SharePoint Hybrid

If you have your own SharePoint Server but opted in to enable *Microsoft Graph*-connectivity to your SharePoint Server, you may be able to use the built-in *Microsoft SharePoint*-Profile.

Please refer to the official documentation from Microsoft for detailed setup guides.

- [Hybrid for SharePoint Server](https://support.office.com/en-us/article/sharepoint-hybrid-4c89a95a-a58c-4fc1-974a-389d4f195383)
- [Plan SharePoint Server hybrid](https://docs.microsoft.com/en-us/sharepoint/hybrid/plan-sharepoint-server-hybrid)

### Administrator Consent Required

Administrator-consent may be required in certain situations. Depending on the setup of your Azure Active Directory (AAD) you may need to perform several steps in order for you to be able to access your SharePoint Online. Please get in contact with your domain administrator.

#### Manual Approval Links

The domain administrator can approve access for Cyberduck and Mountain Duck using the following links:

- [Cyberduck](https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=f40bc18f-cd02-4212-b7f1-15243e4e2ad3&redirect_uri=https://cyberduck.io/oauth&scope=sites.readwrite.all%20files.readwrite.all%20offline_access%20user.read%20groupmember.read.all)
- [Mountain Duck](https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=94c5bafe-e6f8-4bd7-94e8-92d5cc8aa581&redirect_uri=https://cyberduck.io/oauth&scope=sites.readwrite.all%20files.readwrite.all%20offline_access%20user.read%20groupmember.read.all)

### Automatically Allow Users to add Apps to the Domain

If applicable and trusted you may set `Users can consent to apps accessing company data on their behalf` to `Yes` at the [Azure Active Directory Portal](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings). This will allow users in the future to add apps without Admin-consent.

### Admin Consent Requests (Preview)

There is a preview method of review application consent through the Azure Active Directory (AAD) Portal. Please enable `Users can request admin consent to apps they are unable to consent to` to `Yes` in the [Enterprise applications - User settings](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings). The domain administrator may now review all consents centrally at [Admin consent requests (Preview)](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AccessRequests).

## SharePoint Server

To connect to a SharePoint Server, choose [WebDAV](webdav/index.md) for the connection type. This is available to

- SharePoint Server 2013
- SharePoint Server 2016
- SharePoint Server 2019

### Available Authentication Methods

#### Basic Authentication

Basic Authentication should only be used when using secured connection over TLS (HTTPS).

#### NTLM Authentication

[NTLM authentication](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/ntlm-user-authentication) may additionally require the name of the computer (NTLM Workstation) and network domain name (NTLM Domain). The optional domain name can be customized as part of the username in the format `REALM\username` in the _Username_ input field when adding a [bookmark](../cyberduck/bookmarks.md#bookmark-options). 

* The default domain used when not specified can be set by using the [hidden configuration option](../tutorials/hidden_properties.md)
    ```
    webdav.ntlm.domain=MYDOMAIN
    ```

* The default workstation can be set using the [hidden configuration option](../tutorials/hidden_properties.md)
    ```
    webdav.ntlm.workstation=MYWORKSTATION
    ```

:::{admonition} Windows
:class: tip

Alternatively, you can set the [hidden configuration option](../tutorials/hidden_properties.md) `webdav.ntlm.environment=true` to read the domain and workstation for NTLM authentication from the Windows environment.
:::

#### Configuration

You may review your SharePoint authentication methods via `SharePoint Central Administration → Security → Specify authentication providers → Select zone`.

![Authentication Admin Panel](_images/AuthenticationAdmin.png)

### Unavailable Authentication Methods

You may not connect to a SharePoint enabled site through WebDAV if any of these authentication methods is required:

- Kerberos (Issue [#133](https://github.com/iterate-ch/cyberduck/issues/12082))
- Forms Based Authentication
- Trusted Identity Provider

## Versioning

A list of file versions can be viewed in the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window.

## Limitations

### Top Level folder

It is not possible to create a top level folder in Mountain Duck or Cyberduck. Instead, the following virtual top level folders are displayed which cannot be moved or renamed:

| Folder Name |
|-------------|
| Default     |
| Drives      |
| Groups      |
| Sites       |

### Quota

Quota reporting is only supported for the *Drives* folder within their respective site folder.