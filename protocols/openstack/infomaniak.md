Infomaniak
====

![Infomaniak Drive Icon](_images/blue-128.png)

:::{contents} Content
:depth: 2
:local:
:::

## Infomaniak Public Cloud

> [High Performance Cloud Infrastructure. In Switzerland, at the right price.](https://www.infomaniak.com/en/hosting/public-cloud)

### Connecting (Swift)

:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

#### Swift Connection Profiles

Log in to your *Infomaniak OpenStack Swift space* via this preconfigured connection profile:

- {download}`Infomaniak Public Cloud 01 (Swift)<https://profiles.cyberduck.io/Infomaniak%20Public%20Cloud%2001%20(Swift).cyberduckprofile>`
- {download}`Infomaniak Public Cloud 02 (Swift)<https://profiles.cyberduck.io/Infomaniak%20Public%20Cloud%2002%20(Swift).cyberduckprofile>`

#### Additional Fields Required

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- **Project:Domain:Username**: Information available in your Infomaniak manager. Example: `PCP-XXXXXX:Default:PCU-XXXXXX`
- **Password**: password is the same as the one you use for the OpenStack dashboard

---

### Connecting (S3)

Infomaniak Public Cloud also supports the S3 protocol, fully compatible with AWS Signature Version 4. This is distinct from Swiss Backup and requires EC2-style credentials generated from the OpenStack API.

:::{important}
Do **not** use Swiss Backup credentials with the S3 protocol. Only credentials from **Public Cloud** via the OpenStack API (EC2-style) are supported.
:::

#### S3 Connection Profiles

- {download}`Infomaniak Public Cloud 01 (S3)<https://profiles.cyberduck.io/Infomaniak%20Public%20Cloud%2001%20(S3).cyberduckprofile>` — Region: `dc3-a`
- {download}`Infomaniak Public Cloud 02 (S3)<https://profiles.cyberduck.io/Infomaniak%20Public%20Cloud%2002%20(S3).cyberduckprofile>` — Region: `dc4-a`

These profiles are configured with:

- Correct hostname (`s3.pub1.infomaniak.cloud` or `s3.pub2.infomaniak.cloud`)
- Region explicitly set (required for AWS Signature V4)
- Path-style access enabled (`s3.bucket.virtualhost.disable=true`)

#### How to Generate Credentials (OpenStack CLI)

To use the S3 protocol, generate EC2-compatible credentials using the OpenStack CLI.

##### Prerequisites

Install the OpenStack CLI and set environment variables:

```bash
export OS_AUTH_URL=https://keystone.pub1.infomaniak.cloud
export OS_USERNAME=PCU-XXXXXXX
export OS_PROJECT_ID=PCP-XXXXXXX
export OS_PASSWORD=your_password
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
```

You can retrieve these from the [OpenStack Horizon dashboard](https://cloud.infomaniak.com) under “API Access”.

##### Create EC2 Credentials

Run:

```bash
openstack ec2 credentials create
```

This returns:

```
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| access      | 5a6c43a89e914eb3b388df9817dcdef2 |
| secret      | xL5Hv2Bp8MqHkKrMBXr7PvVHZoUZaeYF |
| project_id  | f091b24c7413428a98b7a4455dc12345 |
| user_id     | 3c362f13e0f144eb8a78fcd6a8aaabcd |
+-------------+----------------------------------+
```

In Cyberduck:

- **Access Key ID** → value of `access`
- **Secret Access Key** → value of `secret`

---

### Troubleshooting

If you encounter this error:

```
SignatureDoesNotMatch
The request signature we calculated does not match the signature you provided.
```

Verify:

- The `Region` field in your profile is set to `dc3-a` or `dc4-a` (not `us-east-1`)
- You are using EC2 credentials from the Public Cloud API (not Swiss Backup)
- Path-style access is enabled

---

### References

- [Official Infomaniak Public Cloud documentation](https://docs.infomaniak.cloud/)
- [OpenStack EC2 Credentials Documentation](https://docs.openstack.org/keystone/latest/user/ec2_credentials.html)
- [Cyberduck S3 Protocol Help](https://trac.cyberduck.io/wiki/help/en/howto/s3)

## Infomaniak Swiss Backup

Swiss Backup is a solution that automatically backs up your files, workstations, mobiles, and servers. Your data is stored in Switzerland in Tier 3+ datacenters in at least three different physical locations. Infomaniak is a leading Swiss hosting service provider that is recognized for the reliability of its services and the quality of its 7/7 support in over five languages.

> [Swiss Backup enables you to back up and recover your workstations, servers, virtual machines, NAS and much more besides in total peace of mind.](https://www.infomaniak.com/en/swiss-backup)

### Connecting

:::info
Swiss Backup also supports both the **Swift** and **S3** protocols.

The type of protocol (Swift or S3) must be selected when you create a new backup space in the Infomaniak Manager.

- If you select **S3**, credentials will be generated automatically during setup.
- These credentials are distinct from those used with Infomaniak Public Cloud.
- S3 credentials for Swiss Backup cannot be created via the OpenStack CLI.

You will receive:

- An **Access Key ID** and a **Secret Access Key**
- A specific **S3 endpoint URL** (different from Public Cloud)

:::


:::{note}
Connection profiles can be installed from *Preferences → Profiles*.
:::

#### Connection Profiles

Log in to your *Infomaniak OpenStack Swift space* via this preconfigured connection profile:

- {download}`Infomaniak Swiss Backup (01) connection profile<https://profiles.cyberduck.io/Infomaniak%20Swiss%20Backup%2001%20(Swift).cyberduckprofile>`
- {download}`Infomaniak Swiss Backup (02) connection profile<https://profiles.cyberduck.io/Infomaniak%20Swiss%20Backup%2002%20(Swift).cyberduckprofile>`
- {download}`Infomaniak Swiss Backup (03) connection profile<https://profiles.cyberduck.io/Infomaniak%20Swiss%20Backup%2003%20(Swift).cyberduckprofile>`
- {download}`Infomaniak Swiss Backup (04) connection profile<https://profiles.cyberduck.io/Infomaniak%20Swiss%20Backup%2004%20(Swift).cyberduckprofile>`

#### Additional Fields Required

Enter the following information in the [bookmark](../../cyberduck/bookmarks.md):

- **Project:Domain:Username**: information sent by email when you created your Swiss Backup space
- **Password**: password sent by email when you created your Swiss Backup space

### References

- [Official Infomaniak documentation](https://www.infomaniak.com/en/support/faq/2284/startup-guide-swiss-backup)
- [Cyberduck connection profile documentation](https://www.infomaniak.com/en/support/faq/2282/swiss-backup-backing-up-files-with-cyberduck)
- [Find out more about Swiss Backup](https://www.infomaniak.com/en/swiss-backup)
- [Test Swiss Backup free](https://www.infomaniak.com/en/swiss-backup)

## Infomaniak kDrive

Refer to [kDrive](../webdav/kdrive.md).
