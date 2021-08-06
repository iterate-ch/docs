Custom Commands
===

Use *Go → Send Command...* to open a command input window for the current browser.

# FTP server

Connected to a FTP server this allows to send arbitrary command not available through the user interface of the browser. Possibly these are extensions to the standard FTP protocol your server may support you can invoke with the `SITE` prefix. Type `SITE HELP` for supported commands.

# SSH server

You can send any remote command to a remote SSH server. This is for example useful if you want a HTTP server to reload its configuration or changing the ownership of files using chown on a `UNIX` system.

```{note}

The current working directory is always your use home. Determine using `pwd` to get the absolute path.
```

```{image} _images/command.png
:alt: Send Command
:width: 700px
```