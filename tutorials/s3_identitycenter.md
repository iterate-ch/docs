Connect to S3 authenticating with AWS IAM Identity Center
====

> [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/) (successor to AWS Single Sign-On) centrally
> manages access to multiple AWS accounts. It enables users
> to sign in once using their existing corporate credentials (such as Okta or Microsoft Entra ID) to access authorized
> resources like S3 via short-lived credentials.
> Use AWS IAM Identity Center to authenticate with S3 by configuring as an OpenID Connect (OIDC) Identity Provider in
> AWS IAM.

The [AWS IAM Identity Center OpenID Connect (OIDC) web service](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html)
is used to
authenticate users with AWS IAM Identity Center.

:::{admonition} Requirements
:class: warning

* Cyberduck [9.5.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.3.0](https://mountainduck.io/changelog/) or later required
  :::

## Configuration in AWS IAM Identity Center

In [AWS IAM Identity Center Console](https://console.aws.amazon.com/singlesignon) choose to *Enable IAM Identity Center*
in a dedicated region.

1. Follow the
   documentation [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).
   Optionally
   customize [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-the-access-portal.html)
   URL in _Settings → Identity source → Actions → Customize AWS access portal_ and configure a custom external identity
   provider (IdP) to manage users and groups by following the
   [documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) such
   as [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/aws-single-sign-on-tutorial).

2. Copy the following values or alternatively setup your configuration
   with AWS CLI:

   :::{admonition} Required Configuration Values
   :class: note
    - _Account ID_ identifying your AWS account from the top right corner of the AWS console.
    - _Region_ from _Dashboard → Settings summary → Region_
    - SSO start URL from _Dashboard → Settings summary → Issuer URL_ or _AWS access portal URL → Dual-stack_.
      :::

   :::{tip}
   Users can copy the _SSO start URL_ from the _AWS access portal_ page at _Accounts → Access keys → AWS IAM Identity Center credentials (Recommended)_.
   :::

3. Create a permission set to limit access for users to S3 in _Permission sets → Create permission set_.
    - Choose _Custom permission set_ in _Select permission set type_ and select _Next_.
    - Expand _AWS managed policies_ and select _AmazonS3FullAccess_ or _AmazonS3ReadOnlyAccess_ and optionally
      _CloudFrontFullAccess_ managed policies and select _Next_.
    - Name the permission set and select _Next_.
    - Select _Create_ and copy the _Permission set name_ from _General settings_.

## Setup Users and Groups

:::{tip}
Alternatively attach a custom identity source in _Settings → Identity source_. You will manage all users and groups in
an external identity provider (IdP).
:::

1. Choose _Users → Add user_ and create a user with a password.
2. The user must login to the AWS access portal URL `awsapps.com/start` with the username and one-time password.
3. Assign a AWS account to the user in _Users → Username → AWS accounts → Assign accounts_.
4. Select the _AWS Organization_ and assign the [previously created](#configuration-in-aws-iam-identity-center)
   _Permission Set_ and
   select _Assign_.

## Create a bookmark in Cyberduck or Mountain Duck

1. Add a new [Bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose *AWS S3 (IAM Identity
   Center)* in the protocol dropdown.
2. Choose _Connect_ and select the AWS CLI profile name when prompted.

   :::{image} _images/S3_CLI_Profile_Prompt.png
   :alt: AWS CLI Profile Prompt
   :width: 400px
   :::

   :::{tip}
   Choose _Cancel_ to skip configuration from the AWS CLI profile and continue with manual configuration.
   :::

   :::{admonition} Using AWS CLI Configuration
   :class: tip
   Pre-configure the settings using AWS CLI to allow reading configuration options from the `~/aws/config`
   file including the _Issuer URL_.

    1. Obtain your IAM Identity Center [configuration](#configuration-in-aws-iam-identity-center) information.
    2. Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    3. Configure your profile with the `aws configure sso` wizard using the command line:

       ```
       $ aws configure sso
       SSO session name (Recommended): my-sso
       SSO start URL [None]: https://my-sso-portal.awsapps.com/start
       SSO region [None]: us-east-1
       SSO registration scopes [None]: sso:account:access
       ```

       :::

3. Choose the _SSO Region_ when prompted.

   :::{warning}
   Must match the region selected when [setting up](#configuration-in-aws-iam-identity-center) IAM Identity Center in
   AWS.
   :::

   :::{image} _images/AWS_Region_Prompt.png
   :alt: AWS Region Prompt
   :width: 400px
   :::

4. Enter the _Issuer URL_ or _AWS Access Portal URL_ when prompted.

   :::{image} _images/AWS_Identity_Center_Issuer_URL_Prompt.png
   :alt: AWS IAM Identity Center Issuer URL Prompt
   :width: 400px
   :::

5. Login to AWS or your third-party identity provider followed by allowing access to Cyberduck or Mountain Duck.

   :::{image} _images/IAM_IdentityCenter_Allow_Access.png
   :alt: Web Browser Screenshot
   :width: 800px
   :::

   :::{tip}
   You can close the web browser window after confirming access.
   :::

6. Choose the _AWS Account ID_ when prompted.

   :::{tip}
   This step is skipped if only a single AWS account is configured with your AWS IAM Identity Center instance.
   :::

7. Choose the _Permission set name_ when prompted previously [configured](#configuration-in-aws-iam-identity-center).

   :::{tip}
   This step is skipped if only a single AWS account is configured with your AWS IAM Identity Center instance.
   :::

:::{admonition} Troubleshooting
:class: warning

### `Start URL region does not match service region`

Make sure to select the region matching the location in the issuer URL of the AWS IAM Identity Center.
:::

### References

- [Integrating AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
