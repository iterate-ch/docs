IDrive®
====

```{contents} Content
:depth: 2
:local:
```

## IDrive® Cloud

> [IDrive® Cloud](https://www.idrive.com/cloud/) is an S3 compatible cloud object storage solution. We provide a scalable, low-cost infrastructure for unlimited data storage. A platform-as-a-service, IDrive® Cloud can be used for various purposes like securely archiving data, hosting a web or mobile applications, or even as robust storage for data analytics.

### Connecting

Double-click on the downloaded file to activate the connection profile.

#### S3

Create S3 Access Keys from the IDrive® Cloud Console.

- {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/IDrive%20Cloud%20S3(us-west-1).cyberduckprofile>` the *IDrive® Cloud S3 Oregon region profile* for preconfigured settings for authentication.
- {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/IDrive%20Cloud%20S3(us-east-1).cyberduckprofile>` the *IDrive® Cloud S3 Virginia region profile* for preconfigured settings for authentication.

**How to create a S3 Access Key**</br>
Keys can be generated in the *Settings* section of the *Profile Details* within the *IDrive® Cloud Console*:

- Click on your username and select *Settings*
- Navigate to the Profile tab and click on *Create New Access Key*. The generated *S3 Access Key* will be displayed in the *User Keys List*.

```{note}
You can have a maximum of 2 pairs of S3 Access Key and Secret.
```

#### OpenStack Swift

- {download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/Openstack%20Swift%20(Keystone%203).cyberduckprofile>` the *OpenStack Swift (Keystone 3) profile* or install it from *Preferences… → Profiles* for preconfigured settings for authentication.

Enter the following authentication credentials to the bookmark:

- Server: `identity.api.idrivecloud.io`
- Project:Domain:Username: `Your project, domain, and username separated by :`
- Password: `API Password`

**How to get the API Password**</br>
The API Password can be obtained from *Swift API Password* section of *IDrive® Cloud console*.

### References

- [IDrive® Cloud documentation](https://www.idrive.com/cloud/guides/default)


## IDrive® e2

> [IDrive® e2](https://www.idrive.com/e2/) is a fast, reliable and affordable object storage solution with S3 API compatibility. It is an ideal solution if you need a second copy in the cloud, off-site disaster recovery, an active and accessible data archive, or long term storage.

### Connection

#### Connection Profile

{download}`Download<http://profiles.cyberduck.io.s3.amazonaws.com/IDrive%20e2.cyberduckprofile>` the *IDrive® e2 Connection Profile* or install it from *Preferences… → Profiles* for preconfigured settings.

#### Manual Configuration

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md). 

- Protocol: `Amazon S3`
- Server: `<your endpoint>`
- Access Key ID: `<your access key>`
- Secret Access Key: `<your secret access key>`

##### Create S3 Access Keys

You have to create access keys to use a third party tool:

1. [Sign in](https://app.idrivee2.com/signin) to your IDrive e2 account via web browser.
2. Navigate to the *Access Key* tab and select *Create Access Key*.
3. Enter name and specifications: regions, permissions, buckets.
4. Select *Create Access Key*. The access key will be generated and the details of the key will be displayed in a popup window.

```{note}
The prompt contailing the access key information will only be displayed once. Make sure to save the details for future use.
```

### Limitations

IDrive® e2 provides a unique domain name for each user region provided within the access key details. If you're missing your domain name, you'll have to generate a new access key. *Note:* Only the Admin can create and manage access keys.

### Ressources

- [IDrive® e2 documentation](https://www.idrive.com/e2/developer-guide)