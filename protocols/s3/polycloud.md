Polycloud
====

> [Polycloud](https://crowdstorage.com/) is an object storage service offering secure and private data storage with immediate access and high reliability. Data are stored as objects within buckets and can be accessed and managed via our basic browser-based user interface, but full functionality is realized by utilizing our S3 compatible API.

## Connecting

{download}`Download<https://drive.google.com/file/d/1a-yZPNHGvm6PvR3JEvdiYzs8OHnf_g6T/view?usp=sharing>` the *Polycloud Connection Profile* for preconfigurated settings for authentication.

Double-click on the downloaded file to activate the connection profile. Enter the following authentication credentials to the bookmark:
- Server: `polycloud.crowdapis.com`
- Access Key ID: Access Key Credentials
- Secret Access Key: Access Key Credentials

### How to Create Application Keys

1. [Sign in](https://polycloud.crowdstorage.com/login) to your Polycloud account
2. Select *Generate Access Key* on the *My Buckets* page.
3. Select *Generate* to confirm that you want to generate an access key.
4. A window will show up containing the key information (Access Key ID, Secret Access Key)

```{note}
The key information will only be shown once and can't be recovered. If you do lose them you can generate new keys, but you will then need to update all of your 3rd party applications with the new credentials.
```

## References

- [CrowdStorage Documentation](https://crowdstorage.com/documentation/connect-cyberduck-server/)