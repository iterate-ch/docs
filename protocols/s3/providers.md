Third-Party Providers
===

:::{contents} Content
:depth: 2
:local:
:::

There are a growing number of third parties besides Amazon offering S3 compatible cloud storage software or solutions.
Here is a non-exhaustive list:

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

## Cloudflare R2

> [Cloudflare R2 Storage](https://www.cloudflare.com/products/r2/) allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.

### Connecting

Supported [regions](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/#available-regions) are:

- `AFR` (Africa)
- `APAC` (Asia Pacific)
- `EEUR` (Eastern Europe)
- `ENAM` (Eastern North America)
- `EU` (European Union)
- `ME` (Middle East)
- `OC` (Oceania)
- `SAM` (South America)
- `WEUR` (Western Europe)
- `WNAM` (Western North America)

### Limitations

The following features are not supported within the [open beta](https://blog.cloudflare.com/r2-open-beta/):
- Specify regions for buckets
- ACLs
- Pre-signed URLs 

### References

- [Cloudflare documentation](https://developers.cloudflare.com/r2/get-started/)

## DreamObject Cloud Storage

> [DreamObjects](http://dreamhost.com/cloud/dreamobjects/) is a cost-effective, public cloud storage service built on top of the open source technology [Ceph](http://ceph.io/). It is compatible with the APIs of [Amazon S3](index.md) and [Swift](../openstack/index.md) based object storage services.

### Limitations

- As `us-west-1` was shut down only `us-east-1` is available for connecting
- View a feature support list in the [API documentation](https://help.dreamhost.com/hc/en-us/articles/217590537-How-To-Use-DreamObjects-S3-compatible-API).
- No support for multipart uploads through Cyberduck.

### References

- [This article describes how to connect Cyberduck to your DreamObjects buckets](https://help.dreamhost.com/hc/en-us/articles/217131247#connecting)
- [The following describes how to use Cyberduck to connect to your DreamObjects account](https://help.dreamhost.com/hc/en-us/articles/217131247-Cyberduck)

## Exoscale

![Exoscale Drive Icon](_images/exoscale.png)

> [Exoscale Simple Object Storage.](https://www.exoscale.com/object-storage/) An S3-compatible object storage service, with zones in Switzerland, Germany, Autria, and Bulgaria.

### Connecting

Connection profiles are available for the following [regions](https://community.exoscale.com/api/sos/):

- Austria (`AT-VIE-1`, `AT-VIE-2`)
- Bulgaria (`BG-SOF-1`)
- Germany (`DE-FRA-1`, `DE-MUC-1`)
- Switzerland (`CH-DK-2`, `CH-GVA-2`)

### Limitations

- No Object tagging
- No Object Lifecycle Management
- No Bucket access logging
- No Conditional writes

### References

- [Exoscale documentation](https://community.exoscale.com/documentation/storage/quick-start/)

## Filebase

> [Filebase](https://docs.filebase.com/) is the first S3-compatible object storage platform that allows you to store data in a secure, redundant, and performant manner across multiple decentralized storage networks.

### References

- [Learn how to backup your data to Filebase using Cyberduck](https://docs.filebase.com/client-configurations/cyberduck)

## IONOS Cloud Object Storage

> IONOS S3 Object Storage is a service offered by IONOS for storing and accessing unstructured data. The Object Storage is fully S3-compliant, which means that it can be used to manage buckets and objects using existing S3 clients.

### Connecting

Connection profiles are available for the following regions:

- Berlin (`eu-central-2`)
- Frankfurt (`eu-central-1`)
- Logrono (`eu-south-2`)

#### Object storage keys

1. Sign into your **IONOS Data Center Designer** and navigate to the **User Manager** via the menu bar **Resource Manager** section.
2. Select a user and click on the **Object Storage Keys** tab on the right.
3. Choose **Generate Key** and confirm the action with **OK**.
The object storage key will be generated automatically.

### References

- [IONOS Cloud documentation](https://docs.ionos.com/cloud/managed-services/s3-object-storage)

## MinIO Cloud Storage

:::{image} _images/MINIO_wordmark.png
:alt: MinIO Logo
:height: 128px
:::

> [MinIO](https://min.io/) is an object storage server built for cloud application developers and DevOps.</br>Store photos, videos, VMs, containers, log files, or any blob of data as objects.

### Connecting

Use the generic S3 profile to connect.

#### Virtual Host Style Requests

Make sure to enable [virtual-host-style requests](https://github.com/minio/minio/tree/master/docs/config#domain) in your MinIO configuration. Alternatively, refer to [Connecting using Deprecated Path Style Requests](index.md#connecting-using-deprecated-path-style-requests).

## Pilvio

Located in Estonia. S3 compatible object storage with perfect cost and reliability ratio. An ideal solution for file, image, video, cad file, backup, or archive storage.

[Pilvio](https://pilvio.com/) is a S3 compatible object storage.

### References

- [Set Up Your Object Storage Space in 4 Steps](https://blog.pilw.io/set-up-your-object-storage-space-in-4-steps/)

## Scaleway Object Storage

> [Scaleway Object Storage](https://www.scaleway.com/docs/object-storage-feature/) is an Object Storage service based on the S3 protocol. It allows you to store any kind of object (documents, images, videos, etc.).

### Connecting

Connection profiles are available for the following regions:

- `nl-ams` (Amsterdam, The Netherlands)
- `fr-par` (Paris, France)
- `pl-waw` (Warsaw, Poland)

### References

- [How to store objects with Object Storage and Cyberduck](https://www.scaleway.com/docs/store-object-with-cyberduck/)

## Seagate Lyve Cloud

> Lyve™ is an edge-to-cloud mass storage platform from Seagate®—built for the distributed enterprise to capture the unstructured data explosion.

### Connection

Use the `S3 (HTTPS)` profile to connect. Available [endpoints](https://help.lyvecloud.seagate.com/en/s3-api-endpoints.html) are:

- US-East-1 (Virginia): `https://s3.us-east-1.lyvecloud.seagate.com`
- US-West-1 (California): `https://s3.us-west-1.lyvecloud.seagate.com`
- AP-Southeast-1 (Singapore): `https://s3.ap-southeast-1.lyvecloud.seagate.com`
- EU-West-1 (London):
`https://s3.eu-west-1.lyvecloud.seagate.com`
- US-Central-2 (Texas):
`https://s3.us-central-2.lyvecloud.seagate.com`

#### Create Access Keys

You have to create service accounts within the *Lyve Cloud console* to use third party tools:

1. [Sign in](https://console.lyvecloud.seagate.com) to your Lyve Cloud via web browser.
2. Select *Service Accounts* from the sidebar menu and choose *Create Service Account*.
3. Enter the name and permissions.
4. Choose *Create*. The access key will be generated and the details of the key will be displayed in a popup window.

:::{note}
The prompt containing the access key information will only be displayed once. Make sure to save the details for future use.
:::

### References

- [Using Cyberduck with Lyve Cloud](https://help.lyvecloud.seagate.com/en/using-cyberduck.html)
- [Using Mountain Duck with Lyve Cloud](https://help.lyvecloud.seagate.com/en/using-mountain-duck.html)

## SFTP To Go

### Connecting

Login to SFTP To Go's dashboard and go to the credentials page:

1. Expand the root credentials to copy the S3 endpoint and secrets.

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- *Protocol:* `Amazon S3`
- *Server:* Copy the bucket from SFTP To Go' dashboard and use them in the following pattern: `<bucket>.s3.amazonaws.com`
- *Access Key ID:* `Access key ID copied from SFTP To Go's dashboard`
- *Secret Access Key:* `Secret access key copied from SFTP To Go's dashboard`
- *Path:* `Bucket name copied from SFTP To Go's dashboard`

### References

- [Connecting via Amazon S3](https://sftptogo.com/docs/how-to-connect/connect-using-amazon-s3)

## Storadera

> [Storadera](https://storadera.com/) is a secure and affordable unlimited data storage for creating archives and backups.

### Connecting

Connection profiles are available for the following regions:

- `eu-central-1` (Amsterdam, Netherlands, Europe)
- `eu-east-1` (Tallinn, Estonia, Europe)

### References

- [How to use Storadera with Cyberduck](https://storadera.com/integrations/cyberduck/)

## Storj DCS

### Credentials

1. Sign into your **Storj DCS** webinterface and navigate to the **Access** section.
2. Choose **Create S3 Credentials**, enter name and permissions, and select buckets.
3. Click **Encrypt My Access** to select the encryption and confirm your choice by selecting **Create my Access**. 

### References

- [How to use Cyberduck and Storj DCS](https://docs.storj.io/dcs/how-tos/how-to-use-cyberduck-and-storj-dcs/)

## Synology C2 Object Storage

> [Synology C2 Object Storage](https://c2.synology.com/en-global/object-storage/overview) provides a secure, S3-compatible, and cost-effective cloud storage solution without API request, download fees, and deletion penalty.

### Connecting

Connection profiles are available for the following regions:

- Frankfurt, Europe (`eu-001`, `eu-002`)
- Seattle, North America (`us-001`, `us-002`)
- Taiwan, APAC (`tw-001`)

### References

- [C2 Object Storage Quick Start Guide](https://kb.synology.com/en-global/C2/tutorial/Quick_Start_C2_Object_Storage)

## More Providers

- [Alibaba](alibaba.md)
- [Aruba Cloud](https://www.cloud.it/)
- [Cloudian HyperStore Appliance](https://cloudian.com/products/hyperstore/)
- [connectria Cloud Storage](https://www.mh.connectria.com/rp/order/cloud_storage_index)
- [DigitalOcean Spaces](digitalocean.md)
- [Garage](https://garagehq.deuxfleurs.fr/)
- [IBM Cloud Object Storage (COS)](https://www.ibm.com/cloud/object-storage)
- [Linode Object Storage](linode.md)
- [NetApp StorageGrid Webscale](https://docs.netapp.com/sgws-114/index.jsp)
- [Oracle Cloud Infrastructure](oraclecloud.md)
- [Outscale (using CEPH Opensource)](https://www.outscale.com/)
- [OVH](../openstack/ovh.md)
- [Scality RS2](scality.md)
- [Seeweb](https://www.seeweb.it/)
- [Spectra BlackPearl Deep Storage Gateway](spectra.md)
- [Swisscom S3 Dynamic Storage](https://www.swisscom.ch/en/business/enterprise/offer/cloud-data-center/dynamic-computing-services.html)
- [Vitanium Cloud](https://vitanium.com/using-vitaniums-object-storage-with-cyberduck/)
- [Vultr Object Storage](https://www.vultr.com/docs/vultr-object-storage#Cyberduck_GUI_tool)
- [Wasabi Storage](wasabi.md)
- [Z1 Storage](https://www.z1storage.com/)