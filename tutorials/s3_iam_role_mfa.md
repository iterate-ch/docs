Configure a user in AWS IAM that is required to use MFA to connect to S3
====

> You want an IAM user who cannot directly access S3, but instead must assume a role (with MFA required) to access S3 buckets in the same AWS account. Create a configuration for AWS CLI that is supported in Cyberduck and Mountain Duck using the [S3 (Credentials from AWS Command Line Interface) connection profile](../protocols/s3/index.md#connecting-using-credentials-from-aws-command-line-interface).

:::{important}
* Cyberduck [8.3.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.2.0](https://mountainduck.io/changelog/) or later required
  :::

:::{note}
No custom configuration required with *AWS S3 (STS Assume Role)* connection profile available from _Preferences… → Profiles_.
:::

## Create a bookmark in Cyberduck or Mountain Duck

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *AWS S3 (STS Assume Role)* connection profile.
3. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose **AWS S3 (STS Assume Role)* connection profile* in the protocol dropdown.

## Create a user with both access keys and a MFA device configured

1. In AWS [IAM console](https://console.aws.amazon.com/iam/) create a new user. Do *not* grant this user any permissions for S3.
2. In the _Security credentials_ tab, choose _Create access key_ and copy to the clipboard.
3. Enter access key ID and secret access key in the bookmark.
4. Assign a MFA device to the user in _Multi-factor authentication (MFA)_.

    :::{tip}
    To allow entering the code in Cyberduck or Mountain Duck when connecting, make sure to choose _Authenticator app_ or _Hardware TOTP token_ as a MFA device. Using Passkey MFA does not allow getting a numeric MFA code.
    :::
5. Copy the MFA device ARN to the clipboard.

## Create IAM role allowing access to S3 enforcing the MFA requirement

1. In AWS [IAM console](https://console.aws.amazon.com/iam/) create a new IAM role that has S3 permissions and requires MFA. The IAM role must have the trusted entity set to the previously created user's ARN.

    ```{code-block} json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::<ACCOUNT_ID>:user/<S3_USER>"
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "Bool": { "aws:MultiFactorAuthPresent": "true" }
                }
            }
        ]
    }
    ```

2. Copy the Role ARN to the clipboard.
3. Attach a permission policy to the role that grants access to S3 such as the managed policy `AmazonS3FullAccess`.

    ```{code-block} json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*"
                ],
                "Resource": "*"
            }
        ]
    }
    ```
   
    Restrict the permissions as necessary.

## Add inline policy to allow the user to assume the role with `sts:AssumeRole`

1. Navigate to the previously added IAM user to attach the `sts:AssumeRole` permission as an inline policy.
2. Add a permission policy for the user by choosing _Add permissions → Create inline policy_ in the _Permissions_ tab. In the policy editor opened, add the action `sts:AssumeRole` for the resource ARN referencing the IAM role `<S3-ROLE-NAME>` created previously allowing access to S3 with MFA.

    ```{code-block} json
    {
       "Version": "2012-10-17",
       "Statement": [
       {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "arn:aws:iam::<Account ID>:role/S3-ROLE-NAME"
        }
        ]
    }
    ```

## Connect to S3 using the bookmark
1. When not already configured in the bookmark, enter the static AWS credentials for the user with the permission to assume the IAM role when prompted.

   :::{image} _images/S3_AssumeRole_Login_Prompt.png
   :alt: Login Prompt
   :width: 400px
   :::

2. Enter the MFA device identification when prompted.

   :::{image} _images/S3_MFA_Device_Prompt.png
   :alt: MFA Device Prompt
   :width: 400px
   :::

   :::{tip}
   Enter the identification number of the MFA device that is associated with the user. The value is either the serial number for a hardware device
   (such as `<code>GAHT12345678</code>`) or an Amazon Resource Name (ARN) for a virtual device (such as `<code>arn:aws:iam::123456789012:mfa/device</code>`)
   :::

3. Enter the one-time MFA code from your device when prompted.

   :::{image} _images/S3_MFA_Code_Prompt.png
   :alt: MFA Code Prompt
   :width: 400px
   :::


:::{admonition} Troubleshooting
:class: warning
### `User: arn:aws:iam::<ACCOUNT_ID>:user/<USERNAME> is not authorized to perform: s3:ListAllMyBuckets because no identity-based policy allows the s3:ListAllMyBuckets action.`
This error occurs when the user does not have permission to list all buckets in the account. Possibly no attempt to assume the role was made.

### `The security token included in the request is invalid.`
The AWS access key ID and secret access key set for the bookmark are invalid.

### `MultiFactorAuthentication failed with invalid MFA one time pass code.`
The one-time MFA code already expired or is invalid.
:::

## Alternative: Using AWS CLI Configuration

Alternatively use the *[S3 (Credentials from AWS Command Line Interface) profile](../protocols/s3/index.md#connecting-using-credentials-from-aws-command-line-interface)* to read values from the AWS CLI `~/aws/credentials` file.

1. Copy the Access Key ID and Secret Access Key to a profile in `~/.aws/credentials`

    ```{code-block} properties
    [<S3_USER>]
    aws_access_key_id=AKIA…
    aws_secret_access_key=…
    ```

2. Copy the MFA ARN and reference it in the `mfa_serial` parameter in the `<S3-ROLE-NAME>` profile in `~/.aws/credentials`. This will require the user to enter a MFA code when assuming a role with a S3 access policy attached when connecting.
    ```{code-block} properties
    [<S3-ROLE-NAME>]
    source_profile=<S3_USER>
    role_arn=arn:aws:iam::<Account ID>:role/<S3-ROLE-NAME>
    mfa_serial=arn:aws:iam::<Account ID>:mfa/<MFA-DEVICE-NAME>
    ```

3. Enter the alias `<S3-ROLE-NAME>` for the role configuration from your AWS CLI configuration in _Server_ of the bookmark.


## Alternative: Use Custom Connection Profile

1. Add the `role_arn` and `mfa_serial` to a [custom connection profile](../protocols/profiles/index.md) to skip the prompts on connect.
    ```{code-block}
    <key>Token Configurable</key>
    <true/>
    <key>Properties</key>
    <dict>
        <!-- Require Role ARN input from user -->
        <key>role_arn</key>
        <string>arn:aws:iam::<Account ID>:role/<S3-ROLE-NAME></string>
        <!-- Can be left blank. Enter ARN for MFA device when assuming role requires token from MFA -->
        <key>mfa_serial</key>
        <string>arn:aws:iam::<Account ID>:mfa/<MFA-DEVICE-NAME></string>
    </dict>
    ```