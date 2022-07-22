DreamObject Cloud Storage
====

```{image} https://cdn.cyberduck.io/img/providers/dreamobjects.png
:alt: DreamObject Cloud Storage
:width: 128px
```

> [DreamObjects](http://dreamhost.com/cloud/dreamobjects/) is a cost-effective, public cloud storage service built on top of the open source technology [Ceph](http://ceph.io/). It is compatible with the APIs of [Amazon S3](index.md) and [Swift](../openstack/index.md) based object storage services.

## Connecting

```{attention}
`us-west-1` was shut down

See the article [What DreamObjects hostname should I use to connect?](https://help.dreamhost.com/hc/en-us/articles/360001370846) for more information.
```

- `us-east-1` {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/DreamObjects%20(us-east-1).cyberduckprofile>` the *DreamObjects Cloud Storage Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings. 
- Alternatively, use `objects-us-east-1.dream.io` for the hostname in Open Connection or Bookmark settings with a *S3* protocol selection. Then user your *Access Key* for the username and *Secret Key* for the password.

## Limitations

- View a feature support list in the [API documentation](https://help.dreamhost.com/hc/en-us/articles/217590537-How-To-Use-DreamObjects-S3-compatible-API).
- No support for multipart uploads through Cyberduck.

## References

- [This article describes how to connect Cyberduck to your DreamObjects buckets](https://help.dreamhost.com/hc/en-us/articles/217131247#connecting)
- [The following describes how to use Cyberduck to connect to your DreamObjects account](https://help.dreamhost.com/hc/en-us/articles/217131247-Cyberduck)