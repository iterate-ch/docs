Microsoft OneDrive
====

:::{image} _images/onedrive.png
:alt: Microsoft OneDrive
:width: 128px
:::

:::{tip}
Download [Mountain Duck](https://mountainduck.io/) as an alternative to the *One Drive* client from Microsoft.
:::

## Connecting

:::{admonition} OAuth 2.0
:class: note
Microsoft Graph, OneDrive, and SharePoint use a OAuth 2.0 authorization code flow to grant access.
:::

The OneDrive connection profile is bundled by default and connects to the endpoint
`https://graph.microsoft.com/v1.0/me`. Login with your personal or business account to `login.microsoftonline.com` when
prompted to grant access to Cyberduck.

1. No credentials must be entered for opening a connection, but instead you need to log-in to your Microsoft account
   and grant access in your web browser after choosing _Connect_.

   :::{image} _images/OneDrive_Sign_In.png
   :alt: OneDrive sign in
   :width: 500px
   :::

2. Allow to _"Open Cyberduck"_ in your web browser to submit the authorization code used to retrieve the access token
   for authenticating with OneDrive. Subsequent connections will not require authorization, unless the refresh token
   expired due to inactivity.

:::{admonition} Multiple Accounts
:class: tip

You can connect to multiple accounts at the same time. Create a new bookmark for every account and run through the OAuth
flow. Make sure to log out of any account in web browser before triggering the OAuth flow for a new account.
:::

### Reset OAuth Tokens

If you have accidentally logged in with the wrong OneDrive Account or want to change the login of the OneDrive bookmark
delete the current bookmark and create a new one to start a new authentication flow.

Alternatively, you can reset the OAuth token by deleting the entries related to `duck:onedrive?user=(user)` out of the
*Windows Credential Manager* or on macOS the entries related to `login.microsoftonline.com` out of *Keychain
Access.app*.

### Expiry

All authentication codes expire after 90 days. If you get the error message
`Forbidden. The caller doesn't have permission to perform the action. [...]` due to this known issue you need to
reauthenticate by performing an [OAuth Reset](#reset-oauth-tokens).

### Available Connection Profiles

:::{note}
Connection profiles not bundled by default can be installed from *Preferences → Profiles*.
:::

|                                                                                         | Allows access to                                                                      | Remarks                                        | Bundled by default |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|------------------------------------------------|:------------------:|
| Microsoft OneDrive                                                                      | Your Drive and shared files	                                                          | Works with your Personal and Business OneDrive |        Yes         |
| [Microsoft SharePoint](sharepoint.md)                                                   | All sites document libraries and accessible group document libraries                  |                                                |        Yes         |
| [Microsoft SharePoint Site](sharepoint.md#microsoft-sharepoint-site-connection-profile) | A single SharePoint Site which isn't listed within the *Microsoft SharePoint profile* |                                                |         No         |
| Microsoft 365 China                                                                     |                                                                                       |                                                |         No         |

### Administrator Consent Required

Depending on the setup of your AAD you may need to perform several steps in order for you to be able to access your
OneDrive. Please get in contact with your domain administrator for following steps.

#### Manual Approval Links

The domain administrator can approve access for Cyberduck and Mountain Duck using the following links:
* [Cyberduck](https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=f40bc18f-cd02-4212-b7f1-15243e4e2ad3&redirect_uri=https://cyberduck.io/oauth&scope=files.readwrite.all%20offline_access%20user.read)
* [Mountain Duck](https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=94c5bafe-e6f8-4bd7-94e8-92d5cc8aa581&redirect_uri=https://cyberduck.io/oauth&scope=files.readwrite.all%20offline_access%20user.read)

#### Automatically Allow Users to add Apps to the Domain

If applicable and trusted you may set `Users can consent to apps accessing company data on their behalf` to `Yes` at
the [AAD Portal](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings).
This will allow users in the future to add apps without Admin-consent.

#### Admin Consent Requests (Preview)

There is a preview method of review application consent through the AAD Portal. Please enable
`Users can request admin consent to apps they are unable to consent to` to `Yes` in
the [Enterprise applications - User settings](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/UserSettings).
The domain administrator may now review all consents centrally
at [Admin consent requests (Preview)](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AccessRequests).

## Cyberduck CLI

You can list the root contents of your OneDrive with [Cyberduck CLI](https://duck.sh/) using

```
duck --list onedrive:/
```

Refer to the [Cyberduck CLI](../cli/index.md) documentation for more operations. For subsequent invocations make sure to
include the `--username` parameter and set it to the email address registered with Microsoft to allow the lookup of
previously saved OAuth tokens.

## Features

### Top Level Folders

The following virtual top level folders are displayed:

| Folder Name |    Contents    |
|-------------|:--------------:|
| My Files    | Personal files |
| Shared      | Shared folders |

It is not possible to create additional top level folders or files.

:::{admonition} Mountain Duck
:class: tip
Set the _Path_ in the [Bookmark](../cyberduck/bookmarks.md) to `/` to show the top level folders. By default, only the
contents of _My Files_ are shown.
:::

### Search

You can [search recursively](../cyberduck/browser.md#filter-and-search) for files fast without browsing folders first.

### Versions

A list of file versions can be viewed in the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window. Files
can be reverted to a chosen version of this list.

### Share

Create download [shares](../cyberduck/share.md#onedrive--sharepoint) of files or folders for people outside of your
organization using *File → Share...*.

## Limitations

There are some limitations that you should keep in mind while working with.

- No interoperability with Microsoft 365 for US Government (other services may apply as well)
- Native file locking only exists for OneDrive Business (Microsoft 365 Business), it is not supported for regular
  consumer use.
- OneDrive API does not list pending upload sessions therefore resuming uploads in Cyberduck will cause the upload to
  start all over again.

### Quota

Mountain Duck can only display the correct cloud storage quota as remaining disk space when setting the *Path* in the
bookmark configuration to a folder different from `/`, for example `My Files`.