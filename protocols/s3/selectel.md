Selectel S3 Storage
====

```{image} _images/selectel.png
:alt: Selectel Drive Icon
:width: 128px
```

> [Selectel Cloud Storage](https://docs.selectel.ru/en/cloud/object-storage/) is a durable S3 for developers and businesses.

## Connecting

- Configure access.
- Configure client.

### Configure Access

Access can be configured by a user with role Account Owner or User Administrator in Selectel S3.
Create a service user with a role with access to S3 object storage, see Role Model Access for details.
Issue the user an S3 key.

### Configuration

- Install Cyberduck client.
- Launch Cyberduck and click New Connection.
- Select the S3 Selectel (or the Amazon S3 profile).
- In the _Server_ field, enter the domain `s3.ru-1.storage.selcloud.ru`, where ru-1 is the pool that hosts the object storage.
- In the _Access Key ID_ field, insert the value of the Access key field from your S3 key.
- In the _Secret Access Key_ field, insert the value of the Secret key field from your S3 key.
- Press Connect.

{download}`Download<https://660fd624-6943-4f0e-9a0a-55b811a8e17a.selstorage.ru/Selectel%20S3%20Cloud%20Storage.cyberduckprofile>` the *Selectel S3 Cloud Storage Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

To work with this profile, the container must have Virtual-Hosted addressing enabled, see the [Detailed instructions for connection](https://docs.selectel.ru/en/cloud/object-storage/tools/cyberduck/) for more details.

## Selectel S3 API Domains⁠

Only authorized access is possible through S3 API domains. You have to use S3-key to work with containers and upload objects via:

- `s3.ru-1.storage.selcloud.ru/<container_name>` domain with Path-Style addressing, used if Virtual-Hosted addressing is not enabled.
- `<container_name>.s3.ru-1.storage.selcloud.ru` domain with Virtual-Hosted addressing, used by default.

We strongly recommend using Virtual-Hosted addressing.
Here ru-1 is the pool that hosts the object store.

## Selectel FTP API Domains⁠

- `ftp.ru-1.storage.selcloud.ru` domain, used if you need make a connect via ftp-protocol.
