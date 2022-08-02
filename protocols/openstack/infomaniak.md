Infomaniak
====

![Infomaniak Drive Icon](_images/blue-128.png)

## Infomaniak Public Cloud

- [Test Infomaniak Public Cloud with free tiers](https://www.infomaniak.com/en/hosting/public-cloud)

### Connecting

```{Note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

#### Connection Profiles

Log in to your *Infomaniak OpenStack Swift space* via this preconfigured connection profile:

- {download}`Infomaniak Public Cloud (01) - Cluster1 connection profile<http://profiles.cyberduck.io.s3.amazonaws.com/Infomaniak%20Public%20Cloud%20(01).cyberduckprofile>`

#### Additional Fields Required

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Project:Domain:Username: `Informations available in your Infomaniak manager. Example: PCP-XXXXXX:Default:PCU-XXXXXX`
- Password: `password is the same as the one you use for the OpenStack dashboard`

### References
- [Official Infomaniak Public Cloud documentation](https://docs.infomaniak.cloud)
- [Find out more about Infomaniak Public Cloud](https://www.infomaniak.com/en/hosting/public-cloud)
- [Test Infomaniak Public Cloud with free tiers](https://www.infomaniak.com/en/hosting/public-cloud)

## Infomaniak Swiss Backup

Swiss Backup is a solution that automatically backs up your files, workstations, mobiles, and servers. Your data is stored in Switzerland in Tier 3+ datacenters in at least three different physical locations. Infomaniak is a leading Swiss hosting service provider that is recognized for the reliability of its services and the quality of its 7/7 support in over five languages.

- [Test Swiss Backup free for 90 days](https://www.infomaniak.com/en/swiss-backup)

### Connecting

```{Note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

#### Connection Profiles

Log in to your *Infomaniak OpenStack Swift space* via this preconfigured connection profile:

- {download}`Infomaniak Swiss Backup (01) - Cluster1 connection profile<http://profiles.cyberduck.io.s3.amazonaws.com/Infomaniak%20Swiss%20Backup%20(01).cyberduckprofile>`
- {download}`Infomaniak Swiss Backup (02) - Cluster2 connection profile<http://profiles.cyberduck.io.s3.amazonaws.com/Infomaniak%20Swiss%20Backup%20(02).cyberduckprofile>`
- {download}`Infomaniak Swiss Backup (03) - Cluster3 connection profile<http://profiles.cyberduck.io.s3.amazonaws.com/Infomaniak%20Swiss%20Backup%20(03).cyberduckprofile>`

#### Additional Fields Required

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Project: Domain:Username: `information sent by email when you created your Swiss Backup space`
- Password: `password sent by email when you created your Swiss Backup space`

### References
- [Official Infomaniak documentation](https://www.infomaniak.com/en/support/faq/2284/startup-guide-swiss-backup)
- [Cyberduck connection profile documentation](https://www.infomaniak.com/en/support/faq/2282/swiss-backup-backing-up-files-with-cyberduck)
- [Find out more about Swiss Backup](https://www.infomaniak.com/en/swiss-backup)
- [Test Swiss Backup free](https://www.infomaniak.com/en/swiss-backup)

## Infomaniak kDrive

### Connecting

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `WebDAV (HTTPS)`
- Server: `connect.drive.infomaniak.com`
- Username: `Your kDrive login email.`
- Password:
	- if two-step authentication is not activated, use the password for your Infomaniak account
	- if two-step authentication is activated, generate an [application password](https://manager.infomaniak.com/v3/profile/application-password)

### Known Issues

#### Can't upload files (Mountain Duck)

kDrive doesn't accept uploads with unknown file sizes. Because of this files can't be uploaded within the *Online* mode as the actual file size can't be reported at the beginning of the upload. The *Smart Synchronization* mode can be used instead as a workaround.

### References

- [kDrive: logging in to your Drive via WebDAV](https://www.infomaniak.com/en/support/faq/2409/kdrive-logging-in-to-your-drive-via-webdav)
