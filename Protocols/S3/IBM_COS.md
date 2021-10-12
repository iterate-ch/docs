IBM Cloud Object Storage (COS)
===

```{attention}
- [**Softlayer is now IBM Cloud.**](https://www.ibm.com/cloud/info/softlayer-is-now-ibm-cloud)
- [**IBM Bluemix has been rebranded as IBM Cloud within October 2017.**](https://www.ibm.com/cloud/blog/announcements/bluemix-is-now-ibm-cloudMore)
```

> A highly scalable cloud [storage service](https://www.ibm.com/cloud/object-storage), designed for high durability, resiliency, and security.

# Connecting

## Credentials

Obtain HMAC [credentials](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-uhc-hmac-credentials-main).

> Users can create a set of HMAC credentials as part of a Service Credential with the use of the advanced configuration parameter {"HMAC":true} during credential creation in the console.

## Connection Profiles

Using [Cross Region Endpoints](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints)

- **us-geo:** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/IBM%20COS%20(us-geo).cyberduckprofile>` the *IBM COS (us-geo) Connection Profile* for preconfigured settings.
- **eu-geo:** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/IBM%20COS%20(eu-geo).cyberduckprofile>` the *IBM COS (eu-geo) Connection Profile* for preconfigured settings.
- **ap-geo:** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/IBM%20COS%20(ap-geo).cyberduckprofile>` the *IBM COS (ap-geo) Connection Profile* for preconfigured settings.

# Buckets
When creating a bucket you can choose the [storage class](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-classes).

# References
- [Transfer files with Cyberduck](https://cloud.ibm.com/docs/services/cloud-object-storage/tutorials?topic=cloud-object-storage-cyberduck)
- [Endpoints and storage locations](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints)
- [Comparing IBM Cloud Object Storage to FTP](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-compare-ftp)