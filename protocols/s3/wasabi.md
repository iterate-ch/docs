Wasabi Storage
====

```{image} https://cdn.cyberduck.io/img/providers/wasabi.png
:alt: Wasabi Storage
:width: 128px
```

> One simple storage solution that is faster than Amazon S3 yet cheaper than Amazon Glacier. Wasabi's immutable buckets protect you against the most common causes of data loss.

[Wasabi](https://wasabi.com/) is a S3 compatible object storage.

## Connecting

```{Note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

- **Wasabi CA Central 1 (Toronto)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(ca-central-1%20).cyberduckprofile>` the *Wasabi Storage (ca-central-1) Connection Profile* for preconfigured settings.
- **Wasabi US East 1 (N. Virginia)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(us-east-1).cyberduckprofile>` the *Wasabi Storage (us-east-1) Connection Profile* for preconfigured settings.
- **Wasabi US East 2 (N. Virginia)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(us-east-2).cyberduckprofile>` the *Wasabi Storage (us-east-2) Connection Profile* for preconfigured settings.
- **Wasabi US West 1 (Oregon)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(us-west-1).cyberduckprofile>` the *Wasabi Storage (us-west-1) Connection Profile* for preconfigured settings.
- **Wasabi US Central 1 (Texas)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(us-central-1).cyberduckprofile>` the *Wasabi Storage (us-central-1) Connection Profile* for preconfigured settings.
- **Wasabi EU Central 1 (Amsterdam)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(eu-central-1).cyberduckprofile>` the *Wasabi Storage (eu-central-1) Connection Profile* for preconfigured settings.
- **Wasabi EU Central 2 (Frankfurt)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(eu-central-2).cyberduckprofile>` the *Wasabi Storage (eu-central-2) Connection Profile* for preconfigured settings.
- **Wasabi EU West 1 (London)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(eu-west-1).cyberduckprofile>` the *Wasabi Storage (eu-west-1) Connection Profile* for preconfigured settings.
- **Wasabi EU West 2 (Paris)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(eu-west-2).cyberduckprofile>` the *Wasabi Storage (eu-west-2) Connection Profile* for preconfigured settings.
- **Wasabi AP Northeast 1 (Tokyo)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(ap-northeast-1).cyberduckprofile>` the *Wasabi Storage (ap-northeast-1) Connection Profile* for preconfigured settings.
- **Wasabi AP Northeast 2 (Osaka)** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Wasabi%20(ap-northeast-2).cyberduckprofile>` the *Wasabi Storage (ap-northeast-2) Connection Profile* for preconfigured settings.

## Known Issues

### 301 Moved Permanently but no location header

You are connected with a connection profile specific to a region not matching the bucket region. Please install the additional connection profile for the specific region of the bucket.

### Certificate Error

Connecting to buckets with dots in the bucket name can cause a certificate error. 

```{image} _images/Wasabi_Certificate_Error.png
:alt: Certificate Error
:width: 400px
```

## References

- [How do I use Cyberduck or Mountain Duck with Wasabi?](https://wasabi-support.zendesk.com/hc/en-us/articles/115001671012-How-do-I-use-Cyberduck-or-Mountain-Duck-with-Wasabi-)