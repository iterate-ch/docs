Connect to S3 authenticating with Google Cloud
====

> Use Google Cloud to authenticate with S3 by configuring as an OpenID Connect (OIDC) Identity Provider in AWS IAM.


:::{tip}
Refer to [Custom connection profile using OpenID Connect provider and AssumeRoleWithWebIdentity STS API](../protocols/profiles/aws_oidc.md) for custom configuration of connection profiles using OIDC web identity federation to connect to AWS S3.
:::

:::{admonition} Requirements
:class: warning
* Cyberduck [9.3.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.1.0](https://mountainduck.io/changelog/) or later required
  :::

## Configuration in Google Cloud Console

Create an OAuth application in the [Google Cloud Console](https://console.cloud.google.com/auth/clients) and configure it as an OIDC Identity Provider.

:::{admonition} Setup a Custom OAuth Client ID Tutorial
:class: tip

Follow the [step-by-step instructions](custom_oauth_client_id.md) to Setup a Custom OAuth Client ID for Google.
:::


1. Navigate to _Solutions → All products → Management → Google Auth Platform → Clients_ in the [Google Cloud Console](https://console.cloud.google.com/auth/clients) and choose _Create client → OAuth client ID_.
2. Select _iOS_ as the application type.

   :::{important}
   Other types require a OAuth Client Secret and do not allow for a supported redirect URI.
   :::

3. Enter `io.cyberduck` for use with Cyberduck or `io.mountainduck` to use with Mountain Duck for the _Bundle ID_.
4. Copy the OAuth Client ID from the credentials screen.


## Configuration in AWS IAM

### Create an OIDC identity provider

:::{tip}
Google is already built-in to AWS as a trusted OIDC identity provider. Instead of using a ARN you can reference the built-in Google IdP in a role with `accounts.google.com`.
:::

### Create a role

Assign a role to the identity provider created in the previous step with permissions to access S3.

1. In AWS [IAM console](https://console.aws.amazon.com/iam/), choose _Create Role_ in _Roles_.
2. Select _Web identity_ as the trusted entity type.
3. Select _Google_ as the _Identity Provider_.
4. Enter the OAuth Client ID from the application registration in Google Cloud Console for _Audience_.
5. The resulting trust policy will look similar to the following:

    ```json
   {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "accounts.google.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "accounts.google.com:aud": "<OAuth Client ID>.apps.googleusercontent.com"
                }
            }
        }
    ]
   }
    ```

6. In the next step attach a permission policy to the role such as the managed policy `AmazonS3FullAccess`.
7. Copy the Role ARN from the _Summary_ tab.


### Create a bookmark in Cyberduck or Mountain Duck

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *AWS S3 (Google OpenID Connect)* connection profile.
3. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose *AWS S3 (Google)* in the protocol dropdown.
4. Enter the OAuth Client ID from the application registration in Google Cloud Console for _OAuth Client ID_ when prompted. It will be saved in the bookmark as a [custom property](hidden_properties.md#in-duck-bookmark-files).

   :::{image} _images/S3_Client_Id_Prompt.png
   :alt: OAuth Client ID Prompt
   :width: 400px
   :::

   :::{tip}
   The _OAuth Client ID_ is the same as the _OAuth Client ID_ from the application registration in Google Cloud Console with the `.apps.googleusercontent.com` suffix.
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
- [Google Identity Platform → OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect)
