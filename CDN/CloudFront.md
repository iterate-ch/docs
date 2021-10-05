Amazon CloudFront Support
===

Amazon CloudFront delivers your static and streaming content using a global network of edge locations. Requests for your objects are automatically routed to the nearest edge location, so content is delivered with the best possible performance. You can enable download or streaming distributions using *File → Info → Distribution* for a [S3](../Protocols/S3/index) bucket or a custom origin distribution for any other source.

# Subscription

You must [signup](http://aws.amazon.com/cloudfront/) for Amazon CloudFront first. You pay only for the data transfer and requests that you actually use.

# Permissions

Make sure your objects in the bucket you want to enable distribution for are world-readable. In *File → Info → Permissions* give `READ` permission to *Everyone* (`http://acs.amazonaws.com/groups/global/AllUsers`).

# Basic (Download HTTP) Distributions

Delivery method used to serve static content.

![CloudFront Configuration](_images/CloudFront_Configuration.png)

# Website Configuration Endpoint Distributions

Enable a [website endpoint](../Protocols/S3/index#website-configuration) with no CDN features.

# Website Configuration Endpoint Distributions with CloudFront CDN

Custom origin CDN distribution with a [website endpoint](../Protocols/S3/index#website-configuration) as a source to make use of the website endpoint features in CloudFront.

You must also enable the website endpoint to make sure the CloudFront edge locations can fetch the content from the origin.

## Reference

- [Using CloudFront with the new Amazon S3 static website hosting features](https://forums.aws.amazon.com/ann.jspa?annID=921)

# Streaming (RTMP) Distributions

```{attention}
Discontinued on December 31, 2020 within CloudFront 

For further information refer to the [AWS announcement](https://forums.aws.amazon.com/ann.jspa?annID=7356).
```

A delivery method used to serve [media](http://en.wikipedia.org/wiki/Flash_Video) using a [streaming protocol](http://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol).

## Playback Configuration

Copy the `RTMP` URL for a given file in a bucket with a streaming distribution enabled is displayed in the Info window *Distribution (CDN)* tab with *Streaming (RTMP)* selected as the delivery method. Where to put the URL depends on the client player you are using.

# Custom Origin (HHTP/HTTPS) Distributions

A [custom origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access) is an origin server that isn't hosted on Amazon S3. The origin server holds the original, definitive versions of your content. You can connect to any [FTP](../Protocols/FTP), [SFTP](../Protocols/SFTP) or [WebDAV](../Protocols/WebDAV/index) server and configure it as an origin server for content distribution with Amazon CloudFront in the *Distribution (CDN)* tab of the [Info](../Cyberduck/Info) panel. The hostname from the *Web URL* configured in the bookmark is used to configure the origin of the CDN.

![Custom Origin CDN](_images/Custom_Origin_CDN.png)

- Adjust the [Web URL](../Cyberduck/Bookmarks#http-url) of the bookmark to the host where you want to CloudFront look for the original content. If the scheme of the Web URL is `http` the origin HTTP port of the distribution is set to the port number in the Web URL (defaults to `80`) and the HTTPS port is set to `443`. If the scheme is `https` the origin HTTPS port of the distribution is set to the port number in the Web URL (defaults to `443`) and the HTTP port is set to `80`.
- Set the *Path* of the bookmark to the document root of your web server. This allows you to select files for [invalidation](#object-invalidation) or set the [default root object](#index-file).
- Connect to the server and select the *Distribution (CDN)* panel from the [Info](../Cyberduck/Info) window.
- Check the *Origin URL* displayed and enable the distribution with *Enable Amazon CloudFront distribution*.
- Refresh the status of the distribution using *`⌘R`*. The initial status is *In Progress* and should subsequently change to *Deployed* when the changes in Amazon CloudFront have propagated.
- Click the *Where* URL to load the content over the CDN.

**Example Configuration:**</br>
The first time your content is served to a worldwide user (one in Tokyo, for example), a copy of the content is fetched from the origin server and stored in cache on the edge servers in that location. The next time the content is requested, it's pulled directly from the cached copy on the edge servers, dramatically reducing delivery time.

![CDN Custom Origin Server](_images/CDN_Custom_Origin_Server.png)

| | | |
|---|---|---|
| Server | media.cyberduck.ch |	Hostname configured in bookmark to connect to. If this is different than what hostname CloudFront should fetch the origin content from, edit the hostname in the Web URL of the bookmark. |
| CNAME | cdn.cyberduck.ch | Alias for hostname assigned by the CloudFront distribution |
| Bookmark Path | `/usr/home/dkocher/cyberduck.ch/` | The Web Server Document Root |
| Selected File | `/home/dkocher/cyberduck.ch/img/cyberduck.icon.png` | A file selected in the browser |
| HTTP URL | http://media.cyberduck.ch/img/cyberduck.icon.png | Origin URL for the resource |
| CDN URL | http://d15bfu8of7vup8.cloudfront.net/img/cyberduck.icon.png | URL for the resource assigned by the CloudFront distribution |
| CDN CNAME URL | http://cdn.cyberduck.ch/img/cyberduck.icon.png | URL for resource in CDN with custom hostname registered in the DNS |

# Deployment Status

Upon changing configuration parameters of a distribution configuration, the settings are not distributed immediately in the CDN. While the deployment is in progress (which can take up to 15 minutes), the status *In Progress* is displayed. The updates are fully propagated throughout the CloudFront system when the distribution's state switches from *In Progress* to *Deployed*.

## CloudFront Access Logging

When this option is enabled, access logs are written to `<bucketname>/logs`. The changes to the logging configuration take effect within 12 hours. The logging option is supported for both download and streaming distributions. Choose the target bucket for access logs in the dropdown menu listing all buckets of your account. It is considered best practice to choose a different logging target for each distribution.

# Origin

The source of the content where CloudFront fetches the content to be served in the edge location of the CDN. This is a [S3](../Protocols/S3/index) bucket or your custom origin.

# Where

The `cloudfront.net` domain assigned to your distribution. This is directing to the edge location in the CDN next to the user requesting an URL.

# CNAMEs

Enter a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) (alias in the Domain Name System) for the hostname of the distribution given by CloudFront. To use multiple CNAMEs for a single distribution, the hostnames must be space delimited. The CNAME must be registered on the nameserver responsible for your domain and point to `cloudfront.net` domain assigned to your distribution.

Example configuration:

	;; QUESTION SECTION:
	;cdn.cyberduck.ch.		IN	A
	
	;; ANSWER SECTION:
	cdn.cyberduck.ch.	1576	IN	CNAME	d15bfu8of7vup8.cloudfront.net.

# Index File

You can assign a default root object to your HTTP or HTTPS distribution. This default object will be served when Amazon CloudFront receives a request for the root of your distribution – i.e., your distribution’s domain name by itself.

When you define a default root object, a user request that calls the root of your distribution returns the default root object. For example, if you designate the file `index.html` as your default root object, a request for `http://d604721fxaaqy9.cloudfront.net/` returns `http://d604721fxaaqy9.cloudfront.net/index.html`.

# Object Invalidation

[Invalidation](http://aws.amazon.com/about-aws/whats-new/2010/08/31/cloudfront-adds-invalidation-feature/) is one way to remove a distribution object from an edge server cache before the expiration setting on the object's header. Invalidation clears the object from the edge server cache, and a subsequent request for the object will cause CloudFront to return to the origin to fetch the latest version of the object.

Use the Invalidate option *File → Info → Distribution (CDN)* to invalidate files from edge locations.

# Copy URLs

CloudFront URLs are available in the regular *Copy URL* menu. Refer to [Open or Copy HTTP URL](../Cyberduck/Browser#open-or-copy-http-url).


# References

- [Amazon CloudFront FAQs](http://aws.amazon.com/cloudfront/faqs/)
- [Video on Demand and Live Streaming Video with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html)
- [Edge Locations](http://aws.amazon.com/cloudfront/#details)