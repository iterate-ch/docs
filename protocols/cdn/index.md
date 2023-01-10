Content Delivery Network (CDN) Configuration
====

```{toctree}
:hidden:
:titlesonly:
akamai
cloudfront
keycdn
```

A content delivery network or content delivery network (CDN) allows the distribution of files from locations all over the world using a network of edge locations. Requests for files are automatically routed to the nearest edge location. Two of the main market players are supported from within Cyberduck with a simple to use interface to enable distributions with a single click of a button.

Using the [Info](../../cyberduck/info.md) panel, the following content distribution networks (CDN) can be enabled:

- [Amazon CloudFront](cloudfront.md)
- [Akamai](akamai.md)
- [KeyCDN](keycdn.md)

## Logging & Analytics

Configuration for the delivery of access logs can be configured from within Cyberduck in the [Info window](../../cyberduck/info.md) for [S3](../s3/index.md), [Google Cloud Storage](../googlecloudstorage.md) and [Amazon CloudFront](cloudfront.md) CDN distributions. The server create a massive amount of log files which is best analyzed with a third-party service.

## Amazon CloudFront

- Add a download or streaming CDN configuration to your [S3](../s3/index.md) bucket.
- Connect to any server using FTP, SFTP or WebDAV and configure it as the origin of a new [Amazon CloudFront](cloudfront.md) CDN distribution.

## Akamai

When connected to [Rackspace Cloudfiles](../openstack/cloudfiles.md), configure [Akamai](akamai.md) content distribution.
