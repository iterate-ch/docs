Eucalyptus Walrus
===

> [Eucalyptus Walrus](http://open.eucalyptus.com/) is an open source implementation of S3. 

# Connecting

- {download}`Download<https://trac.cyberduck.io/raw-attachment/wiki/help/en/howto/eucalyptus/Eucalyptus%20Walrus%20S3.cyberduckprofile>` the *Eucalyptus Walrus S3 Connection Profile* for preconfigured settings.

Choose *Eucalyptus Walrus S3* from the protocol dropdown menu in the [Open Connection](../../Cyberduck/Connection) or [Bookmark](../../Cyberduck/Bookmarks) settings and enter the hostname of your installation. Refer to [S3](index) in general.

The only difference to regular S3 is that the storage path (endpoint) is assumed to be `/services/Walrus` instead of `/`.

## Login Credentials

Download your credentials ZIP from `ecc.eucalyptus.com`. You can find the access key and secret in the file *eucarc*.

# Distribution

You can enable [Amazon CloudFront (Content Delivery Network) distribution](../../CDN/CloudFront) using *File → Info → Distribution (CDN)*.

# Limitations

- No content distribution ([CDN](../../CDN/index)) configuration.
- No bucket logging configuration.
- No bucket location support.
- Storage class options are not available.