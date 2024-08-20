Setup a Custom OAuth Client ID for Google Drive & Google Cloud Storage
===

This is a step-by-step tutorial to connect with a custom OAuth 2.0 Client ID for [Google Cloud Storage](../protocols/googlecloudstorage.md) and [Google Drive](../protocols/googledrive.md).

:::{contents} Content
:depth: 2
:local:
:::

## Register Client ID

- Log in to [Google Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager) and create a new project. You will be prompted to select a name of the project.

:::{image} _images/Create_New_Project_Client_ID.png
:alt: Create new Project
:width: 800px
:::

- Navigate to _APIs & Services_ → _Enabled APIs & services_.

:::{image} _images/APIs_Services_Client_ID.png
:alt: APIs and Services
:width: 800px
:::

- Select _Enable APIs & Services_ and search for "Google Drive API" in the search box of the API library.

:::{image} _images/Enable_APIs_Client_ID.png
:alt: Enable APIs
:width: 800px
:::

- Select _Google Drive API_ from the search results and choose _Enable_. Repeat the same for _Google Cloud Storage JSON API_ when you want to access Google Cloud Storage.

:::{image} _images/Search_Google_API.png
:alt: API Library Google Drive
:width: 800px
:::

- Navigate to _APIs & Services → OAuth consent screen_.

:::{image} _images/Consent_Screen_Client_ID.png
:alt: Consent Screen OAuth Client ID
:width: 800px
:::

- Choose _External_ from _User Type_ and select _Create_. Choose any _App Name_ and select _Save and Continue_.

:::{image} _images/App_Information_Client_ID.png
:alt: App Information OAuth Client ID
:width: 800px
:::

- Select _Add or Remove Scopes_ in the next step. Search for "Google Drive API" and enable the scope `.../auth/drive`. Repeat the same for `.../auth/devstorage.full_control` when you want to access Google Cloud Storage. Select _Update_ to confirm and _Save and Continue_ to move to the next step.

:::{image} _images/List_of_Scopes_Client_ID.png
:alt: List of Scopes OAuth Client ID
:width: 800px
:::

- Add an email address registered as a Google account after selecting _Add Users_. Confirm by selecting _Save and Continue_.

:::{image} _images/Test_Users_Client_ID.png
:alt: Test Users OAuth Client ID
:width: 800px
:::

- Navigate to _APIs & Services → Credentials_ and select _OAuth client ID_ from _Create Credentials_.

:::{image} _images/Client_ID_Credentials.png
:alt: OAuth Client ID Credentials
:width: 800px
:::

- Select _Desktop app_ for _Application type_ and enter any _Name_. Select _Create_ to continue.

:::{image} _images/Application_Type_Client_ID.png
:alt: Application Type for Credentials
:width: 800px
:::

- Copy the _Client ID_ displayed. You will need it to set up the custom connection profile in the next step.

:::{image} _images/OAuth_Client_ID_Credentials.png
:alt: OAuth Client ID Credentials
:::

## Add Custom Connection Profile

Download the [template](../protocols/profiles/google_client_id.md#sample-google-drive-with-custom-oauth-client-id-connection-profile) for Google Drive or Google Cloud Storage:
- {download}`Google Drive Custom OAuth Client ID.cyberduckprofile<../protocols/profiles/_static/Google Drive Custom OAuth Client ID.cyberduckprofile>`
- {download}`Google Storage Custom OAuth Client ID.cyberduckprofile<../protocols/profiles/_static/Google Storage Custom OAuth Client ID.cyberduckprofile>`


Use the _OAuth Client ID_ created to edit the `OAuth Client ID` and `OAuth Redirect Url` in the template connection profile leaving other keys unchanged.

```xml
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        …
        <key>OAuth Client ID</key>
        <string>NUMBER-ID.apps.googleusercontent.com</string>
        <key>OAuth Redirect Url</key>
        <string>com.googleusercontent.apps.NUMBER-ID:oauth</string>
        …
    </dict>
</plist>
```

- `OAuth Client ID`. Override the registered application OAuth Client ID.
- `OAuth Redirect Url`. Use the reverse notation of the OAuth Client ID and append `:oauth` to it.


Double-click the connection profile to open and register or copy to the _Profiles_ folder in the [application support folder](../cyberduck/support.md#application-support-folder).

## Update Protocol Selection in Bookmark

The saved profile will be available in the _Protocol_ section of the [bookmark](../cyberduck/bookmarks.md#bookmark-options) configuration. 