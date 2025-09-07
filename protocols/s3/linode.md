Linode Object Storage
===

> S3-compatible [Linode Object Storage](https://www.linode.com/products/object-storage/) makes it easy and more affordable to manage unstructured data such as content assets, as well as sophisticated and data-intensive storage challenges around artificial intelligence and machine learning.

## Connecting

### Connection Profile

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md). Choose the endpoint based on the bucket location. Refer to [Availability](https://www.linode.com/docs/products/storage/object-storage/)

- **Protocol**: `Amazon S3`
- **Server**: `us-southeast-1.linodeobjects.com`, `us-east-1.linodeobjects.com`, `eu-central-1.linodeobjects.com`, `ap-south-1.linodeobjects.com`
- **Access Key ID**: your access key
- **Secret Access Key**: your secret access key

### Generate Access Keys

You have to generate an access key before you can connect to Linode Object storage:

1. Log into the [Linode Cloud Manager](https://cloud.linode.com/).
2. Click on the *Object Storage* link in the sidebar, navigate to the *Access Keys* tab, and select *Create an Access Key*. 
3. If you haven't enabled Object Storage till now you will be prompt to confirm that you want to *Enable Object Storage*.

Within the *Create an Access Key* menu:

1. Set a label as a reference for the key
2. Enable *Limited Access* to limit granted permissions per buckets
3. Select *Submit* to generate the key

After submitting a window will be displayed containing the *Access Key* and *Secret Key*. 

:::{tip}
The window will only be displayed once and the *Secret Key* cannot be retrieved once the window is closed. Make sure to keep the credential somewhere safe.
:::

## References

- [Linode Object Storage Documentation](https://www.linode.com/docs/products/storage/object-storage/)
- [Using Cyberduck with Object Storage](https://www.linode.com/docs/products/storage/object-storage/guides/cyberduck/)
