Box.com
====

```{image} _images/box.png
:alt: Box Drive Icon
:width: 128px
```

```{tip}
Download [Mountain Duck](https://mountainduck.io/) as an alternative to *Box Drive*.
```

> [Box](https://box.com/) Simple, secure file sharing and collaboration from anywhere.

## Connecting

Use the default *Box* connection profile to connect to your server using the Box API. This allows to have Multi-Factor Authentication enabled for your accout.

### Alternate Connection Options

#### FTP

```{important}
Only available for Box business and enterprise accounts
```

Enter the following information in the [bookmark](../cyberduck/bookmarks.md):

- Protocol: `FTP` or `FTPS`
- Server: `ftp.box.com`
- Username: Your Box account email address
- Password: Your Box account password

#### WebDAV

```{warning}
Box WebDAV support reached end-of-life at October 25th, 2019
```

1. {download}`Download<https://svn.cyberduck.ch/trunk/profiles/Box.cyberduckprofile>` the *Box Connection Profile* for preconfigured settings.
2. Enter your email address for the username.

Alternatively, enter the following information in the [bookmark](../cyberduck/bookmarks.md):

- Protocol: `WebDAV (HTTPS)`
- Server: `dav.box.com`
- Username: Your Box account email address
- Password: Your Box account password
- Path: `dav`

## Share

```{note}
Only available using the default *Box* connection profile.
```

Create download and upload [shares](../cyberduck/share.md#box) of files or folders for people who are not Box users by using *File → Share...*.

## Known Limitations

### Modification Date

The modification date retention is supported for new files uploaded but without the option to adjust the modification date later.

## References

- [WebDAV with Box](https://support.box.com/hc/en-us/articles/360043696414-WebDAV-with-Box)
- [Using Box with FTP or FTPS](https://support.box.com/hc/en-us/articles/360043697414-Using-Box-with-FTP-or-FTPS)
