FTP & FTP-TLS
===

```{image} _images/ftp.png
:alt: Send Command
:width: 128px
```

# FTP Connect Mode

Choose between an [Active (PORT) or Passive (PASV) connect mode](http://en.wikipedia.org/wiki/File_Transfer_Protocol#Connection_methods) per [bookmark](../Cyberduck/Bookmarks.md) or when opening a [new connection](../Cyberduck/Connection.md#toolbar-button). The default setting can be set in the System Preferences in *Network → Advanced... → Proxies → Use Passive FTP Mode (PASV)*.

# Character Encoding

The character encoding used to parse directory listings can be set as a per bookmark setting. If special characters such as Umlaute aren't displayed correctly in the browser, try to change the character encoding used. To change the character encoding for the current browser, use *View → Text Encoding*. The setting is also available per [bookmark](../Cyberduck/Bookmarks.md). Try `UTF-8` (the default), `ISO-8859-1` and `Windows-1252`.

# TLS Connections (FTPS)

FTP with [explicit](http://en.wikipedia.org/wiki/FTPS.md#explicit) TLS is supported. Implicit FTPS with no negotiation is deprecated and not supported. FTPS should not be confused with the [SSH File Transfer Protocol (SFTP)](SFTP.md).

## Mutual TLS

Mutual (two-way) TLS with a client certificate for authentication is supported. When a server requests a client certificate for authentication, a prompt is displayed to choose a certificate with a private key that matches the given issuer name requested from the server. Matching certificates are searched for in the Keychain on macOS or the Windows Certificate Manager respectively.

![Windows Security Prompt](_images/Windows-Security-Prompt.png)

## Switch to Secure Connection

If you attempt to connect to a server using FTP without TLS transport security but the server advertises support for TLS (as a response to `FEAT`), a prompt is displayed to secure the connection.

![Unsecured Connection](_images/Unsecured_connection.png)

You can always switch back to FTP without TLS transport security by changing the protocol selection in the bookmark to *FTP (File Transfer Protocol)*.

## Trust Certificate

If the certificate is not trusted by the system, you are asked to make an exception if you still want to connect to the site that cannot be verified. This failure during certificate trust verification is most often the case when the certificate is invalid either

- Because the hostname does not match the common name in the certificate. You will get the error message `You might be connecting to a server that is pretending to be…`.
- The certificate is self signed or signed by a root authority not trusted in the system.
- The certificate is expired.

You can temporarily or permanently allow to connect nevertheless by choosing *Continue*. To remember your choice, select *Always Trust…*.

# Distribution (CDN)

You can enable custom origin [Amazon CloudFront (Content Delivery Network) distribution](../CDN/CloudFront.md) using *File → Info → Distribution (CDN)*.

# Remote Commands

Use *Go → Send Command...* to open a command input window for the current browser.

Connected to a FTP server this allows to send arbitrary command not available through the user interface of the browser. Possibly these are extensions to the standard FTP protocol your server may support you can invoke with the `SITE` prefix. Type `SITE HELP` for supported commands.

# Server Compatibility

## ProFTPd

- You need to have the option set `TLSOptions NoSessionReuseRequired` for FTP-TLS connections (Issue [#5087](https://trac.cyberduck.io/ticket/5087)). If configuring the server is not an option, users should switch back to plain FTP connections. Choose *FTP (File Transfer Protocol)* in the bookmark protocol setting. Most users hit by this compatibility issue have been asked to secure the connection because support for TLS was detected upon negogiating the connection.

Example configuration:

	TLSOptions

      The NoSessionReuseRequired option has been added.  As of
      ProFTPD 1.3.3rc1, mod_tls only accepts SSL/TLS data connections
      that reuse the SSL session of the control connection, as a security
      measure.  Unfortunately, there are some clients (e.g. curl) which
      do not reuse SSL sessions.

      To relax the requirement that the SSL session from the control
      connection be reused for data connections, use the following in the
      proftpd.conf:

        <IfModule mod_tls.c>
          ...
          TLSOptions NoSessionReuseRequired
          ...
        </IfModule>

- The option `TLSOptions AllowClientRenegotiations` must be set for FTP-TLS connections (Issue [#3012](https://trac.cyberduck.io/ticket/3012)).
- The option `TLSProtocol SSLv23` must be set for FTP-TLS connections (Issue [#5061](https://trac.cyberduck.io/ticket/5061)).

## vsFTPd

- The option `require_ssl_reuse=NO` must be set for FTP-TLS connections (Issue [#5087](https://trac.cyberduck.io/ticket/5087)).

# Preferences

## Connection → Text Encoding

The text encoding selected is used to decode the filenames in a directory listing sent by the server. It is important this matches the text encoding used by the server to encode the characters as otherwise characters not in the ASCII range (such as German Umlaute) are not displayed correctly. `UTF-8` (the default), `ISO-8859-1` and `Windows-1252` are the most common. You can also change the text encoding per browser using *View → Text Encoding*.

## Default Protocol Handler

You can set Cyberduck or a third party application as the default application (protocol handler) for `FTP` in *Preferences → FTP*. When you click URLs in another application like your web browser, this application is opened to open the URL instead.

### Reset Windows FTP Protocol Registration

This has been fixed in Cyberduck 7.3.0. Cyberduck has overwritten the default Windows FTP protocol integration through Internet Explorer. This effectively disabled the Windows "Add Network location" for FTP-protocol. To reset this back to default you have to run following Registry-file which will reset the FTP-protocol registration back to default.

- {download}`ftp-default.reg<../_static/Ressources/ftp-default.reg>` | This has been tested for Windows 10 1909 only. This may or may not work for previous versions of Windows.

Applying Registry-files is not riskless and should be avoided if not necessary. Alternatively, you may apply following sequence to get the FTP-protocol handler definitions for your operating system version:

1. Create a Virtual Machine for your platform
2. Open RegEdit, navigate to *HKCR\ftp*
3. Open the context menu for the *ftp*-key, select *Export*
4. Import previously exported Registry-file on your PC
5. Delete the Virtual Machine

# Known Issues

## Maximum Number of Connections

Many servers limit the number of allowed connections with an error message like `530 Sorry, the maximum number of clients (10) from your host are already connected.`. Because FTP is a stateful protocol it requires opening separate connections when transferring files in parallel. Refer to [limit the number of connections](../Cyberduck/Transfer.md#connections) allowed for the file transfers.

## Error Opening Data Socket

For data transfers and possibly file listings (depending on the features supported by the server), a second data connection must be opened using `PASV` or `PORT` commands which is referred to as a passive or active data connection.

Depending on the firewall and router configuration in your network there may be errors reported:

- Failure opening active data socket reports `I won't open a connection to xxx.xxx.xx.xx (only to xxx.xx.xxx.x)`

## It is not Possible to Change Permissions

The error message `FTP Error: SITE not understood` or similar is displayed. The server does not support this feature (which is an optional extension to the FTP protocol) and can not be used.

## Listing Directory Fails or Shows no Content

Various options are available to adjust the usage of different directory listing commands (`LIST`, `STAT` and `MLSD`). Directory listings are requested using `STAT`, `MLSD`, `LIST -a` and `LIST` commands in that order. If a failure is detected (because the server may not support the command), the next option is tried. Because this can be fuzzy logic, it may still be that Cyberduck does not correctly fall back to a supported list command. You may then try to force the use of a given command.

To disable `STAT` for directory listings, change the [hidden configuration option](../Cyberduck/Preferences.md#hidden-configuration-options) as follows:

	defaults write ch.sudo.cyberduck ftp.command.stat false

To disable `LIST -a` for directory listings, open a Terminal.app window and enter

	defaults write ch.sudo.cyberduck ftp.command.lista false

To disable `MLSD` for directory listings, open a Terminal.app window and enter

	defaults write ch.sudo.cyberduck ftp.command.mlsd false

Restart Cyberduck.

## File Locks with vsFTPd

Set the property `lock_upload_files=NO` in *vsftpd_conf*.