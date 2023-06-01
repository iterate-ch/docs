OVH Public Cloud Storage
====

> With the [OVH Object Storage](https://www.ovh.com/us/public-cloud/storage/object-storage/) cloud solution, you only pay for what you use with no limitation when it comes to size and duration. Thanks to the OpenStack Swift technology, you can store your high-performance data in the OVH cloud environment and instantly access it at any time. This solution is perfect for web projects and can be used to make your objects available through HTTP.

```{seealso}
[hubiC (OVH)](hubic)
```

## Connecting

```{note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

### OpenStack Swift

{download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage.cyberduckprofile>`  the *OVH Public Cloud Storage Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

#### Manual Configuration

You will need to create a new user in the [OVH manager](https://www.ovh.com/manager/cloud/) in *Cloud → Servers → Project → OpenStack*. Choose *Download OpenStack configuration file* (`openrc.sh`) and open it in a text editor. Copy the values `OS_TENANT_ID:OS_USERNAME` for the username from the file.

- Server: `auth.cloud.ovh.net`
- Port: `443`
- Username: `OS_TENANT_ID:OS_USERNAME`
- Password: `Password`. You will find the password in the user list in *Project → OpenStack*.

### S3

Access your containers via S3 by creating an S3 user via *OVHcloud Control Panel*.

- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(bhs).cyberduckprofile>` the *OVH Public Cloud Storage (Beauharnois) Connection Profile* for preconfigured settings.
- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(gra).cyberduckprofile>` the *OVH Public Cloud Storage (Gravelines) Connection Profile* for preconfigured settings.
- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(rbx).cyberduckprofile>` the *OVH Public Cloud Storage (Roubaix) Connection Profile* for preconfigured settings.
- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(sbg).cyberduckprofile>` the *OVH Public Cloud Storage (Strasbourg) Connection Profile* for preconfigured settings.
- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(uk).cyberduckprofile>` the *OVH Public Cloud Storage (London) Connection Profile* for preconfigured settings.
- {download}`Download<https://profiles.cyberduck.io/OVH%20Public%20Cloud%20Storage%20(waw).cyberduckprofile>` the *OVH Public Cloud Storage (Warsaw) Connection Profile* for preconfigured settings.

#### Creating S3 access using the control panel

- Log into your [OVHcloud Control Panel](https://us.ovhcloud.com/manager/).
- Choose a *Standard Object Storage* container from your public cloud project.
- Check the region and install the corresponding connection profile.
- Add an existing user or create a new one.

## Cyberduck CLI

To use a connection, the corresponding profile must be [installed](../../cli/index.md#profiles) with the following parameters using [Cyberduck CLI](https://duck.sh/).

	duck --username OS_TENANT_ID:OS_USERNAME --password PROJECT_USER_PASSWORD --region BHS3 --list ovh://CONTAINERNAME

Alternatively, connect using the default connection profile by specifying the authentication hostname with

	duck --username OS_TENANT_ID:OS_USERNAME --password PROJECT_USER_PASSWORD --region BHS3 --list swift://auth.cloud.ovh.net/CONTAINERNAME

## Containers

You can choose the region when creating a new container with *File → New Folder…*.

![OVH Public Cloud Storage](_images/OVH_Public_Cloud_Storage.png)

## Limitations

- The S3 access is currently limited to the storage class *Standard*.
- Server-side encrypted objects using SSE-C can't be used or downloaded.

## References
- [Manage Object Storage with Cyberduck](https://docs.ovh.com/us/en/storage/manage_object_storage_with_cyberduck/)
- [Configure user access to Horizon](https://docs.ovh.com/us/en/public-cloud/configure_user_access_to_horizon/)
- [Configure S3 access](https://support.us.ovhcloud.com/hc/en-us/articles/10695902938899-How-to-Create-a-Container-in-OVHcloud-S3-Object-Storage)