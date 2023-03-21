Enter Cloud Suite Object Storage
====

> [Enter Cloud Suite Object Storage](https://www.entercloudsuite.com/en/) a Pay-Per-Use Storage provides IaaS public object storage that you can use to archive large amounts of data in a variety of formats in the cloud. You only pay for the space and time you use – starting at 0.075€ per Gb per month – and can even archive data for very short periods of time.

## Connecting

### Connection Profile

- {download}`Download<https://profiles.cyberduck.io/default/Enter%20Cloud%20Suite.cyberduckprofile>` the *Enter Cloud Suite (Keystone) Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

Use the Tenant ID `email` and password to login. See [API Access](https://cm.entercloudsuite.com/project/access_and_security/).

![Enter Cloud Suite](_images/entercloudsuite.com.png)

### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `Swift (OpenStack Object Storage)`
- Server: `api.entercloudsuite.com`
- Port: `443`
- Username: *Enter Cloud Suite* `credentials email`
- Password: *Enter Cloud Suite* `credentials password`
- Tenant: `Tenant ID` from the [OpenStack RC File](https://cm.entercloudsuite.com/project/access_and_security/).