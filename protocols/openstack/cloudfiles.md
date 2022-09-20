Rackspace Cloud Files
====

![Cloud Files Icon](_images/cloudfiles_icon.png)

> Cloud Files, powered by OpenStack®, provides easy-to-use online storage for files and media which can be delivered globally at blazing speeds over Akamai's content delivery network (CDN).

[Signup](https://cart.rackspace.com/cloud/) and connect to your [Rackspace Cloud Files](http://www.rackspace.com/openstack/public/files) account. You must make sure you have generated a valid API Access Key using the control panel available at [manage.rackspacecloud.com](https://manage.rackspacecloud.com/).

## Connecting

```{note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

### Connection Profiles

- **Rackspace US:** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/default/Rackspace%20US.cyberduckprofile>` the *Rackspace US Connection Profile* for preconfigured settings. Containers from regions *DFW, ORD, IAD, HKG* and *SYD* are displayed in the browser.
- **Rackspace UK:** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20UK.cyberduckprofile>` the *Rackspace UK Connection Profile* for preconfigured settings. Containers from regions *LON* are displayed in the browser.

#### Profile for a Single Region

- **Rackspace US (DFW):** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20US%20(DFW).cyberduckprofile>` the *Rackspace US (DFW) Connection Profile* for preconfigured settings. Containers from regions *DFW* are displayed in the browser.
- **Rackspace US (ORD):** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20US%20(ORD).cyberduckprofile>` the *Rackspace US (ORD) Connection Profile* for preconfigured settings. Containers from regions *ORD* are displayed in the browser.
- **Rackspace US (IAD):** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20US%20(IAD).cyberduckprofile>` the *Rackspace US (IAd) Connection Profile* for preconfigured settings. Containers from regions *IAD* are displayed in the browser.
- **Rackspace US (HKG):** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20US%20(HKG).cyberduckprofile>` the *Rackspace US (HKG) Connection Profile* for preconfigured settings. Containers from regions *HKG* are displayed in the browser.
- **Rackspace US (SYD):** {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Rackspace%20US%20(SYD).cyberduckprofile>` the *Rackspace US (SYD) Connection Profile* for preconfigured settings. Containers from regions *SYD* are displayed in the browser.

### Manual Configuration

Alternatively, enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- Protocol: `Swift (OpenStack Object Storage)`
- Server: `lon.auth.api.rackspacecloud.com`
- Port: `443`

## Additional Information

### Containers

You can create a new top-level container using *File → New Folder... (MacOS `⇧⌘N` Windows `Ctrl+Shift+N`)*. You can select from regions *DFW, ORD, HKG* and *SYD*.

![Create Container](_images/Create_Container.png)

### Folders

Creating a folder inside a container will create a placeholder object named after the directory that has no data content and the MIME type `application/x-directory`.

### Distribution

You can enable [Akamai CDN (Content Delivery Network) distribution](../../protocols/cdn/akamai.md) for a selected container using *File → Info → Distribution (CDN)*. Choose *Enable Access Logging* to save their raw CDN weblogs to your Cloud Files storage account.

#### Logging

You can enable private container access logging to `.ACCESS_LOGS` by adding the metadata `X-Container-Meta-Access-Log-Delivery` name with a value of `true` to the container. Choose *File → Info → Metadata*. To enable access logs for CDN enabled, refer to [distribution access logging](../../protocols/cdn/akamai.md#distribution-access-logging).

### Public URLs

You can access all URLs (including from [CDN](../../protocols/cdn/akamai.md) configurations) from the menu Edit → Copy URL and File → Open URL. 

```{note}
You must first open *File → Info → Distribution (CDN)* before these URLs are available.
```

![Copy URLs](_images/Copy_URLs.png)

### Metadata

You can add [custom HTTP headers](../../cyberduck/info.md#metadata-http-headers) to files to store metadata. Choose *File → Info → Metadata* to edit custom headers.

## Limitations

- No resumable transfers

### Default Metadata

Currently only possible using a [hidden configuration option](../../cyberduck/preferences.md#hidden-configuration-options) you can define default headers to be added for uploads. Multiple headers must be separated using a whitespace delimiter. Key and value of a header are separated with `=`. For example, if you want to add a HTTP header for Cache-Control and one named `Creator` you would set

	defaults write ch.sudo.cyberduck openstack.metadata.default "Cache-Control=public,max-age=86400 Creator=Cyberduck"