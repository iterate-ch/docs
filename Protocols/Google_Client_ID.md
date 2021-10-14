Custom OAtuh 2.0 Client ID for Google Cloud Storage and Google Drive
===

> To use OAuth 2.0 in your application, you need an OAuth 2.0 client ID, which your application uses when requesting an OAuth 2.0 access token.

# Verification Issue

Login using OAuth is currently failing with the default OAuth Client ID application registration in Cyberduck. When attempting to allow access for Cyberduck to Google Drive, the following error is displayed.

```{error}
Sign in with Google temporarily disabled for this app. This app has not been verified yet by Google in order to use Google Sign In.
```

As a workaround, you can register your own OAuth Client ID to connect to [Google Drive](Google_Drive). For [Google Storage](Google_Cloud_Storage) you can use [Interoperable Access](Google_Cloud_Storage#interoperable-access) as a workaround.

# Register Client ID

Follow the steps in [Setting up OAuth 2.0](https://support.google.com/googleapi/answer/6158849?hl=en). From Credentials copy the client ID and client secret by choosing the action Edit OAuth client.

```{image} _images/Google_Create_OAuth_Client_ID.png
:alt: Google Create OAuth Client ID
:width: 600px
```
```{image} _images/Google_Client_ID_and_client_secret.png
:alt: Google Client ID and Client Secret
:width: 600px
```

*Edit the OAuth Consent Screen* to add the scopes *Google Cloud Storage JSON API* `../auth/devstorage.read_write` and/or *Google Drive API* `../auth/drive`. You will first need to enable *Google Drive* in the Google API Library.

# Edit Custom Connection Profile

Create a custom [connection profile](Cyberduck/Profiles) with the following properties.

- `OAuth Client ID`. Override the registered application client id.
- `OAuth Client Secret`. Override the registered application client secret.

## Sample Google Drive with Custom OAuth Client ID Connection Profile

- {download}`Google Drive Custom OAuth Client ID.cyberduckprofile<_static/Ressources/Google Drive Custom OAuth Client ID.cyberduckprofile>`

## Sample Google Cloud Storage with Custom OAuth Client ID Connection Profile

- {download}`Google Storage Custom OAuth Client ID.cyberduckprofile<_static/Ressources/Google Storage Custom OAuth Client ID.cyberduckprofile>`