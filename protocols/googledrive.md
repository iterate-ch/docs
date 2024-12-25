Google Drive
====

:::{image} _images/googledrive.png
:alt: Google Drive Icon
:width: 128px
:::

:::{tip}
Download [Mountain Duck](https://mountainduck.io/) as an alternative to *Drive File Stream* or *Drive for Desktop*.
:::

:::{contents} Content
:depth: 2
:local:
:::

## Connecting

Connect to your [Google Drive](http://drive.google.com/) to store plain files.

:::{admonition} Advanced Protection Program
:class: warning

Using *[Advanced Protection Program](https://support.google.com/accounts/answer/7539956#non-goog_apps&zippy=%2Ccan-i-use-non-google-apps-services-or-apps-script-with-advanced-protection)* will cause the OAuth login flow to fail with the error message: `400 admin_policy_enforced`.
:::

### Authentication

:::{admonition} OAuth 2.0
:class: note
Google Drive uses a OAuth 2.0 authorization code flow to grant access.
:::

1. Choose _[Open Connection…](../cyberduck/connection.md)_ or add a _[New Bookmark](../cyberduck/bookmarks.md)_ to save the connection settings.
2. No credentials must be entered for opening a connection, but instead you need to log-in to your Google account 
and grant access in your web browser after choosing _Connect_.
3. Choose *Allow* on the website opened in your default web browser to grant access. 
4. Allow to _"Open Cyberduck"_ in your web browser to submit the authorization code used to retrieve the access token for authenticating with Google Drive. Subsequent connections will not require authorization, unless the refresh token expired due to inactivity.

:::{admonition} Multiple Accounts
:class: tip

You can connect to multiple accounts at the same time. Create a new bookmark for every account and run through the OAuth 2.0 flow. Make sure to log out in your browser prior to setting up a new bookmark to make sure the new bookmark is linked to a newly authenticated account.
:::

### Google Apps Accounts

To access the Google Docs storage of your company's [Google Apps](https://workspace.google.com/features/) Account, use
your email address connected to your Google Apps account for the username.

### Google Account With 2-Step Verification

Refer
to [Signing in using application-specific passwords](http://support.google.com/accounts/bin/answer.py?answer=185833) on
how to set an application-specific password to access Google Drive with 2-step verification enabled for your Google
Account.

:::{admonition} Multiple Accounts
:class: tip

You can connect to multiple accounts at the same time. Create a new bookmark for every account and run through the OAuth
flow. Make sure to log out in your browser prior setting up a new bookmark to make sure the new bookmark is linked to a
newly authenticated account.
:::

### Reset OAuth Tokens

If you have accidentally logged in with the wrong Google Drive Account or want to change the login of the Google Drive
bookmark delete the current bookmark and create a new one to start a new authentication flow.

Alternatively, you can reset the OAuth token by deleting the entries related to `duck:googledrive?user=(user)` out of
the *Windows Credential Manager* or on macOS the entries related to `accounts.google.com` out of *Keychain*.

### Custom OAuth Client ID

You can register a [custom OAuth 2.0 client ID](profiles/google_client_id.md) with Google to operate independently of
our registered client ID.

## Cyberduck CLI

You can list the root contents of your Google Drive with [Cyberduck CLI](https://duck.sh/) using

```
duck --list googledrive:/
```

Refer to the [Cyberduck CLI](../cli/index.md) documentation for more operations. For subsequent invocations make sure to
include the `--username` parameter and set it to the email address registered with Google to allow the lookup of
previously saved OAuth tokens.

## Features

### Top Level Folders

The following virtual top level folders are displayed:

| Folder Name    |                             Contents                              |
|----------------|:-----------------------------------------------------------------:|
| My Drive       |                          Personal files                           |
| Shared Drives  |                      Shared drives for teams                      |
| Shared with me | Documents and folders shared with you from another Google account |

It is not possible to create additional top level folders or files.

:::{admonition} Mountain Duck
:class: tip
Set the _Path_ in the [Bookmark](../cyberduck/bookmarks.md) to `/` to show the top level folders. By default, only the
contents of _My Drive_ are shown.
:::

### Search

You can [search recursively](../cyberduck/browser.md#filter-and-search) for files fast without browsing folders first.

### Versions

A list of file versions can be viewed in the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window.
Additionally, versions of the list can be deleted.

### Deleting Files and Folders

Deleted files are trashed instead of being permanently deleted. This feature is enabled by default. It can be disabled
using a [hidden configuration option](../tutorials/hidden_properties.md).

```
browser.delete.trash=false
```

### Google Docs Documents

For Google Docs documents (*Docs, Sheets, Slides*), URL shortcut files are displayed that point your web browser to the
document in Google Docs.

- `.webloc` on macOS
- `.url` on Windows

:::{attention}
*Google Docs* files can't be managed (renamed, moved, or deleted) within Mountain Duck or Cyberduck.
:::

### Share

Create download [shares](../cyberduck/share.md#google-drive) of files or folders for others with no access to your
Google Drive using *File → Share...*.

## Issues

### Rate Limits

Google Drive is imposing rate limits to requests resulting in `403 Forbidden` replies indicating the *Rate Limit
Exceeded* error. Make sure you have set to *Repeat failed networking tasks*
in [Preferences → Connection](../cyberduck/connection.md#repeat-failed-networking-tasks) and set a delay.

### The Granted Scopes do not Give Access to all of the Requested Spaces

Please remove the previously saved OAuth tokens `Google Drive (Email) OAuth2 Access Token` saved in your keychain and
reconnect to grant Cyberduck access to Google Photos.

### Abusive Files

Google Drive may require the user is acknowledging the risk of downloading known malware or other abusive files. For
such files a prompt *Acknowledge the risk of downloading known malware or other abusive file* is shown when the file has
been flagged by Google as possible malware.

