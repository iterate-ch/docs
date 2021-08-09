KeyCDN
===

> [KeyCDN](https://www.keycdn.com/) is the leading European content delivery network. The CDN already supports HTTP/2 and consists of 24+ points of presence (POPs) around the world. KeyCDN does not charge extra for HTTPS traffic or HTTP requests. The pricing model is transparent and purely pay-as-you-go. No monthly fee.

# KeyCDN Features

KeyCDN offers a state-of-the-art features:
- Full [HTTP/2](https://www.keycdn.com/blog/keycdn-http2-support/) support for all customers
- [Free Custom SSL based on Let's Encrypt](https://www.keycdn.com/support/use-letsencrypt-with-keycdn-to-enable-ssl-tls/)
- [Raw logs](https://www.keycdn.com/support/cdn-log-format/) in real time.
- CDN changes in near-realtime: Any change or update of a KeyCDN zone is globally provisioned within minutes
- Free WordPress plugins developed by KeyCDN: [CDN Enabler](https://wordpress.org/plugins/cdn-enabler/) and [Cache Enabler](https://wordpress.org/plugins/cache-enabler/)
- File browser for push zones: Any content of y push zone can be browsed within the KeyCDN dashboard.

# Content Delivery with a KeyCDN Push Zone

## Free Trial Account Including $10

KeyCDN offers a free trial account for all Cyberduck users preloaded with \$10. The whole feature set of KeyCDN is available during the test phase. Sign up for free [KeyCDN trial account](https://www.keycdn.com/?a=7) including $10 worth 250 GB of traffic.

## Creating a KeyCDN Push Zone

A KeyCDN [push zone](https://www.keycdn.com/support/create-a-push-zone/) is needed in order to use Cyberduck and upload content to a zone.

## KeyCDN Configuration

Once a KeyCDN push zone has been created. Connect with Cyberduck to your push zone. Enter the following information in the [bookmark](../Cyberduck/Bookmarks):

- Protocol: `FTP-SSL (Explicit AUTH TLS)`
- Server: `ftp.keycdn.com`
- Port: `21`
- Username: The same username as used for the KeyCDN dashboard
- Password: Same as used for the KeyCDN dashboard

# KeyCDN Tools

KeyCDN offers a wide variety of tools along with the CDN that can be used:

- Analyze a website performance with the [KeyCDN Speed Test](https://tools.keycdn.com/speed)
- Locate IPs worldwide with [IP Location Finder](https://tools.keycdn.com/geo)
- Check if a website is ready for HTTP/2 with the [KeyCDN HTTP/2 Test](https://tools.keycdn.com/http2-test)
- Examine HTTP headers with [Curl Test](https://tools.keycdn.com/curl)