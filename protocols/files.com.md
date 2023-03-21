Files.com
====

> [Files.com](https://www.files.com/) is one single API and App for all the Files in your business, no matter where they live.

## Connecting

### REST API

The connection profile allows to login using the *Files.com REST API* supporting two-factor authentication.

- {download}`Download<https://profiles.cyberduck.io/default/Files.com.cyberduckprofile>` the *Files.com Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

### Manual Configuration

#### FTPS

Enter the following information in the [bookmark](../cyberduck/bookmarks.md):

- Protocol: `FTP-SSL (Explicit AUTH TLS)`
- Server: `app.files.com`
- Username: `Your Files.com username`
- Password: `Your Files.com password`

#### WebDAV

Enter the following information in the [bookmark](../cyberduck/bookmarks.md):

- Protocol: `WebDAV (HTTPS)`
- Server: `<subdomain>.files.com`
- Username: `Your Files.com username`
- Password: `Your Files.com password`

## References

- [Connecting via FTP/FTPS](https://www.files.com/docs/integrations/ftp-ftps)
- [Connecting via WebDAV](https://www.files.com/docs/integrations/webdav)