Configure a user in AWS IAM that is required to use MFA to connect to a bucket in S3 with a policy requiring MFA
====

> You want an IAM user with permissions to access S3 to require input from a MFA device when opening a specific bucket.
> Create a configuration for AWS CLI that is supported in Cyberduck and Mountain Duck using
> the [S3 (Credentials from AWS Command Line Interface) connection profile](../protocols/s3/index.md#connecting-using-credentials-from-aws-command-line-interface)
> or use
> the [AWS S3 (MFA Session Token) connection profile](../protocols/s3/index.md#connecting-using-assumerole-from-aws-security-token-service-sts)
> with no additional configuration.


:::{important}

* Cyberduck [8.3.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.2.0](https://mountainduck.io/changelog/) or later required
  :::

## Create a bookmark in Cyberduck or Mountain Duck

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *AWS S3 (MFA Session Token)* connection profile.
3. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose *AWS S3 (MFA Session Token)*
   connection profile in the protocol dropdown.

## Create IAM user with access keys and MFA enabled

1. In AWS [IAM console](https://console.aws.amazon.com/iam/) create a new user.
2. In _Security Credentials_, choose _Assign MFA device_
3. In _Security Credentials_, choose _Create access key_

Ensure the attached policy for the user has S3 access IAM [
`GetSessionToken`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html) permissions.

## Add bucket policy to deny access to bucket with no MFA

1. In AWS [S3 console](https://console.aws.amazon.com/s3/) for a new or existing bucket, choose _Permissions_ and then
   _Bucket Policy_.
2. Edit the bucket policy to require MFA for access.

    ```{code-block} json
    {
    "Version": "2012-10-17",
    "Id": "RequireMFAForS3Access",
    "Statement": [
        {
            "Sid": "DenyAllAccessWithoutMFA",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::<BUCKET_NAME>",
                "arn:aws:s3:::<BUCKET_NAME>/*"
            ],
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "false"
                }
            }
        }
    ]
    }
    ```

## Connect to S3 using the bookmark

Using the AWS Security Token Service (STS) `GetSessionToken` API, temporary credentials are generated for the user from
static access keys and a MFA device.

1. When not already configured in the bookmark, enter the static _Access Key ID_ and _Secret Access Key_ configured for
   the user.

2. Enter the MFA device identification when prompted.

   :::{image} _images/S3_MFA_Device_Prompt.png
   :alt: MFA Device Prompt
   :width: 400px
   :::

   :::{tip}
   Enter the identification number of the MFA device that is associated with the user. The value is either the serial
   number for a hardware device
   (such as `<code>GAHT12345678</code>`) or an Amazon Resource Name (ARN) for a virtual device (such as
   `<code>arn:aws:iam::123456789012:mfa/device</code>`)
   :::

3. Enter the one-time MFA code from your device when prompted.

   :::{image} _images/S3_MFA_Code_Prompt.png
   :alt: MFA Code Prompt
   :width: 400px
   :::

## References

- [How do I require users from other AWS accounts to use MFA to access my Amazon S3 buckets?](https://repost.aws/knowledge-center/enforce-mfa-other-account-access-bucket)
- [Requiring MFA](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-MFA)