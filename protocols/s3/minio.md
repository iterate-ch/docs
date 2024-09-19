MinIO Cloud Storage
====

:::{image} _images/MINIO_wordmark.png
:alt: MinIO Logo
:height: 128px
:::

> [MinIO](https://min.io/) is an object storage server built for cloud application developers and DevOps.</br>Store photos, videos, VMs, containers, log files, or any blob of data as objects.

## Connecting

Download and install the [generic S3 profile](index.md#generic-s3-profiles).

### Virtual Host Style Requests

:::{attention}
Make sure to enable [virtual-host-style requests](https://github.com/minio/minio/tree/master/docs/config#domain) in your MinIO configuration. Alternatively, refer to [Connecting using Deprecated Path Style Requests](index.md#connecting-using-deprecated-path-style-requests).
:::