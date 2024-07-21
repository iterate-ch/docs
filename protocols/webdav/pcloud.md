pCloud
====

> [pCloud](https://www.pcloud.com/) is encrypted cloud storage, where you can store your personal files, backup your PC or share your business documents with your colleagues.

## Connecting

```{attention}
WebDAV access is only available for paid plans.
```

### Connection Profiles

```{note}
Connection profiles can be installed from *Preferences → Profiles*.
```

- **pCloud Europe (Luxemburg):** {download}`Download<https://profiles.cyberduck.io/pCloud%20Europe%20(Luxemburg).cyberduckprofile>` the *pCloud Europe (Luxemburg) Connection Profile* for preconfigured settings.
- **pCloud Texas (USA):** {download}`Download<https://profiles.cyberduck.io/pCloud%20Texas%20(USA).cyberduckprofile>` the *pCloud Texas (USA) Connection Profile* for preconfigured settings.	

### Manual Configuration

#### Data Region: USA (Texas)

- Server: `https://webdav.pcloud.com`
- Port: `443`
- Username: pCloud login Email
- Password: pCloud login password

#### Data Region: Europe (Luxemburg)

- Server: `https://ewebdav.pcloud.com`
- Port: `443`
- Username: pCloud login Email
- Password: pCloud login password

## Interoperability

Using Mountain Duck and pCloud Client simultaneously can cause issues for the pCloud Client. The Client requires an older version of the device driver than Mountain Duck and can't deal with the newer version installed by Mountain Duck. 

```{note}
Reported for pCloud Client version 4.0.0 (Windows).
```

## References

- [pCloud via WebDAV ansprechen](https://www.techstream.at/pcloud-via-webdav-ansprechen-geht-das/)