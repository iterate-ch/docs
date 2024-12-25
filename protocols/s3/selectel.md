Selectel S3 Storage
====

```{image} _images/selectel.png
:alt: Selectel Drive Icon
:width: 128px
```

> [Selectel Cloud Storage](https://docs.selectel.ru/en/cloud/object-storage/) is a durable S3 for developers and businesses.

## Connecting

{download}`Download<https://660fd624-6943-4f0e-9a0a-55b811a8e17a.selstorage.ru/Selectel%20S3%20Cloud%20Storage.cyberduckprofile>` the *Selectel S3 Cloud Storage Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

:::{tip}
The container must have virtual-hosted addressing enabled, see the [Detailed instructions for connection](https://docs.selectel.ru/en/cloud/object-storage/tools/cyberduck/) for more details.
:::

### Configure Access

Access can be configured by a user with role _Account Owner_ or _User Administrator_ in Selectel S3.  Create a service user with a role with access to S3 object storage, see [Role Model Access](https://docs.selectel.ru/en/cloud/object-storage/manage/manage-access/) for details.
Issue the user an S3 key.

### Configuration

1. Choose _[Open Connection…](../cyberduck/connection.md)_ or add a _[New Bookmark](../cyberduck/bookmarks.md)_ to save the connection settings.
2. Select the _S3 Selectel_ protocol or alterntively the generic Amazon S3 profile.
3. In the _Server_ field, enter the domain `s3.ru-1.storage.selcloud.ru`, where `ru-1` is the pool that hosts the object storage.
4. In the _Access Key ID_ field, insert the value of the _Access key_ field from your S3 key.
5. In the _Secret Access Key_ field, insert the value of the _Secret key_ field from your S3 key.

## Selectel S3 API Domains

Only authorized access is possible through S3 API domains. You have to use S3-key to work with containers and upload objects via:

- `s3.ru-1.storage.selcloud.ru/<container_name>` domain with Path-Style addressing, used if Virtual-Hosted addressing is not enabled.
- `<container_name>.s3.ru-1.storage.selcloud.ru` domain with Virtual-Hosted addressing, used by default.

We strongly recommend using Virtual-Hosted addressing. In this example, `ru-1` is the pool that hosts the object store.

## Selectel FTP API Domains

- `ftp.ru-1.storage.selcloud.ru` domain, used if you need make a connection using FTP[](../ftp.md).