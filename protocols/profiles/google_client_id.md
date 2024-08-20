Custom OAuth 2.0 Client ID for Google Cloud Storage and Google Drive
====

Instructions to register a custom OAuth 2.0 Client ID in the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) to connect to [Google Drive](../googledrive.md) or [Google Storage](../googlecloudstorage.md).

> To use OAuth 2.0 in your application, you need an OAuth 2.0 client ID, which your application uses when requesting an OAuth 2.0 access token.

## Register Client ID

:::{admonition} Tutorial
:class: tip

Follow the [step-by-step instructions](../../tutorials/custom_oauth_client_id.md) to setup a Custom OAuth Client ID.
:::

Follow the steps in [Setting up OAuth 2.0](https://support.google.com/googleapi/answer/6158849?hl=en). From Credentials copy the client ID and client secret by choosing the action Edit OAuth client.

* Choose _Desktop app_ as the _Application type_ which will result in a Client ID with a suffix like `number-id.apps.googleusercontent.com`.

:::{image} _images/Google_Create_OAuth_Client_ID.png
:alt: Google Create OAuth Client ID
:width: 600px
:::

:::{image} _images/Google_Client_ID_and_client_secret.png
:alt: Google Client ID and Client Secret
:width: 600px
:::

* Edit the OAuth Consent Screen* to add the scopes *Google Cloud Storage JSON API* `../auth/devstorage.read_write` and/or *Google Drive API* `../auth/drive`. You will first need to enable *Google Drive* in the Google API Library.

## Edit Custom Connection Profile

Create a custom [connection profile](index.md) with the following properties.

- `OAuth Client ID`. Override the registered application client id.
- `OAuth Client Secret`. Optional. Override the registered application client secret.
- `OAuth Redirect Url`. Use the reverse notation of the client id and set it like

```
        <key>OAuth Redirect Url</key>
        <string>com.googleusercontent.apps.number-id:oauth</string>
```

### Sample Google Drive with Custom OAuth Client ID Connection Profile

- {download}`Google Drive Custom OAuth Client ID.cyberduckprofile<_static/Google Drive Custom OAuth Client ID.cyberduckprofile>`

### Sample Google Cloud Storage with Custom OAuth Client ID Connection Profile

- {download}`Google Storage Custom OAuth Client ID.cyberduckprofile<_static/Google Storage Custom OAuth Client ID.cyberduckprofile>`