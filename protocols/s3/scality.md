Scality RS2
====

> [Scality RING (RS2)](https://www.scality.com/products/ring/) is a commercial object storage product that implements an S3 protocol to connect with. The Protocol is called RS2 in Scality's product line. Scality is used by many providers to implement their cloud storage.

## Connecting

Choose *Amazon S3* from the protocol dropdown menu in the [Open Connection](../../cyberduck/connection.md) or Bookmark settings. Enter the username and password that have been created for you by your provider or IT Organization. Refer to [S3](index.md) in general.

Once connected, the behavior with an S3 account is exactly the same.

## Provider

### Dunkel Cloud Storage

:::{image} _images/Dunkel_Cloud_Storage.png
:alt: Dunkel Cloud Storage Drive Icon
:width: 128px
:::

> [Dunkel Cloud Storage](http://www.dunkel.de/s3/) ist ein S3 kompatibler Cloud Storage in deutschen Rechenzentren. 

Refer also to [S3](index.md) wiki page in general.

#### Connection Profile

The connection profile can be installed from the *Preferences → Profiles* tab.

#### Limitations

- No bucket location support (All data is stored in Germany).
- No bucket logging configuration.
- Storage class options are not available.
- Torrent URLs are not supported.
- No content distribution ([CDN](../../protocols/cdn/index.md)) configuration.

### Seeweb Cloud Object Storage

> [Seeweb Cloud Object Storage](https://www.seeweb.it/en/products/cloud-object-storage) is the Italian storage solution of secure space and traffic for your files.

#### Connection

- *Protocol:* `S3`
- *Server:* `seewebstorage.it`
- *Access Key ID* 
- *Secret Access Key* 

### NetApp StorageGRID

> [NetApp StorageGRID](https://www.netapp.com/data-storage/storagegrid/) is a software-defined object storage suite that supports a wide range of use cases across public, private, and hybrid multi-cloud environments.

#### Connection

Values for hostname, port, credentials, and path have to be created by using a setup wizard or manually using the Grid Manager.

#### References

- [StorageGRID Setup Documentation](https://docs.netapp.com/us-en/storagegrid-118/landing-configure-manage/index.html)

## Limitations

- No content distribution ([CDN](../../protocols/cdn/index.md)) configuration.
- No bucket logging configuration.