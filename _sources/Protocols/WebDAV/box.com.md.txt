Box.com
===

> [box](https://box.com/) Simple, secure file sharing and collaboration from anywhere.

# Connecting

## FTP

```{important}
Only available for Box.com business and enterprise accounts
```

Enter the following information in the [bookmark](../../Cyberduck/Bookmarks):

- Protocol: `FTP` or `FTPS`
- Server: `ftp.box.com`
- Username: Your Box account email address
- Password: Your Box account password

## WebDAV

```{warning}
Box.com WebDAV support reached end-of-life at October 25th, 2019
```

1. {download}`Download<https://svn.cyberduck.ch/trunk/profiles/Box.cyberduckprofile>` the *Box Connection Profile* for preconfigured settings.
2. Enter your email address for the username.

Alternatively, enter the following information in the [bookmark](../../Cyberduck/Bookmarks):

- Protocol: `WebDAV (HTTPS)`
- Server: `dav.box.com`
- Username: Your Box account email address
- Password: Your Box account password
- Path: `dav`

# References

- [WebDAV with Box](https://support.box.com/hc/en-us/articles/360043696414-WebDAV-with-Box)
- [Using Box with FTP or FTPS](https://support.box.com/hc/en-us/articles/360043697414-Using-Box-with-FTP-or-FTPS)