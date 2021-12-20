Box.com
===

> [box](https://box.com/) Simple, secure file sharing and collaboration from anywhere.

# Connecting

## Connection Profile

Use the default *Box* profile to connect to your server using the box API.
The default profile allows to connect to account with OAuth login enabled.

## Manual Configuration

### FTP

```{important}
Only available for Box.com business and enterprise accounts
```

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `FTP` or `FTPS`
- Server: `ftp.box.com`
- Username: Your Box account email address
- Password: Your Box account password

### WebDAV

```{warning}
Box.com WebDAV support reached end-of-life at October 25th, 2019
```

1. {download}`Download<https://svn.cyberduck.ch/trunk/profiles/Box.cyberduckprofile>` the *Box Connection Profile* for preconfigured settings.
2. Enter your email address for the username.

Alternatively, enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `WebDAV (HTTPS)`
- Server: `dav.box.com`
- Username: Your Box account email address
- Password: Your Box account password
- Path: `dav`

# Share

```{note}
Only available using the default *Box* connection profile.
```

Create [URL shares](../../cyberduck/share.md#box) for people who are not Box users by using *File → Share...*.

# References

- [WebDAV with Box](https://support.box.com/hc/en-us/articles/360043696414-WebDAV-with-Box)
- [Using Box with FTP or FTPS](https://support.box.com/hc/en-us/articles/360043697414-Using-Box-with-FTP-or-FTPS)