Cloudflare R2
====

> [Cloudflare R2 Storage](https://www.cloudflare.com/products/r2/) allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.

## Connection

{download}`Download<https://profiles.cyberduck.io/Cloudflare%20R2%20Storage%20(S3).cyberduckprofile>` the *Cloudflare R2 Storage (S3) Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

:::{tip}
Make sure to set `<ACCOUNT_ID>.r2.cloudflarestorage.com` for server. The `ACCOUNT_ID` can be found in the [Cloudflare dashboard](https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/).
:::

:::{warning}
For tokens that are limited to _Object Read & Write_ or _Object Read only_ with no permission to list buckets, the bucket name to
connect to must be set in `Path` when configuring the [bookmark](../../cyberduck/bookmarks.md#edit-bookmark).
:::

### Regions
The connection profile supports the following [regions](https://developers.cloudflare.com/r2/reference/data-location/#available-hints):

- `APAC` (Asia Pacific)
- `EEUR` (Eastern Europe)
- `ENAM` (Eastern North America)
- `WEUR` (Western Europe)
- `WNAM` (Western North America)

## Limitations

The following features are not supported within the [open beta](https://blog.cloudflare.com/r2-open-beta/):
- Specify regions for buckets
- ACLs
- Pre-signed URLs 

## References

- [Cloudflare documentation](https://developers.cloudflare.com/r2/get-started/)