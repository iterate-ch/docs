BigCommerce
====

## Connecting

### Manual Configuration
1. Obtain your WebDAV credentials and setup details from your BigCommerce control panel ([Server Settings → File Access (WebDAV)](http://login.bigcommerce.com/deep-links/settings/file-access)).
2. Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):
	- **Protocol**: `WebDAV (HTTPS)`
	- **Server**: The domain name of your WebDAV Path with the protocol scheme `https://` and path `/dav` removed.
	- **Username**: Your WebDAV username
	- **Password**: Your WebDAV password
	- **Path**: `dav`

### Connection Profile
Go to [Settings → File access (WebDAV)](http://login.bigcommerce.com/deep-links/settings/file-access) and click _Download_ next to _Cyberduck Connection Profile_ file. Open the [connection profile](../../protocols/profiles/index.md) with Cyberduck to create a bookmark with pre-configured settings.

## Interoperability

:::{warning}
Ensure that that filenames contain no whitespace.
:::

## References

- [File Access (WebDAV)](https://support.bigcommerce.com/s/article/File-Access-WebDAV)
- [Connecting to WebDAV with Cyberduck](https://support.bigcommerce.com/s/article/File-Access-WebDAV#cyberduck)
- [Uploading and Linking to a File in Your Store](https://support.bigcommerce.com/s/article/How-do-I-add-and-link-to-a-file-in-my-store?language=en_US)