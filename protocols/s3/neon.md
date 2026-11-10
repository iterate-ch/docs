Neon Object Storage
====

> [Neon Object Storage](https://neon.com/docs/storage/overview) is S3 compatible object storage included with Neon projects. Each branch has its own storage endpoint.

## Connecting

### Connection Profile

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

{download}`Download<https://profiles.cyberduck.io/Neon%20Object%20Storage.cyberduckprofile>` the *Neon Object Storage Connection Profile* for preconfigured settings.

:::{tip}
Set *Server* to the storage endpoint of your branch, like `br-<branch>.storage.c-<n>.<region>.aws.neon.tech`. In the [Neon Console](https://console.neon.tech/), click *Connect* and open the *Storage* tab to copy the endpoint.
:::

### Access Keys

Credentials are scoped to a branch and its child branches.

1. Log in to the [Neon Console](https://console.neon.tech/) and select your project.
2. Click *Connect* and open the *Storage* tab.
3. Click *Reveal credential* or *Copy credentials*. You can also create a credential with `storage:read` and `storage:write` scopes in *Settings → Credentials*.
4. Enter the token ID (`nak_live_…`) for *Access Key ID* and the secret (`nsk_live_…`) for *Secret Access Key*.

## Limitations

- ACLs are read only. Renaming a file fails after the copy because the ACL of the source file cannot be applied to the target.
- Versioning and lifecycle configurations are not enforced.
- Bucket logging, website configuration and transfer acceleration are not supported.

## References

- [Neon Object Storage documentation](https://neon.com/docs/storage/overview)
- [S3 compatibility](https://neon.com/docs/storage/s3-compatibility)
