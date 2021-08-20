Swift (OpenStack Object Storage)
===

# Connecting

Connect to a [Swift (OpenStack Object Storage)](http://docs.openstack.org/Swift/latest) installation. Choose *Swift (OpenStack Object Storage)* from the list of protocols.

## Authentication Context Path

### Authetication with `devauth` for context `/v1.0`

Legacy authentication option.

- {download}`Download<https://svn.cyberduck.ch/trunk/profiles/Openstack%20Swift%20(v1).cyberduckprofile>` the *Openstack Swift (v1) profile* for preconfigured settings.

### Authentication with `swauth`

Legacy authentication option.

- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Swauth).cyberduckprofile>` the *Openstack Swift (Swauth HTTPS) profile* for preconfigured settings.
- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Swauth%20HTTP).cyberduckprofile>` the *Openstack Swift (Swauth HTTP)* profile for preconfigured settings.

### Authentication with `Keystone 2.0` for context `/v2.0/tokens`

To get the login tokens from an OpenStack Identity service no configuration change is needed. You will get prompted to provide the tenant name with a *Provide additional login credentials* prompt or can provide it with the username in the format `<tenant>:<user>`.

Bundled by default since Cyberduck version 4.4.4.

- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Keystone%202).cyberduckprofile>` the *Openstack Swift (Keystone 2) profile* for preconfigured settings.

If you have a Swift installation without SSL configured, you need an optional connection profile to connect using HTTP only without transport layer security.

- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Keystone%202%20HTTP).cyberduckprofile>` the *Openstack Swift (Keystone 2 HTTP) profile* for preconfigured settings.

### Authentication with `Keystone 3.0` for context `/v3/tokens`

Bundled by default since Cyberduck version 4.8.

- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Keystone%203).cyberduckprofile>` the *Openstack Swift (Keystone 3) profile* for preconfigured settings.

If you have a Swift installation without SSL configured, you need an optional connection profile to connect using HTTP only without transport layer security.

- {download}`Download<https://svn.cyberduck.io/trunk/profiles/Openstack%20Swift%20(Keystone%203%20HTTP).cyberduckprofile>` the *Openstack Swift (Keystone 3 HTTP) profile* for preconfigured settings.

You will get prompted to provide the project name with a *Provide additional login credentials prompt* or can provide it with the username in the format `<project>:<user>`.

## Regions

Multiple regions are supported when authenticating with a Keystone (2.0) identity endpoint. Containers from all regions are displayed in the browser. Choose *View → Column → Region* to display the region in the browser.

## Container

On your first login, you will need to create at least one container (folder) to put your content in. Choose *File → New Folder (MacOS `⌘N` Windows `Ctrl+N`)* and specify a name. After the container has been created, you may start adding your content to the storage platform.

![Create Container](_images/Create_Container.png)

# Cyberduck CLI

Connect with [Cyberduck CLI](https://duck.sh/) usingthe default connection profile using authentication with `Keystone 2.0` for context `/v2.0/tokens` with

	duck --username OS_TENANT_ID:OS_USERNAME --password PASSWORD  --list swift://SWIFT_KEYSTONE_AUTH_SERVER/CONTAINERNAME

Refer to the [Cyberduck CLI](../../CLI/index) documentation for more operations.

# Third Party Providers

- [Rackspace Cloud Files (US & UK)](CloudFiles) with [Akamai CDN](../../CDN/Akamai)
- [Internap AgileFILES](Internap)
- [Cloud.ca Object Store](Cloud.ca)
- [Memset Memstore Object Storage](Memset)
- [Enter Cloud Suite](Enter_Cloud_Suite)
- [Oracle Storage Cloud Service](../S3/Oracle_Cloud#oci-object-storage-classic)
- [Oktawave Cloud Storage](Oktawave)
- [SwiftStack](SwiftStack)
- [RunAbove](https://runabove.readthedocs.io/en/latest/en/-posts/2014-04-22-how-to-use-cyberduck-with-openstack-swift/)
- [Cloud A](Cloud_A)
- [AURO](AURO)
- [OVH](OVH)
- [HubiC (OVH)](HubiC)
- [Zetta.IO](Zetta.IO)
- [Selectel Cloud Storage](Selectel)
- [EMC Elastic Cloud Storage](EMC)
- [Infomaniak](Infomaniak)
- [IDrive® Cloud](../S3/IDrive_Cloud#open-stack-swift)
- [OpenStack FlexCloud](FlexCloud)

# Temporary URLs

A private object stored in OpenStack Swift can be made publicly available for a limited time using a signed URL. The signed URL can be used by anyone to download the object, yet it includes a date and time after which the URL will no longer work. Copy the signed URL from *Edit → Copy URL→ Signed URL*.

- **Rackspace** A value must be set on your account metadata for `X-Account-Meta-Temp-Url-Key`.

# Large Uploads

Supported using Static Large Object segmentation. Files larger than 2GB are uploaded in segments using the default threshold. The upload chunk size is 100MB by default with a maximum of 5 concurrent connections. The number of connections used can be limited using the toggle in the lower right of the transfer window.

Large uploads can be resumed when interrupted.

# Distribution (CDN)

You can CDN enable the container using *File → Info → Distribution (CDN)* if supported by the provider.

# Preferences

## Large Upload Segment Size

You can set the [hidden option](../../Cyberduck/Preferences#hidden-configuration-option) `openstack.upload.largeobject.size` for the segment size in `bytes` (Issue #9134).

# Known Issues

- <del>Authentication failure with ec2-credentials</del> (Issue #7754)

## Multiple OpenStack Swift containers in different regions with the same name

Browsing containers will be erratic. As a workaround, browse a region by using a [connection profile](../../Cyberduck/Profiles) limited to a single region as with [Rackspace Cloudfiles region profiles](CloudFiles#profiles-for-a-single-region).

## In Finder.app, creating a new top-level folder in OpenStack Swift will not allow to rename it from `untitled folder`

<del>Because OpenStack Swift does not allow to rename containers this operation will fail.</del></br>As of Cyberduck version 2.2 the new bucket is created only after renaming in Finder. Make sure to choose a filename with no whitespace.