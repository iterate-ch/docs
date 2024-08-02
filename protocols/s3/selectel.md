Selectel S3 Storage
====

```{image} _images/selectel.png
:alt: Selectel Drive Icon
:width: 128px
```

> [Selectel Cloud Storage](https://docs.selectel.ru/en/cloud/object-storage/) is a durable S3 for developers and businesses.

## Connecting

The integration Cyberduck with Selectel can be operated through a graphical or console client via the S3 API.

- Configure access.
- Configure client.

### Configure access

Access can be configured by a user with role Account Owner or User Administrator in Selectel S3.

Create a service user with a role with access to S3 object storage, see Role Model Access for details.
Issue the user an S3 key.

### Customize the client⁠

- Install Cyberduck client.
- Launch Cyberduck and click New Connection.
- Select the Amazon S3 profile. To work with this profile, the container must have Virtual-Hosted addressing enabled, see the Amazon S3 instructions in the Cyberduck documentation for more details.
- In the Server field, enter the domain s3.ru-1.storage.selcloud.ru, where ru-1 is the pool that hosts the object storage.
- In the Access Key ID field, insert the value of the Access key field from S3-key.
- In the Secret access key field, insert the value of the Secret key field from the S3 key.
- Press Connect.

> [Detailed instructions for connection](https://docs.selectel.ru/en/cloud/object-storage/tools/cyberduck/)

## Selectel S3 API Domains⁠

Only authorized access is possible through S3 API domains. You have to use S3-key to work with containers and upload objects via:

- ```s3.ru-1.storage.selcloud.ru/<container_name>``` domain with Path-Style addressing, used by default if Virtual-Hosted addressing is not enabled.
- ```<container_name>.s3.ru-1.storage.selcloud.ru``` domain with Virtual-Hosted addressing, used if Virtual-Hosted addressing is enabled in container settings.

Here ru-1 is the pool that hosts the object store.
