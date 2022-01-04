Zero byte file truncate issue with Nextcloud and ownCloud deployed with FastCGI
====

# Summary

Using a client to upload files with [HTTP chunked transfer encoding](https://en.wikipedia.org/wiki/Chunked_transfer_encoding) to a server **with fastcgi/php-fmp enabled can lead to zero byte files**. Chunked transfer encoding is used when the content length is unknown at the time the transfer is started and no `Content-length` header can be set.

# Background

There are basically two options to encode a `PUT` request. You either know the length of the data you want to transfer at the time of starting the request then you can set the HTTP `Content-Length` header appropriately or you don't know the length and thus have to choose a streaming approach using the chunked transfer encoding which does not need a `Content-Length` header at all. A client is free to choose either of the two request types as both are completely fine with the [HTTP specification](https://tools.ietf.org/html/rfc2616).

Most clients out there, including web browsers, use the former method and thus do not hit this issue. There are use cases though which make it necessary to transfer data chunked. For example [Mountain Duck](https://mountainduck.io/) that implements a virtual file system for accessing your cloud storage online. The write callbacks we get from the OS just include an offset, a buffer length and the buffer itself. Mountain Duck does not know the final size in advance. From a virtual file system perspective the call backs Mountain Duck get for an upload are as follows

	1 - CreateFile myFile.txt
	2 - SetAllocationSize myFile.txt, 1024
	3 - WriteFile myFile.txt, offset 0, length 1024, buffer
	4 - SetAllocationSize myFile.txt, 2048
	5 - WriteFile myFile.txt, offset 1024, length 1024, buffer
	6 - CloseFile myFile.txt

In step 3 [Mountain Duck](https://mountainduck.io/) opens a connection to the remote server, send a `PUT` request with the HTTP header `Transfer-Encoding: chunked` and streams through all subsequent write callbacks. Finally, in step 6, the connection is closed.

## Related bug Reports

Since the expected length is missing in the header the streaming characteristic of such requests makes them more difficult to be handled in the components being passed. From our research the issue only exists in environments that use Fast CGI to speak to their PHP application. See related bug reports

- [PHP Bug #60826 Raw POST data missing with chunked encoding, FastCGI](https://bugs.php.net/bug.php?id=60826)
- [Apache HTTPD bug 53332 - Requests with chunked encoding have no body available to FCGI backend](https://bz.apache.org/bugzilla/show_bug.cgi?id=53332).

# Recommended Configuration

## Nginx

The Nginx developers try to work around this issue by simply buffering the entire incoming stream and forward it through the FastCGI interface as a request with a well-known length. Make sure request buffering setting `fastcgi_request_buffering` is enabled (Nginx does request buffering by [default](http://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_request_buffering)). There are several [options](http://nginx.org/en/docs/http/ngx_http_fastcgi_module.html) to adjust the buffering behaviour.

Another (unverified) workaround might be to switch from socket to loopback communication for an Nginx/PHP-FPM setup. For more information refer to [github](https://github.com/nextcloud/server/issues/3628#issuecomment-749568045).

## Apache

We are aware of migrations for Apache HTTP Server such as disabling any buffering strategies in [mod_fcgid](https://httpd.apache.org/mod_fcgid) or [mod_proxy_fcgi/php-fpm](https://wiki.apache.org/httpd/PHP-FPM). Thus you should avoid using FastCGI and use `mod_php` instead which is known to handle chunked transfers correctly.

# References

- [sabre/dav - Finder](http://sabre.io/dav/clients/finder/)
- [sabre/dav - Zero Byte Files](http://sabre.io/dav/0bytes/)
- [Troubleshooting WebDAV](https://doc.owncloud.org/server/8.1/admin_manual/issues/#troubleshooting-webdav)