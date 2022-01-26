Memset Object Storage
====

![Memset Logo](_images/Memset_Logo.png)

> Memset Memstore is an exciting new long-term storage solution. Based on the OpenStack Object Storage platform, combined with our own impressive infrastructure, Memstore™ is flexible, scalable, easy to use, and secure. We take care of the details from disk space to backups; you simply drag and drop your files and leave everything else to us. You only pay for what you use, whether that be 1GB or 1TB, and there are no license fees or hidden costs. Data replication means that your data is unaffected by hardware failures and you can sleep soundly knowing your data is safe with us.

**Free 5GB Account**</br>
Sign up for a free account that comes with 5GB of storage and 5GB of transfer per month [Memset Object Storage](https://www.memset.com/services/object-storage/).

## Connecting

```{Note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

### Connection Profile

#### Memset 1.0

{download}`Download<https://svn.cyberduck.ch/trunk/profiles/Memset%20(1.0).cyberduckprofile>` the *Memset (1.0) Profile* for preconfigured settings.

Use your Memstore access username (e.g. `mstestaa1.admin`) and password (API key) to log in.

#### Keystone

{download}`Download<https://svn.cyberduck.ch/trunk/profiles/Memset%20(Keystone).cyberduckprofile>` the *Memstore (Keystone) Profile* for preconfigured settings.

Use `admin` for the username, the Memstore name when prompted for the Tenant ID (e.g. `mstestaa1`) and password (API key) to log in.

### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `Swift (OpenStack Object Storage)`
- Server: `auth.storage.memset.com`
- Port: `443`
- Username: Memstore name and username e.g. `mstestaa1.admin`
	- If you are not using the `admin` user then a container name will need to be specified under *More Options*
- Password: `Memstore password (API key)`

![Memstore configuration](_images/Memstore.Swift.Config.png)


## References
- [Documentation and Resources for Developers](https://docs.memset.com/cd/API-%2F-Developer-Resources.199072028.html)
- [Swift Openstack API with Cyberduck](https://docs.memset.com/cd/Swift-OpenStack-API-with-Cyberduck.199072116.html)