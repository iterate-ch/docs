Dropbox
====

```{image} _images/dropbox.png
:alt: Dropbox Drive Icon
:width: 128px
```

```{tip}
Access your [Dropbox](https://db.tt/49NiK95I) without syncing to your computer. Download [Mountain Duck](https://mountainduck.io/) as an alternative to *Dropbox Client*.
```

## Connecting

1. You will be asked to link Cyberduck to your Dropbox account on your first connection attempt.

![Dropbox Link](_images/Dropbox_Link.png)

3. Log in to Dropbox and grant permissions to *Cyberduck*.

![Dropbox Permissions](_images/Dropbox_Permissions.png)

4. The authorization code will be submitted to Cyberduck automatically.

```{admonition} Multiple Accounts
:class: tip
You can connect to multiple accounts at the same time. Create a new bookmark for every account and run through the OAuth flow. Make sure to log out in your browser prior to setting up a new bookmark to make sure the new bookmark is linked to a newly authenticated account.
```

### Reset OAuth Tokens

If you have accidentally logged in with the wrong Dropbox Account or want to change the login of the Dropbox bookmark delete the current bookmark and create a new one to start a new authentication flow. Alternatively, you can reset the OAuth token by deleting the entries related to `duck:dropbox?user=(user)` out of the *Windows Credential Manager* or on macOS the entries related to `api.dropboxapi.com` out of *Keychain Access.app*.

## Cyberduck CLI

You can list the root contents of your Dropbox with [Cyberduck CLI](https://duck.sh/) using

	duck --list dropbox:/

Refer to the [Cyberduck CLI](../cli/index.md) documentation for more operations. For subsequent invocations make sure to include the `--username` parameter and set it to the email address registered with Dropbox to allow the lookup of previously saved OAuth tokens.

## Features

### Shared Folders

If you want to access folders that are shared with you through Dropbox you have to add the desired folder to your own drive at the webpage of Dropbox. To do that, open your Dropbox Account within a web browser and navigate to the *Shared* section. Add the desired file or folder to your own drive by clicking on the *Add* button beside the file or folder.

### Search

```{attention}
This only applies to Cyberduck.
```

You can [search recursively](../cyberduck/browser.md#filter-and-search) for files fast without browsing folders first.

### Versions

A list of file versions can be viewed in the *Versions* tab of the *[Info](../cyberduck/info.md#versions)* window. Files can be reverted to a chosen version of this list. 

## Share & Request Files

You can share an URL to provide access to a document in your Dropbox from *File → Share…*. Optionally set a password required to download the file. Request others to add files to your Dropbox with *File → Request Files…*.

```{note}
Password protected share links are only available for [paid business plans](https://help.dropbox.com/share/set-link-permissions).
```

## Known Limitations

### Comparison With Dropbox Desktop App

The Dropbox desktop app has the following advantages to improve upload performance not available through the public API.
- Server side caching to skip transferring previously uploaded files ([#247](https://github.com/iterate-ch/docs/issues/247)).
- Binary diff uploads transferring only changed contents within a single file.

### Modification Date

The modification date retention is supported for new files uploaded but without the option to adjust the modification date later.

### Restricted Content

Downloads may fail with a `409 Conflict (restricted_content)` error reply for files considered restricted.

```{attention}
The file cannot be transferred because the content is restricted. For example, sometimes there are legal restrictions due to copyright claims.
```

### Will not Save the File or Folder Because of its Name.

Uploads may fail with a `409 (disallowed_name)` error reply for files with certain characters in the filename.

