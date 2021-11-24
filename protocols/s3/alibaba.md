Alibaba Cloud Object Storage Service (OSS)
===

> [Alibaba Cloud Object Storage Service (OSS)](https://www.alibabacloud.com/help/doc-detail/31817.htm) is a storage service that enables you to store, back up, and archive any amount of data in the cloud. OSS is a cost-effective, highly secure, and highly reliable cloud storage solution. It uses RESTful APIs and provides 99.9999999999% (12 nines) durability (designed for) and 99.995% availability or service continuity (designed for).

# Connecting

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md). Lookup the *Internet endpoint* for the buckets you want to access. Refer to [Regions and endpoints](https://www.alibabacloud.com/help/doc-detail/31837.htm).

- Protocol: `S3 (Amazon Simple Storage Service)`
- Server: `oss-eu-west-1.aliyuncs.com`, `oss-eu-central-1.aliyuncs.com`, `oss-me-east-1.aliyuncs.com`, `oss-us-east-1.aliyuncs.com`, `oss-us-west-1.aliyuncs.com`, `oss-cn-shenzhen.aliyuncs.com`, …
- Username and Password: Access credentials in your [user center console](https://usercenter.console.aliyun.com/).

# Known Issues

The error `The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.` indicates that you try to access a bucket in a different region than the endpoint you are connecting to.

# References

- [Regions and endpoints](https://www.alibabacloud.com/help/doc-detail/31837.htm)