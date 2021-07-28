IDrive® Cloud
===

> [IDrive® Cloud](https://www.idrive.com/cloud/) is an S3 compatible cloud object storage solution. We provide a scalable, low-cost infrastructure for unlimited data storage. A platform-as-a-service, IDrive® Cloud can be used for various purposes like securely archiving data, hosting a web or mobile applications, or even as robust storage for data analytics.

# Connecting

## Connection Profile

Double-click on the downloaded file to activate the connection profile.

### S3

Create S3 Access Keys from the IDrive® Cloud Console.

- {download}`Download<https://or.object-store.api.idrivecloud.io/v1/1dfd88d37b544d778bff5a9ad469d08c/cyberduck-profiles/Openstack%20S3.cyberduckprofile>` the *IDrive® Cloud S3 Oregon region profile* for preconfigured settings for authentication.

**How to create a S3 Access Key**</br>
Keys can be generated in the *Settings* section of the *Profile Details* within the *IDrive® Cloud Console*:

- Click on your username and select *Settings*
- Navigate to the Profile tab and click on *Create New Access Key*. The generated *S3 Access Key* will be displayed in the *User Keys List*.

```{note}
You can have a maximum of 2 pairs of S3 Access Key and Secret.
```

### OpenStack Swift

- {downloadDownload the OpenStack Swift (Keystone 3) profile for preconfigured settings for authentication.

Enter the following authentication credentials to the bookmark:

- Server: `identity.api.idrivecloud.io`
- Project:Domain:Username: `Your project, domain, and username separated by :`
- Password: `API Password`

**How to get the API Password**</br>
The API Password can be obtained from *Swift API Password* section of *IDrive® Cloud console*.

# References

- [IDrive® Cloud documentation](https://www.idrive.com/cloud/guides/default)