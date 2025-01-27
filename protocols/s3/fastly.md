Fastly Object Storage
====

> [Fastly Object Storage](https://www.fastly.com/products/storage) Fastly Object Storage operates as a drop-in replacement for the S3 API with zero egress costs.

## Connecting

### Connection Profile

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

Download the desired region for the Hetzner Object Storage Connection Profile with preconfigured settings.

- **eu-central** {download}`Fastly Object Storage (eu-central).cyberduckprofile<https://profiles.cyberduck.io/Fastly%20Object%20Storage%20(eu-central).cyberduckprofile>`
- **us-east** {download}`Fastly Object Storage (us-east).cyberduckprofile<https://profiles.cyberduck.io/Fastly%20Object%20Storage%20(us-east).cyberduckprofile>`
- **us-west** {download}`Fastly Object Storage (us-west).cyberduckprofile<https://profiles.cyberduck.io/Fastly%20Object%20Storage%20(us-west).cyberduckprofile>`

### Access Keys

You have to generate an access key with *Read and write* permissions before you can connect:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to Resources → https://manage.fastly.com/resources/object-storage.
3. Click Create key and copy the _Access Key_ and _Secret Key_.


## References
- [Fastly Documentation](https://docs.fastly.com/en/guides/working-with-object-storage#working-with-the-s3-compatible-api)
