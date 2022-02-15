Alibaba Cloud Object Storage Service (OSS)
====

```{image} https://cdn.cyberduck.io/img/providers/alibaba.png
:alt: Alibaba Cloud Object Storage Service
:width: 128px
```

> [Alibaba Cloud Object Storage Service (OSS)](https://www.alibabacloud.com/help/doc-detail/31817.htm) is a storage service that enables you to store, back up, and archive any amount of data in the cloud. OSS is a cost-effective, highly secure, and highly reliable cloud storage solution. It uses RESTful APIs and provides 99.9999999999% (12 nines) durability (designed for) and 99.995% availability or service continuity (designed for).

## Connecting

```{Note}
All connection profiles are available through the *Preferences → Profiles* tab.
```

### Connection Profile

- **Alibaba Beijing** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Beijing).cyberduckprofile>` the *Alibaba (Beijing) Connection Profile* for preconfigured settings.
- **Alibaba Chengdu** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Chengdu).cyberduckprofile>` the *Alibaba (Chengdu) Connection Profile* for preconfigured settings.
- **Alibaba Dubai** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Dubai).cyberduckprofile>` the *Alibaba (Dubai) Connection Profile* for preconfigured settings.
- **Alibaba Frankfurt** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Frankfurt).cyberduckprofile>` the *Alibaba (Frankfurt) Connection Profile* for preconfigured settings.
- **Alibaba Guangzhou** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Guangzhou).cyberduckprofile>` the *Alibaba (Guangzhou) Connection Profile* for preconfigured settings.
- **Alibaba Hangzhou** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Hangzhou).cyberduckprofile>` the *Alibaba (Hangzhou) Connection Profile* for preconfigured settings.
- **Alibaba Heyuan** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Heyuan).cyberduckprofile>` the *Alibaba (Heyuan) Connection Profile* for preconfigured settings.
- **Alibaba Hohhot** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Hohhot).cyberduckprofile>` the *Alibaba (Hohhot) Connection Profile* for preconfigured settings.
- **Alibaba Hong Kong** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Hong%20Kong).cyberduckprofile>` the *Alibaba (Hong Kong) Connection Profile* for preconfigured settings.
- **Alibaba Jakarta** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Jakarta).cyberduckprofile>` the *Alibaba (Jakarta) Connection Profile* for preconfigured settings.
- **Alibaba Kuala Lumpur** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Kuala%20Lumpur).cyberduckprofile>` the *Alibaba (Kuala Lumpur) Connection Profile* for preconfigured settings.
- **Alibaba London** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(London).cyberduckprofile>` the *Alibaba (London) Connection Profile* for preconfigured settings.
- **Alibaba Manila** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Manila).cyberduckprofile>` the *Alibaba (Manila) Connection Profile* for preconfigured settings.
- **Alibaba Mumbai** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Mumbai).cyberduckprofile>` the *Alibaba (Mumbai) Connection Profile* for preconfigured settings.
- **Alibaba Qingdao** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Qingdao).cyberduckprofile>` the *Alibaba (Qingdao) Connection Profile* for preconfigured settings.
- **Alibaba Shanghai** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Shanghai).cyberduckprofile>` the *Alibaba (Shanghai) Connection Profile* for preconfigured settings.
- **Alibaba Shenzhen** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Shenzhen).cyberduckprofile>` the *Alibaba (Shenzhen) Connection Profile* for preconfigured settings.
- **Alibaba Singapore** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Singapore).cyberduckprofile>` the *Alibaba (Singapore) Connection Profile* for preconfigured settings.
- **Alibaba Sydney** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Sydney).cyberduckprofile>` the *Alibaba (Sydney) Connection Profile* for preconfigured settings.
- **Alibaba Tokyo** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Tokyo).cyberduckprofile>` the *Alibaba (Tokyo) Connection Profile* for preconfigured settings.
- **Alibaba Ulanqab** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Ulanqab).cyberduckprofile>` the *Alibaba (Ulanqab) Connection Profile* for preconfigured settings.
- **Alibaba Virginia** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Virginia).cyberduckprofile>` the *Alibaba (Virginia) Connection Profile* for preconfigured settings.
- **Alibaba Zhangjiakou** {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Alibaba%20(Zhangjiakou).cyberduckprofile>` the *Alibaba (Zhangjiakou) Connection Profile* for preconfigured settings.

### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md). Lookup the *Internet endpoint* for the buckets you want to access. Refer to [Regions and endpoints](https://www.alibabacloud.com/help/doc-detail/31837.htm).

- Protocol: `S3 (Amazon Simple Storage Service)`
- Server: `oss-eu-west-1.aliyuncs.com`, `oss-eu-central-1.aliyuncs.com`, `oss-me-east-1.aliyuncs.com`, `oss-us-east-1.aliyuncs.com`, `oss-us-west-1.aliyuncs.com`, `oss-cn-shenzhen.aliyuncs.com`, …
- Username and Password: Access credentials in your [user center console](https://usercenter.console.aliyun.com/).

## Known Issues

The error `The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.` indicates that you try to access a bucket in a different region than the endpoint you are connecting to.

## References

- [Regions and endpoints](https://www.alibabacloud.com/help/doc-detail/31837.htm)