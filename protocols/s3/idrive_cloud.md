IDrive® Cloud
===

> [IDrive® Cloud](https://www.idrive.com/cloud/) is an S3 compatible cloud object storage solution. We provide a scalable, low-cost infrastructure for unlimited data storage. A platform-as-a-service, IDrive® Cloud can be used for various purposes like securely archiving data, hosting a web or mobile applications, or even as robust storage for data analytics.

# Connecting

## Connection Profile

Double-click on the downloaded file to activate the connection profile.

### S3

Create S3 Access Keys from the IDrive® Cloud Console.

- {download}`Download<https://s3.us-west-1.idrivecloud.io/v1/d6fb089f27314160b3464ed223e0b283/cyberduck-profiles/IDrive%20Cloud%20S3(us-west-1).cyberduckprofile>` the *IDrive® Cloud S3 Oregon region profile* for preconfigured settings for authentication.
- {download}`Download<https://s3.us-west-1.idrivecloud.io/v1/d6fb089f27314160b3464ed223e0b283/cyberduck-profiles/IDrive%20Cloud%20S3(us-east-1).cyberduckprofile>` the *IDrive® Cloud S3 Virginia region profile* for preconfigured settings for authentication.

**How to create a S3 Access Key**</br>
Keys can be generated in the *Settings* section of the *Profile Details* within the *IDrive® Cloud Console*:

- Click on your username and select *Settings*
- Navigate to the Profile tab and click on *Create New Access Key*. The generated *S3 Access Key* will be displayed in the *User Keys List*.

```{note}
You can have a maximum of 2 pairs of S3 Access Key and Secret.
```

### OpenStack Swift

- {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Openstack%20Swift%20(Keystone%203).cyberduckprofile>` the *OpenStack Swift (Keystone 3) profile* or install it through the *Profiles* tab of the preferences for preconfigured settings for authentication.

Enter the following authentication credentials to the bookmark:

- Server: `identity.api.idrivecloud.io`
- Project:Domain:Username: `Your project, domain, and username separated by :`
- Password: `API Password`

**How to get the API Password**</br>
The API Password can be obtained from *Swift API Password* section of *IDrive® Cloud console*.

# References

- [IDrive® Cloud documentation](https://www.idrive.com/cloud/guides/default)