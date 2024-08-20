Setup a Custom OAuth Client ID for Google Drive & Google Cloud Storage
===

This is a step-by-step tutorial to connect with a custom OAuth 2.0 Client ID for [Google Cloud Storage](../protocols/googlecloudstorage.md) and [Google Drive](../protocols/googledrive.md).

:::{contents} Content
:depth: 2
:local:
:::

## Register Client ID

Log in to your Google account, go to [Google Cloud resource manager](https://console.cloud.google.com/cloud-resource-manager) and create a new project.

:::{image} _images/Create_New_Project_Client_ID.png
:alt: Create new Project
:width: 800px
:::

You will be prompt to select a name of the project. Once the project is created navigate to _APIs &  Services_ and select _Enable APIs & services_.

:::{image} _images/APIs_Services_Client_ID.png
:alt: APIs and Services
:width: 800px
:::

Select _Enable APIs & services_ and search for "Google Drive API" in the search box of the API library.

:::{image} _images/Enable_APIs_Client_ID.png
:alt: Enable APIs
:width: 800px
:::

The results will show three with the Google Drive icon. Select the result called _Google Drive API_ and enable it. The other two are optional but not necessary.

:::{image} _images/Search_Google_API.png
:alt: API Library Google Drive
:width: 800px
:::

Afterward, go to _OAuth consent screen_.

:::{image} _images/Consent_Screen_Client_ID.png
:alt: Consent Screen OAuth Client ID
:width: 800px
:::

Choose _External_ and select _Create_. Fill in the required information by using your own gmail address and select _Save and Continue_.

:::{image} _images/App_Information_Client_ID.png
:alt: App Information OAuth Client ID
:width: 800px
:::

Select _Add or Remove Scopes_ in the next step. Search for "Google Drive API" and enable the scope ".../auth/drive". The other scopes are optional but not necessary. Select _Update_ to confirm and _Save and Continue_ to move to the next step.

:::{image} _images/App_Information_Client_ID.png
:alt: List of Scopes OAuth Client ID
:width: 800px
:::

Add the email addresses for your gmail accounts after selecting _Add Users_.

:::{image} _images/Test_Users_Client_ID.png
:alt: Test Users OAuth Client ID
:width: 800px
:::

Confirm by selecting _Save and Continue_. Check the overview and choose _Back to Dashbord_ or go to _Credentials_ directly.

:::{image} _images/Client_ID_Credentials.png
:alt: OAuth Client ID Credentials
:width: 800px
:::

Select _Desktop app_ as application type, name the credential, and select _Create_ to confirm.

:::{image} _images/Application_Type_Client_ID.png
:alt: Application Type for Credentials
:width: 800px
:::

The Credentials will be created and displayed automatically. Make sure save the credentials in a save place as you need them to set up the custom connection profile in the next step.

:::{image} _images/OAuth_Client_ID_Credentials.png
:alt: OAuth Client ID Credentials
:width: 400px
:::

## Add Custom Connection Profile

Edit the sample profile and save it into the _Profiles_ folder of the application support folder.

- {download}`Google Drive Custom OAuth Client ID.cyberduckprofile<_static/Google Drive Custom OAuth Client ID.cyberduckprofile>`

Use the OAuth credentials to edit the following sections of the sample profile:

:::{image} _images/Edit_Custom_Client_ID_Profile.png
:alt: Edit Google OAuth Client ID
:width: 600px
:::

The saved profile will be available in the _Protocol_ section of the bookmark configuration. 