Connect to S3 authenticating with Microsoft Entra ID
====

> Use Microsoft Entra ID to authenticate with S3 by configuring as an OpenID Connect (OIDC) Identity Provider in AWS IAM.


:::{tip}
Refer to [Custom connection profile using OpenID Connect provider and AssumeRoleWithWebIdentity STS API](../protocols/profiles/aws_oidc.md) for custom configuration of connection profiles using OIDC web identity federation to connect to AWS S3.
:::

:::{important}
* Cyberduck [9.3.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.1.0](https://mountainduck.io/changelog/) or later required
  :::

## Configuration in Microsoft Entra ID

Create an application in the [Microsoft Entra ID portal](https://entra.microsoft.com/) and configure it as an OIDC Identity Provider.

1. Navigate to _Entra ID → → App registrations_ in the [Microsoft Entra ID portal](https://entra.microsoft.com/) and choose _New registration_.
2. In _Authentication_, add a redirect URI with the value `x-cyberduck-action://oauth` to allow authentication with Cyberduck.
3. In _Authentication_, add a redirect URI with the value `x-mountainduck-action://oauth` to allow authentication with Mountain Duck.
4. Copy the OAuth Client ID from _Overview → Essentials → Application (client) ID_.


## Configuration in AWS IAM

### Create an OIDC identity provider
1. In AWS [IAM console](https://console.aws.amazon.com/iam/) add a new identity provider in _Identity providers_.
2. Configure the provider as type _OpenID Connect_ with the provider URL set to `https://login.microsoftonline.com/<TENANT-ID>/v2.0`. Replace <TENANT-ID> with your Microsoft Entra ID tenant ID. Copy the ARN for the next [step](#create-a-role).
3. Set the _Audience_ to the Application (client) ID from Microsoft Entra.

### Create a role

Assign a role to the identity provider created in the previous step with permissions to access S3.

1. In AWS [IAM console](https://console.aws.amazon.com/iam/) add a new role.
2. Choose _Assign role_ followed by _Create a new role_ with a _Web identity_ trusted entity type. It should have _Identity provider_ and _Audience_ options prefilled with the ARN of the identity provider and Client ID from Microsoft Entra.
3. The resulting trust policy will look similar to the following:

    ```json
   {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/login.microsoftonline.com/<TENANT-ID>/v2.0"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "login.microsoftonline.com/<TENANT-ID>/v2.0:aud": "<Application (client) ID>"
                }
            }
        }
    ]
   }
    ```
   
    :::{tip}
    The `<ACCOUNT_ID>` is replaced with your AWS account ID and `<Application (client) ID>` with the OAuth Client ID of the application you created in the previous [step](#configuration-in-microsoft-entra-id). For `Federated`, the ARN of the identity provider you created in the previous step is set. For the condition `aud` use the application client ID of the application you created in the previous step.
    :::

4. In the next step attach a permission policy to the role such as the managed policy `AmazonS3FullAccess`.
5. Copy the Role ARN from the _Summary_ tab.


### Create a bookmark in Cyberduck or Mountain Duck

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *AWS S3 (Microsoft Entra)* connection profile.
3. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose *AWS S3 (Microsoft Entra)* in the protocol dropdown.
4. Enter the Application (client) ID from the application registration in Microsoft Entra for _OAuth Client ID_ when prompted. It will be saved in the bookmark as a [custom property](hidden_properties.md#in-duck-bookmark-files).
    
   :::{image} _images/S3_Client_Id_Prompt.png
   :alt: OAuth Client ID Prompt
   :width: 400px
   :::

   :::{tip}
   The _OAuth Client ID_ is the same as the _Application (client) ID_ from the application registration in Microsoft Entra.
   :::

   :::{note}
   Alternatively set `OAuth Client ID` in a [custom connection profile](../protocols/profiles/aws_oidc.md).
   :::

5. Enter the Role ARN from the previous step when prompted. It will be saved in the bookmark as a [custom property](hidden_properties.md#in-duck-bookmark-files).

   :::{note}
   Alternatively set `role_arn` as a custom property in a [custom connection profile](../protocols/profiles/aws_oidc.md).
   :::

   :::{image} _images/S3_Role_ARN_Prompt.png
   :alt: MFA Prompt
   :width: 400px
   :::

:::{admonition} Troubleshooting
:class: attention
### `Not authorized to perform sts:AssumeRoleWithWebIdentity`
Validate the _Trusted entities_ in _Trust relationships_ in the IAM console.

### `Request ARN is invalid`
The role ARN entered is not valid.

### `The security token included in the request is invalid`
Invalid client token ID. Check the OAuth Client ID in the connection profile.
:::

## References
- [AWS Identity and Access Management → OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)