Custom connection profile using OpenID Connect provider and AssumeRoleWithWebIdentity STS API
====

> With web identity federation, you don't need to create custom sign-in code or manage your own user identities. Instead, users of your app can sign in using a well-known external identity provider (IdP), such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP. They can receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account.

```{important}
* Cyberduck [8.7.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [4.15.0](https://mountainduck.io/changelog/) or later required
```

Connection profiles must include the `OAuth Authorization Url`, `OAuth Token Url`, `OAuth Redirect Url` and `Scopes` of the OpenID Connect (OIDC) identity provider and the `STS Endpoint` for the STS API endpoint which defaults to `https://sts.amazonaws.com/`. Set the property `s3.assumerole.rolearn` in the connection profile to the Role ARN configured in AWS. Set it to `s3.assumerole.rolearn=` for a prompt to enter on login.

## Prerequisites

- Register the OAuth Client ID with your identity provider (IdP)
- Configure the OIDC provider in AWS IAM or compatible implementation like [MinIO Security Token Service (STS)](https://min.io/docs/minio/linux/developers/security-token-service.html)
- Make sure to restrict access by configuring the role and trust policy using rules referencing the claims available in the JWT token from the identity provider that is passed to `AssumeRoleWithWebIdentity` STS API.

## Blueprint

```xml
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>s3</string>
        <key>Vendor</key>
        <string>s3-sts</string>
        <key>OAuth Authorization Url</key>
        <string>…</string>
        <key>OAuth Token Url</key>
        <string>…</string>
        <key>OAuth Client ID</key>
        <string>…</string>
        <key>OAuth Client Secret</key>
        <string>…</string>
        <key>OAuth Redirect Url</key>
        <string>x-cyberduck-action:oauth</string>
        <key>OAuth PKCE</key>
        <false/>
        <key>Scopes</key>
        <array>
            <string>openid</string>
            <string>offline_access</string>
        </array>
        <key>Authorization</key>
        <string>AuthorizationCode</string>
        <key>Password Configurable</key>
        <false/>
        <key>Username Configurable</key>
        <false/>
        <key>Token Configurable</key>
        <false/>
        <key>Username Placeholder</key>
        <string>Username</string>
        <key>STS Endpoint</key>
        <string>https://sts.amazonaws.com/</string>
        <key>Properties</key>
        <array>
            <string>s3.assumerole.rolearn=arn:aws:iam::…</string>
        </array>
    </dict>
</plist>
```

### References 

- [About web identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)