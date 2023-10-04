Infomaniak kDrive
====

> kDrive is an online platform which enables you to retain a copy of your files and share them with employees.

### Connecting

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `WebDAV (HTTPS)`
- Server: `connect.drive.infomaniak.com`
- Username: `Your kDrive login email.`
- Password:
    - If two-step authentication is not activated, use the password for your Infomaniak account
    - If two-step authentication is activated, generate an [application password](https://manager.infomaniak.com/v3/profile/application-password)

### Known Issues

#### Can't upload files (Mountain Duck)

kDrive doesn't accept uploads with unknown file sizes. Because of this files can't be uploaded within the *Online* mode as the actual file size can't be reported at the beginning of the upload. The *Smart Synchronization* mode can be used instead as a workaround.

### References

- [kDrive: logging in to your Drive via WebDAV](https://www.infomaniak.com/en/support/faq/2409/kdrive-logging-in-to-your-drive-via-webdav)
