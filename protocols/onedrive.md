Microsoft OneDrive
====

```{image} _images/onedrive.png
:alt: Microsoft OneDrive
:width: 128px
```

```{tip}
Download [Mountain Duck](https://mountainduck.io/) as an alternative to the *One Drive* client from Microsoft.
```

## Connecting

> Microsoft Graph, OneDrive, and SharePoint support using a standard OAuth2 authorization flow.

The OneDrive connection profile is bundled by default and connects to the endpoint `https://graph.microsoft.com/v1.0/me`. Login with your personal or business account to `login.microsoftonline.com` when prompted to grant access to Cyberduck.

1. OneDrive uses OAuth 2 for authentication with `graph.microsoft.com`. When opening a connection, a web browser window is opened to grant access to OneDrive for Cyberduck.
	```{image} _images/Microsoft_OneDrive_OAuth_Authorization.png
	:alt: OAuth 2 Authentication
	:width: 500px
	``` 
2. Copy the authorization code into the login prompt in Cyberduck to complete authentication. Subsequent connections will not require authorization, unless the refresh token itself is expired due to inactivity.

![OAuth 2 Prompt](_images/OneDrive_OAuth_2_Authorization.png)

```{admonition} Multiple Accounts
:class: tip
You can connect to multiple accounts at the same time. Create a new bookmark for every account and run through the OAuth flow.
```

### Reset OAuth Tokens

If you have accidentally logged in with the wrong OneDrive Account or want to change the login of the OneDrive bookmark delete the current bookmark and create a new one to start a new authentication flow.

Alternatively, you can reset the OAuth token by deleting the entries related to `duck:onedrive?user=(user)` out of the *Windows Credential Manager* or on macOS the entries related to `login.microsoftonline.com` out of *Keychain Access.app*.

### Expiry

All authentication codes expire after 90 days. If you get the error message `Forbidden. The caller doesn't have permission to perform the action. [...]` due to this known issue you need to reauthenticate by performing an [OAuth Reset](#reset-oauth-tokens).

### Available Connection Profiles

|                                            | Allows access to | Remarks                                        | Bundled by default |
|--------------------------------------------| --- |------------------------------------------------| :---: |
| Microsoft OneDrive                         | Your Drive and shared files	| Works with your Personal and Business OneDrive | Yes |
| [Microsoft SharePoint](sharepoint.md)      | All sites document libraries and accessible group document libraries |                                                | Yes |
| [Microsoft SharePoint Site](sharepoint.md) | A single SharePoint Site which isn't listed within the *Microsoft SharePoint profile* | Can't mount specific directories               | Yes |

### Administrator Consent Required

Depending on the setup of your AAD you may need to perform several steps in order for you to be able to access your OneDrive. Please get in contact with your domain administrator for following steps.

#### Manually Adding Cyberduck & Mountain Duck

```{Important}
Cyberduck 7.8 and later or Mountain Duck 4.4 and later required
```

Copy the link that corresponds to your used version, and send it to your domain administrator, this will add Cyberduck to the domain and all users are allowed to access Cyberduck in the future.

* [Grant administrator consent](https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=f40bc18f-cd02-4212-b7f1-15243e4e2ad3&redirect_uri=https://cyberduck.io/oauth&scope=sites.readwrite.all%20files.readwrite.all%20offline_access%20user.read)

#### Automatically Allow Users to add Apps to the Domain

If applicable and trusted you may set `Users can consent to apps accessing company data on their behalf` to `Yes` at the [AAD Portal](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings). This will allow users in the future to add apps without Admin-consent.

#### Admin Consent Requests (Preview)

There is a preview method of review application consent through the AAD Portal. Please enable `Users can request admin consent to apps they are unable to consent to` to `Yes` in the [Enterprise applications - User settings](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings). The domain administrator may now review all consents centrally at [Admin consent requests (Preview)](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AccessRequests).

## Cyberduck CLI

You can list the root contents of your OneDrive with [Cyberduck CLI](https://duck.sh/) using

	duck --list onedrive:/

Refer to the [Cyberduck CLI](../cli/index.md) documentation for more operations. For subsequent invocations make sure to include the `--username` parameter and set it to the email address registered with Microsoft to allow the lookup of previously saved OAuth tokens.

## Features
### Search

You can [search recursively](../cyberduck/browser.md#filter-and-search) for files fast without browsing folders first.

### Versions

A list of file versions can be viewed in the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window. Files can be reverted to a chosen version of this list. 

### Share

Create download [shares](../cyberduck/share.md#onedrive--sharepoint) of files or folders for people outside of your organization using *File → Share...*.

## Limitations

There are some limitations that you should keep in mind while working with.

- We've added support for Microsoft 365 China in **Cyberduck 7.8 / Mountain Duck 4.4** but aren't able to verify if it works properly.
- No interoperability with Microsoft 365 for US Government (other services may apply as well)
- Native file locking only exists for OneDrive Business (Microsoft 365 Business), it is not supported for regular consumer use.

### Top Level folder
It is not possible to create a top level folder in Mountain Duck or Cyberduck. Instead, the following virtual top level folders are displayed which cannot be moved or renamed:

| Folder Name |    Contents    |
|-------------|:--------------:|
| My Files    | Personal files |
| Shared      | Shared folders |
