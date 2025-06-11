Linode Object Storage
===

> S3-compatible [Linode Object Storage](https://www.linode.com/products/object-storage/) makes it easy and more affordable to manage unstructured data such as content assets, as well as sophisticated and data-intensive storage challenges around artificial intelligence and machine learning.

## Connecting

### Connection Profile

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

Connection profiles for the following regions are available.

- [Linode Object Storage (au-mel-1)(e2)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28au-mel-1%29%28e2%29.cyberduckprofile)
- [Linode Object Storage (br-gru-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28br-gru-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (de-fra-1)(e3)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28de-fra-1%29%28e3%29.cyberduckprofile)
- [Linode Object Storage (ap-south-1)(e0)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28ap-south-1%29%28e0%29.cyberduckprofile)
- [Linode Object Storage (es-mad-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28es-mad-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (eu-central-1)(e0)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28eu-central-1%29%28e0%29.cyberduckprofile)
- [Linode Object Storage (fr-par-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28fr-par-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (gb-lon-1)(e3)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28gb-lon-1%29%28e3%29.cyberduckprofile)
- [Linode Object Storage (id-cgk-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28id-cgk-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (in-bom-1)(e3)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28in-bom-1%29%28e3%29.cyberduckprofile)
- [Linode Object Storage (in-maa-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28in-maa-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (it-mil-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28it-mil-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (jp-osa-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28jp-osa-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (nl-ams-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28nl-ams-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (se-sto-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28se-sto-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (sg-sin-1)(e2)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28sg-sin-1%29%28e2%29.cyberduckprofile)
- [Linode Object Storage (us-east-1)(e0)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-east-1%29%28e0%29.cyberduckprofile)
- [Linode Object Storage (us-iad-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-iad-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-iad-2)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-iad-2%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-lax-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-lax-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-mia-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-mia-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-ord-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-ord-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-sea-1)(e1)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-sea-1%29%28e1%29.cyberduckprofile)
- [Linode Object Storage (us-sea-9)(e3)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-sea-9%29%28e3%29.cyberduckprofile)
- [Linode Object Storage (us-southeast-1)(e0)](https://profiles.cyberduck.io/Linode%20Object%20Storage%20%28us-southeast-1%29%28e0%29.cyberduckprofile)

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
