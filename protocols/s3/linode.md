Linode Object Storage
===

> S3-compatible [Linode Object Storage](https://www.linode.com/products/object-storage/) makes it easy and more affordable to manage unstructured data such as content assets, as well as sophisticated and data-intensive storage challenges around artificial intelligence and machine learning.

## Connecting

### Connection Profile

```{note}
Connection profiles can be installed from *Preferences → Profiles*..
```

- **Linode Object Storage (France, Paris)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(fr-par-1).cyberduckprofile>` the *Linode Object Storage (Paris) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Milan, Italy)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(it-mil-1).cyberduckprofile>` the *Linode Object Storage (Milan) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Singapore)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(ap-south-1).cyberduckprofile>` the *Linode Object Storage (Singapore) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Frankfurt, Germany)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(eu-central-1).cyberduckprofile>` the *Linode Object Storage (Frankfurt) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Newark, NJ, USA)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(us-east-1).cyberduckprofile>` the *Linode Object Storage (Newark) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Atlanta, GA, USA)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(us-southeast-1).cyberduckprofile>` the *Linode Object Storage (Atlanta) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Washington, DC, USA)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(us-iad-1).cyberduckprofile>` the *Linode Object Storage (Washington) Connection Profile* for preconfigured settings.
- **Linode Object Storage (Chicago, IL, USA)** {download}`Download<https://profiles.cyberduck.io/Linode%20Object%20Storage%20(us-ord-1).cyberduckprofile>` the *Linode Object Storage (Chicago) Connection Profile* for preconfigured settings.

### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md). Choose the endpoint based on the bucket location. Refer to [Availability](https://www.linode.com/docs/products/storage/object-storage/)

- Protocol: `Amazon S3`
- Server: `us-southeast-1.linodeobjects.com, us-east-1.linodeobjects.com, eu-central-1.linodeobjects.com, ap-south-1.linodeobjects.com`
- Access Key ID: `<your access key>`
- Secret Access Key: `<your secret access key>`

### Generate Access Keys

You have to generate an access key before you can connect to Linode Object storage:

1. Log into the [Linode Cloud Manager](https://cloud.linode.com/).
2. Click on the *Object Storage* link in the sidebar, navigate to the *Access Keys* tab, and select *Create an Access Key*. 
3. If you haven't enabled Object Storage till now you will be prompt to confirm that you want to *Enable Object Storage*.

Within the *Create an Access Key* menu:

- Set a label as a reference for the key
- Enable *Limited Access* to limit granted permissions per buckets
- Select *Submit* to generate the key

After submitting a window will be displayed containing the *Access Key* and *Secret Key*. 

```{note}
The window will only be displayed once and the *Secret Key* cannot be retrieved once the window is closed!
Make sure to keep the credential somewhere safe.
```

## References

- [Linode Object Storage Documentation](https://www.linode.com/docs/products/storage/object-storage/)
- [Using Cyberduck with Object Storage](https://www.linode.com/docs/products/storage/object-storage/guides/cyberduck/)
