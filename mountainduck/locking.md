File Locking
====

Mountain Duck supports locking files to prevent conflicting edits from others while a document is open in an editor.

## Native Server-Side Locking

File locking is natively supported for the following protocols:

- [Dropbox for Business](../protocols/dropbox.md)
- [Microsoft OneDrive Business](../protocols/onedrive.md)
- [Microsoft SharePoint](../protocols/sharepoint.md)
- [WebDAV](../protocols/webdav/index.md)

:::{note}
Some WebDAV implementations may not support locking documents.
:::

Files opened from one of the supported protocols are locked for editing by other users. Mountain Duck locks files on the server when opened in an editor. This prevents other users from modifying the document until the file is closed by the user.

## Pseudo Locking for Protocols with no Native Lock Support Using Lock Owner Files

```{warning}
Not supported for _Integrated_ connect mode.
```

For connections other than [WebDAV](../protocols/webdav/index.md), we support detecting files opened by others by looking for owner lock files uploading to the server.

:::{note}
Support is currently limited to files edited in *Microsoft Word, Microsoft Excel, and Microsoft Powerpoint* on macOS and Windows.
:::

:::{attention}
*Excel 97-2003* files are not included because Excel doesn't create lock files for those file types: `*.xls`, `*.xlt`, `*.xla`.
:::

### References

When a previously saved file is opened for editing, for printing, or for review, Word creates a temporary file that has a .doc file name extension. This filename extension begins with a tilde (\~) that is followed by a dollar sign ($) that is followed by the remainder of the original file name. This temporary file holds the login name of the person who opens the file. This temporary file is called the "owner file".

- [Description of how Word creates temporary files](https://support.microsoft.com/en-us/help/211632/description-of-how-word-creates-temporary-files)
- [The document is locked for editing by another user error message when you try to open a document in Word](https://support.microsoft.com/en-us/help/313472/the-document-is-locked-for-editing-by-another-user-error-message-when)

## Error Message When Opening Locked Documents

Attempting to open a locked document, an error message is displayed notifying the document can only be opened in read-only mode. Samples of error messages from different applications.

:::::{tabs}
::::{group-tab} macOS

**Microsoft Word**<br/>
`Read Only. To save a copy of this document, click Duplicate`

:::{image} _images/Read_Only_Microsoft_Word_macOS.png
:alt: Read Only Microsoft Word (macOS)
:width: 500px
:::

**Libre Office**<br/>
`Document ... is locked for editing by... . Open document read-only or open a copy of the document for editing.`

:::{image} _images/Document_in_Use_Libre_Office_macOS.png
:alt: Document in Use Libre Office (macOS)
:width: 400px
:::

:::{image} _images/Read_Only_Mode_Libre_Office_macOS.png
:alt: Read Only Mode Libre Office (macOS)
:width: 400px
:::

::::
::::{group-tab} Windows

**Microsoft Word**<br/>
`This file is already opend by another user. Would you like to make a copy of this file for your use?`

:::{image} _images/File_in_Use_Microsoft_Word_Windows.png
:alt: File in Use Microsoft Word (Windows)
:width: 400px
:::

Choose *Receive notification when the original copy is available* to open the document in read-only mode and get an alert when the other user has closed the document.

:::{image} _images/Microsoft_Word_Read-Only_Edit_Windows.png
:alt: Read Only Edit Microsoft Word (Windows)
:width: 400px
:::

:::{image} _images/Microsoft_Word_File_Now_Available_Windows.png
:alt: File Now Available Microsoft Word (Windows)
:width: 400px
:::

**Microsoft Excel**<br/>
`File in Use: File is locked for editing by ... . Open 'Read-Only' or click 'Notify' to open read-only and receive notification when the document is no longer in use.`

:::{image} _images/Read_Only_Microsoft_Excel_Windows.png
:alt: Read Only Microsoft Excel (Windows)
:width: 400px
:::

Choose *Notify* to open the document in read-only mode and get an alert when the other user has closed the document.

:::{image} _images/Microsoft_Excel_File_Now_Available_Notification_Windows.png
:alt: File Now Available Notification Microsoft Excel
:width: 400px
:::

::::
:::::

## Resolution

If you get a warning that the document is *Read-Only*, ask other users to close the document. If the *Read-Only* warning prevails, these are the steps to follow.

- If you are connecting to a WebDAV server with lock support, ask the server administrator to clean up locks on the server.
- For all other servers, delete the file named `~$...`.

## Preferences

Locking is disabled by default. Refer to [Preferences](preferences.md) to enable it in *Sync → Locking → Lock Files*.

## Limitations

- Due to Dropbox file restrictions lock files are forbidden files and can't be uploaded. Therefore, pseudo file locking is not available using Dropbox.
- [NextCloud & ownCloud via WebDAV](../protocols/webdav/nextcloud.md) don't support locking documents. Make sure to select *Nextcloud & ownCloud* in the bookmark configuration to make use of pseudo locking.