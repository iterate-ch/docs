Oracle Cloud Infrastructure
====

:::{image} _images/OCI_Object_Storage.png
:alt: Oracle Drive Icon
:width: 128px
:::

> [Oracle Cloud Infrastructure (OCI)](https://oracle.com/cloud) provides two separate Object Storage solutions: *OCI Object Storage* and *OCI Object Storage Classic*. Both of them can be accessed using Cyberduck.

![Oracle Cloud Marketplace Badge](_images/cloud-mrktplc-badge.png)

## OCI Object Storage

### Connecting

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

For connecting to OCI Object Storage, Cyberduck version 6.4.0 or later is required. You need to use the [OCI Amazon S3 Compatible API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm).

Follow these instructions:
1. Create an Amazon S3 Compatibility API key by following the instructions within the [Oracle Cloud Documentation](https://docs.oracle.com/en-us/Content/Identity/Tasks/managingcredentials.htm#Working2).
2. [Install](../profiles/index.md#installation) the connection profile for the [region](https://docs.cloud.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) you want to connect to
    - {download}`OCI Object Storage (ap-sydney-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-sydney-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-melbourne-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-melbourne-1).cyberduckprofile>`
    - {download}`OCI Object Storage (sa-saopaulo-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(sa-saopaulo-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ca-montreal-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ca-montreal-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ca-toronto-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ca-toronto-1).cyberduckprofile>`
    - {download}`OCI Object Storage (eu-frankfurt-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(eu-frankfurt-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-hyderabad-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-hyderabad-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-mumbai-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-mumbai-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-osaka-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-osaka-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-tokyo-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-tokyo-1).cyberduckprofile>`
    - {download}`OCI Object Storage (eu-amsterdam-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(eu-amsterdam-1).cyberduckprofile>`
    - {download}`OCI Object Storage (me-jeddah-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(me-jeddah-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-seoul-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-seoul-1).cyberduckprofile>`
    - {download}`OCI Object Storage (ap-chuncheon-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(ap-chuncheon-1).cyberduckprofile>`
    - {download}`OCI Object Storage (eu-zurich-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(eu-zurich-1.cyberduckprofile>`
    - {download}`OCI Object Storage (uk-london-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(uk-london-1).cyberduckprofile>`
    - {download}`OCI Object Storage (us-ashburn-1).cyberduckprofile<https://profiles.cyberduck.io/OCI%20Object%20Storage%20(us-ashburn-1).cyberduckprofile>`
3. Create a new bookmark and select the connection profile installed as the protocol.
4. Update the *Server* field and replace `<namespace>` with your tenancy's namespace (For more information about namespaces, and ways to find your namespace refer to the [Oracle Cloud Documentation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm))
5. Enter the *Access Key* that you obtained while creating *Amazon S3 Compatible API Key*
6. Enter the *Secret Key* that you obtained while creating *Amazon S3 Compatible API Key*

## OCI Object Storage Classic

### Connecting

Follow these instructions:

1. {download}`Download<https://trac.cyberduck.io/attachment/wiki/help/en/howto/oraclecloud/Oracle%20Storage%20Cloud.cyberduckprofile>` the Oracle Storage Cloud profile for preconfigured settings using the `/auth/v1.0` authentication context.
2. Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):
	- **Protocol**: Swift (OpenStack Object Storage)
	- **Server**: `IdentityDomain.storage.oraclecloud.com`. For example, this is `cyduck.storage.oraclecloud.com`
	- **Username**: `ServiceName-IdentityDomain:UserName`. For example this is `Storage-cyduck:dkocher@cyberduck.io`
	- **Password**: Oracle Cloud Password
	- **Tenant**: Oracle Cloud Username
 	- OCI Object Storage Classic Regions
		- us2: Chicago, IL
		- us6: Ashburn, VA
		- em2: Amsterdam
		- em3: UK

### References

- [Using Cyberduck and duck CLI to access Oracle Cloud Infrastructure Classic Storage](https://medium.com/oracledevs/using-cyberduck-and-duck-cli-to-access-oracle-cloud-infrastructure-classic-storage-edfeb04c82c4)