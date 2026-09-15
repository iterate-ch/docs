Connect to ownCloud Infinite Scale & OpenCloud with OpenID Connect
====

> Authenticate with the OpenID Connect (OIDC) identity provider configured for your [ownCloud Infinite Scale (oCIS)](https://owncloud.dev/ocis/) or [OpenCloud](https://opencloud.eu/) deployment using a custom connection profile.

Both ownCloud Infinite Scale and OpenCloud disable Basic Authentication by default and require OAuth 2.0 tokens issued by the identity provider (IdP) in use such as the built-in IdP, Keycloak or Microsoft Entra ID. This tutorial explains how to obtain the OAuth endpoints and client configuration from the public configuration published by your server and how to write a [connection profile](../protocols/profiles/index.md) for use with [Cyberduck](../cyberduck/index.md) and [Mountain Duck](../mountainduck/index.md).

:::{note}
Cyberduck [9.3.0](https://cyberduck.io/changelog/) and Mountain Duck [5.1.0](https://mountainduck.io/changelog/) or later set the username from the ID token after login to connect to the user home at `/remote.php/dav/files/<username>`. Previous versions connect to `/remote.php/webdav`.
:::

The examples below use the OpenCloud deployment at `cloud.example.net` which is configured with Microsoft Entra ID as the identity provider. Replace the hostname with your own server, the tenant ID `00000000-0000-0000-0000-000000000000` with your Microsoft Entra tenant ID and the client ID `11111111-1111-1111-1111-111111111111` with the OAuth Client ID of your application registration.

## Discover the OAuth Configuration

### OpenID Connect Discovery Document

The server publishes the [OpenID Connect discovery document](https://openid.net/specs/openid-connect-discovery-1_0.html) at `/.well-known/openid-configuration`. Open the URL in a web browser or fetch it using `curl`.

```bash
curl -s https://cloud.example.net/.well-known/openid-configuration | jq '{issuer, authorization_endpoint, token_endpoint, scopes_supported}'
```

```json
{
  "issuer": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/v2.0",
  "authorization_endpoint": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/oauth2/v2.0/authorize",
  "token_endpoint": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/oauth2/v2.0/token",
  "scopes_supported": [
    "openid",
    "profile",
    "email",
    "offline_access"
  ]
}
```

:::{tip}
If the document is not available on the server hostname, look up the issuer using WebFinger and append `/.well-known/openid-configuration` to the `href` returned.

```bash
curl -s "https://cloud.example.net/.well-known/webfinger?resource=https%3A%2F%2Fcloud.example.net"
```
:::

### Web Client Configuration

The OAuth Client ID and scopes requested by the web interface are published in `/config.json`.

```bash
curl -s https://cloud.example.net/config.json | jq '.openIdConnect'
```

```json
{
  "metadata_url": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/v2.0/.well-known/openid-configuration",
  "authority": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/v2.0",
  "client_id": "11111111-1111-1111-1111-111111111111",
  "response_type": "code",
  "scope": "openid profile email offline_access api://11111111-1111-1111-1111-111111111111/opencloud"
}
```

:::{note}
Access tokens must be issued for an audience accepted by the server. Request the same scopes as the web client, including any API scope such as `api://…/opencloud` required with Microsoft Entra ID.
:::

### Map to Connection Profile Keys

| Source                                            | Value                    | Connection Profile Key    |
|---------------------------------------------------|--------------------------|---------------------------|
| `/.well-known/openid-configuration`               | `authorization_endpoint` | `OAuth Authorization Url` |
| `/.well-known/openid-configuration`               | `token_endpoint`         | `OAuth Token Url`         |
| `/config.json`                                    | `openIdConnect.client_id`| `OAuth Client ID`         |
| `/config.json`                                    | `openIdConnect.scope`    | `Scopes`                  |

## Register Redirect URIs in Identity Provider

After login in the web browser, the identity provider redirects back to the application. Register the redirect URIs matching the `OAuth Redirect Url` in the connection profile with the OAuth client in your identity provider.

:::::{tabs}
::::{tab} Custom URL Scheme

- `x-cyberduck-action:oauth` for Cyberduck
- `x-mountainduck-action:oauth` for Mountain Duck

::::
::::{tab} Loopback Address

- `http://localhost/` for both Cyberduck and Mountain Duck

The application listens on a random port on the loopback interface to receive the authorization code. This option requires the identity provider to accept redirect URIs to the loopback interface with any port as recommended for native apps in [RFC 8252](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3). Both Microsoft Entra ID and Keycloak support registering `http://localhost` without a port.

:::{admonition} Requirements
:class: warning
* Cyberduck [9.5.0](https://cyberduck.io/changelog/) or later required
* Mountain Duck [5.3.0](https://mountainduck.io/changelog/) or later required
:::

::::
:::::

:::::{tabs}
::::{tab} Microsoft Entra ID

1. Open the application registration for the OAuth Client ID in the [Microsoft Entra admin center](https://entra.microsoft.com/) in _Identity → Applications → App registrations_.
2. Navigate to _Authentication_ and choose _Add a platform_ → _Mobile and desktop applications_.
3. Enter `x-cyberduck-action:oauth` in _Custom redirect URIs_ and choose _Configure_. Repeat for `x-mountainduck-action:oauth`. When using the loopback address, enter `http://localhost` instead.

:::{note}
Microsoft Entra ID ignores the port number for redirect URIs with `localhost`.
:::

:::{important}
Redirect URIs registered for the _Single-page application_ platform used by the web interface cannot be used by Cyberduck and Mountain Duck.
:::

::::
::::{tab} Keycloak

**Import client configuration for Keycloak**

Import a sample client configuration with _Import client_ in _Clients_ of the Keycloak admin console to allow OAuth authentication from Cyberduck & Mountain Duck. Both register the redirect URIs `x-cyberduck-action:oauth` and `x-mountainduck-action:oauth`.

- [OpenCloud GitHub repository](https://github.com/opencloud-eu/opencloud/blob/main/devtools/deployments/multi-tenancy/config/keycloak/clients/cyberduck.json). Registers a public client with the Client ID `Cyberduck` requiring no client secret. Set an empty `OAuth Client Secret` in the connection profile.
- [ownCloud GitHub repository](https://github.com/owncloud/ocis/blob/7af9cd9e53183acbaac2ffbc6414402bdef1f5d4/deployments/examples/ocis_keycloak/config/keycloak/clients/cyberduck.json). Registers a confidential client with _Client authentication_ enabled.

:::{important}
For a confidential client, set the client secret from the _Credentials_ tab of the client in `OAuth Client Secret` of the connection profile or disable _Client authentication_ to register a public client.
:::

**Configure existing client**

1. Open the client for the OAuth Client ID in the Keycloak admin console in _Clients_.
2. Add `x-cyberduck-action:oauth` and `x-mountainduck-action:oauth` to _Valid redirect URIs_ and choose _Save_. When using the loopback address, add `http://localhost/` instead.

:::{note}
Keycloak ignores the port number for redirect URIs with `localhost`, `127.0.0.1` and `[::1]`.
:::

::::
::::{tab} OpenCloud Built-in Identity Provider

No client registration is required when using the built-in identity provider of OpenCloud. The public client with the Client ID `OpenCloudDesktop` registered by default for the OpenCloud Desktop Client accepts redirect URIs to the loopback interface with any port.

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *OpenCloud (OpenID Connect)* connection profile.
3. Add a new [bookmark](../cyberduck/bookmarks.md) and choose *OpenCloud (OpenID Connect)* in the protocol dropdown. Enter the hostname of your OpenCloud server in _Server_.

:::{note}
On first login you are asked to allow access for _OpenCloud Desktop Client_. Consent is required to obtain a refresh token with the `offline_access` scope.
:::

:::{attention}
The client registration is part of the default configuration of the built-in identity provider and may have been changed by the server administrator.
:::

::::
::::{tab} ownCloud Infinite Scale Built-in Identity Provider

No client registration is required when using the built-in identity provider of ownCloud Infinite Scale. The client registered by default for the _ownCloud desktop app_ accepts redirect URIs to the loopback interface with any port.

1. Open _Preferences… → Profiles_ in Cyberduck or Mountain Duck.
2. Enable the *ownCloud Infinite Scale (OpenID Connect)* connection profile.
3. Add a new [bookmark](../cyberduck/bookmarks.md) and choose *ownCloud Infinite Scale (OpenID Connect)* in the protocol dropdown. Enter the hostname of your ownCloud Infinite Scale server in _Server_.

:::{note}
On first login you are asked to allow access for _ownCloud desktop app_. Consent is required to obtain a refresh token with the `offline_access` scope.
:::

:::{important}
Unlike the client registered in OpenCloud, the client is confidential and requires the client secret validated by the token endpoint. The connection profile includes the default client secret published in the [ownCloud Infinite Scale configuration](https://github.com/owncloud/ocis/blob/master/services/idp/pkg/config/defaults/defaultconfig.go).
:::

:::{attention}
The client registration is part of the default configuration of the built-in identity provider and may have been changed by the server administrator.
:::

::::
:::::

:::{note}
Alternatively register a dedicated OAuth client for Cyberduck and Mountain Duck with the identity provider as long as the access token issued is accepted by the server.
:::

## Write Connection Profile

Create a file with the extension `.cyberduckprofile` using a text editor.

:::::{tabs}
::::{tab} Blueprint

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>owncloud</string>
        <key>Vendor</key>
        <string>…</string>
        <key>Description</key>
        <string>…</string>
        <key>Default Hostname</key>
        <string>…</string>
        <key>Hostname Configurable</key>
        <false/>
        <key>OAuth Authorization Url</key>
        <string>…</string>
        <key>OAuth Token Url</key>
        <string>…</string>
        <key>OAuth Client ID</key>
        <string>…</string>
        <key>OAuth Client Secret</key>
        <string></string>
        <key>OAuth Redirect Url</key>
        <string>${oauth.handler.scheme}:oauth</string>
        <key>OAuth PKCE</key>
        <true/>
        <key>Scopes</key>
        <array>
            <string>openid</string>
            <string>profile</string>
            <string>email</string>
            <string>offline_access</string>
        </array>
        <key>Username Configurable</key>
        <false/>
        <key>Password Configurable</key>
        <false/>
    </dict>
</plist>
```

- `Protocol` Must be `owncloud` to connect using WebDAV with [ownCloud extensions](../protocols/webdav/nextcloud.md) such as resumable uploads, versioning and sharing.
- `Vendor` Unique identifier for the connection profile.
- `Default Hostname` Hostname of the server. Set `Hostname Configurable` to `false` to prevent editing.
- `OAuth Authorization Url` The `authorization_endpoint` from the discovery document.
- `OAuth Token Url` The `token_endpoint` from the discovery document.
- `OAuth Client ID` The `client_id` from `config.json` or of a dedicated client registered with the identity provider. Use `OpenCloudDesktop` with the built-in identity provider of OpenCloud.
- `OAuth Client Secret` Set an empty value for public clients to not send a client secret. Omit the key to prompt for input when connecting. Set the client secret when the client registered is confidential such as the sample client configuration for Keycloak from ownCloud.
- `OAuth Redirect Url` Resolves to `x-cyberduck-action:oauth` in Cyberduck and `x-mountainduck-action:oauth` in Mountain Duck allowing the same profile to be used in both applications. Alternatively set to `http://localhost/` with Cyberduck 9.5.0 and Mountain Duck 5.3.0 or later when the identity provider accepts redirect URIs to the loopback interface with any port.
- `OAuth PKCE` Use Proof Key for Code Exchange (PKCE). Enabled by default.
- `Scopes` The scopes requested. Include `offline_access` to obtain a refresh token and not require to login again when the access token expires. Add `openid` to obtain an ID token used to determine the username.
- `Username Configurable` and `Password Configurable` Set to `false` as no credentials are required. The username is set from the `preferred_username` claim in the ID token after login with Cyberduck 9.3.0 and Mountain Duck 5.1.0 or later.

::::
::::{tab} Example (Microsoft Entra ID)

Connection profile for the OpenCloud deployment at `cloud.example.net` with Microsoft Entra ID as identity provider:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>owncloud</string>
        <key>Vendor</key>
        <string>cloud.example.net-entra</string>
        <key>Description</key>
        <string>OpenCloud Entra ID (cloud.example.net)</string>
        <key>Default Nickname</key>
        <string>OpenCloud</string>
        <key>Default Hostname</key>
        <string>cloud.example.net</string>
        <key>Hostname Configurable</key>
        <false/>
        <key>OAuth Authorization Url</key>
        <string>https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/oauth2/v2.0/authorize</string>
        <key>OAuth Token Url</key>
        <string>https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/oauth2/v2.0/token</string>
        <key>OAuth Client ID</key>
        <string>11111111-1111-1111-1111-111111111111</string>
        <key>OAuth Client Secret</key>
        <string></string>
        <key>OAuth Redirect Url</key>
        <string>${oauth.handler.scheme}:oauth</string>
        <key>OAuth PKCE</key>
        <true/>
        <key>Scopes</key>
        <array>
            <string>openid</string>
            <string>profile</string>
            <string>email</string>
            <string>offline_access</string>
            <string>api://11111111-1111-1111-1111-111111111111/opencloud</string>
        </array>
        <key>Username Configurable</key>
        <false/>
        <key>Password Configurable</key>
        <false/>
    </dict>
</plist>
```

::::
::::{tab} Example (Keycloak)

Connection profile for an OpenCloud deployment at `cloud.example.net` with Keycloak at `keycloak.example.net` as identity provider using the realm `openCloud` and the public client `Cyberduck` imported from the [sample client configuration](https://github.com/opencloud-eu/opencloud/blob/main/devtools/deployments/multi-tenancy/config/keycloak/clients/cyberduck.json):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>owncloud</string>
        <key>Vendor</key>
        <string>cloud.example.net-keycloak</string>
        <key>Description</key>
        <string>OpenCloud Keycloak (cloud.example.net)</string>
        <key>Default Nickname</key>
        <string>OpenCloud</string>
        <key>Default Hostname</key>
        <string>cloud.example.net</string>
        <key>Hostname Configurable</key>
        <false/>
        <key>OAuth Authorization Url</key>
        <string>https://keycloak.example.net/realms/openCloud/protocol/openid-connect/auth</string>
        <key>OAuth Token Url</key>
        <string>https://keycloak.example.net/realms/openCloud/protocol/openid-connect/token</string>
        <key>OAuth Client ID</key>
        <string>Cyberduck</string>
        <key>OAuth Client Secret</key>
        <string></string>
        <key>OAuth Redirect Url</key>
        <string>${oauth.handler.scheme}:oauth</string>
        <key>OAuth PKCE</key>
        <true/>
        <key>Scopes</key>
        <array>
            <string>openid</string>
            <string>profile</string>
            <string>email</string>
            <string>offline_access</string>
        </array>
        <key>Username Configurable</key>
        <false/>
        <key>Password Configurable</key>
        <false/>
    </dict>
</plist>
```

::::
:::::

## Install Connection Profile

Double-click the `.cyberduckprofile` file to install it or copy it to the _Profiles_ folder in the [application support folder](../cyberduck/support.md#application-support-folder).

## Create Bookmark

1. Add a new [bookmark](../cyberduck/bookmarks.md) in Cyberduck or Mountain Duck and choose the connection profile in the _Protocol_ dropdown.
2. Connect to the bookmark. The login page of the identity provider opens in your default web browser.
3. After successful login, you are redirected back to Cyberduck or Mountain Duck. The OAuth tokens are saved in the Keychain on macOS or Credential Manager on Windows.

:::{admonition} Troubleshooting
:class: attention

### `AADSTS50011: The redirect URI specified in the request does not match`
The redirect URI `x-cyberduck-action:oauth`, `x-mountainduck-action:oauth` or `http://localhost` is not registered for the application in Microsoft Entra ID. Register the redirect URI for the _Mobile and desktop applications_ platform.

### `AADSTS9002327: Tokens issued for the 'Single-Page Application' client-type may only be redeemed via cross-origin requests`
The redirect URI is registered for the _Single-page application_ platform. Register the redirect URI for the _Mobile and desktop applications_ platform instead.

### `AADSTS7000218: The request body must contain the following parameter: 'client_assertion' or 'client_secret'`
The application registration requires a client secret. Enable _Allow public client flows_ in _Authentication_ of the application registration or set `OAuth Client Secret` in the connection profile.

### `Invalid redirect_uri` with Keycloak
Add `x-cyberduck-action:oauth` and `x-mountainduck-action:oauth` or the loopback address set in `OAuth Redirect Url` to _Valid redirect URIs_ of the client.

### Login Failure with `401 Unauthorized` after successful login in web browser
The access token is not accepted by the server. Make sure to request the same scopes as the web client from `config.json` in `Scopes` of the connection profile.
:::

## References

- [NextCloud & ownCloud](../protocols/webdav/nextcloud.md)
- [Connection Profiles](../protocols/profiles/index.md)
- [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)
- [OpenCloud Documentation](https://docs.opencloud.eu/)
- [ownCloud Infinite Scale → Authentication](https://doc.owncloud.com/ocis/next/deployment/services/s-list/auth-basic.html)
- [Microsoft identity platform → Redirect URI best practices](https://learn.microsoft.com/en-us/entra/identity-platform/reply-url)
