Content Delivery Network (CDN) Configuration
===

```{toctree}
:hidden:

Akamai
CloudFront
KeyCDN
```

A content delivery network or content delivery network (CDN) allows the distribution of files from locations all over the world using a network of edge locations. Requests for files are automatically routed to the nearest edge location. Two of the main market players are supported from within Cyberduck with a simple to use interface to enable distributions with a single click of a button.

Using the [Info](../Cyberduck/Info) panel, the following content distribution networks (CDN) can be enabled:

- [Amazon CloudFront](CloudFront)
- [Akamai](Akamai)
- [KeyCDN](KeyCDN)

## Logging & Analytics

Configuration for the delivery of access logs can be configured from within Cyberduck in the [Info window](../Cyberduck/Info) for [S3](../Protocols/S3/index), [Google Cloud Storage](../Protocols/Google_Cloud_Storage) and [Amazon CloudFront](CloudFront) CDN distributions. The server create a massive amount of log files which is best analyzed with a third-party service.

# Amazon CloudFront

- Add a download or streaming CDN configuration to your [S3](../Protocols/S3/index) bucket.
- Connect to any server using FTP, SFTP or WebDAV and configure it as the origin of a new [Amazon CloudFront](CloudFront) CDN distribution.

# Akamai

When connected to [Rackspace Cloudfiles](../Protocols/OpenStack/CloudFiles), configure [Akamai](Akamai) content distribution.

