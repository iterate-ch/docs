Command Line Interface (CLI)
===

[Cyberduck with a command-line interface (CLI)](https://duck.sh/) is available for Mac, Windows & Linux. It is installed as `duck`.

# Installation

`````{tabs}
````{group-tab} macOS

**Homebrew**<br/>
Available as a [Homebrew](http://brew.sh/) package. Use
`brew install duck`
to install.


**MacPorts**<br/>
```{note}

The port is maintained by a third party. Use
`sudo port install duck`
to install.
```


**Snapshot Builds**<br/>
`brew install iterate-ch/cyberduck/duck`


**Package**<br/>
[Download](https://dist.duck.sh) the latest installer package.

````
````{group-tab} Windows

**Chocolatey**<br/>
Available as a [Chocolatey](https://chocolatey.org) package. Use
`choco install duck`
to install.


**MSI Installer**<br/>
[Download](https://dist.duck.sh) the latest setup.


**Snapshot Builds**<br/>
Not currently available.

```{image} _images/CLI_Setup.png
:alt: Send Command
:width: 500px
```

````
````{group-tab} Linux

**RPM Package Repository**<br/>
To add the `duck` repository to your system you need to put a file `duck.repo` with the following content into `/etc/yum.repos.d/`.

**Snapshot Builds**<br/>
Copy and paste

```{code-block}
echo -e "[duck-nightly]\n\
name=duck-nightly\n\
baseurl=https://repo.cyberduck.io/nightly/\$basearch/\n\
enabled=1\n\
gpgcheck=0" | sudo tee /etc/yum.repos.d/duck-snapshot.repo > /dev/null
```

to add the configuration.

**Stable Builds**<br/>
```{code-block}
echo -e "[duck-stable]\n\
name=duck-stable\n\
baseurl=https://repo.cyberduck.io/stable/\$basearch/\n\
enabled=1\n\
gpgcheck=0" | sudo tee /etc/yum.repos.d/duck-stable.repo > /dev/null
```

To install *Cyberduck CLI* use 
`sudo yum install duck`

**DEB Package Repository**<br/>
Add the `duck` repositories to your `/etc/apt/sources.list` manually:

```{code-block}
deb https://s3.amazonaws.com/repo.deb.cyberduck.io nightly main
deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main
```

or using 
`echo -e "deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main" | sudo tee /etc/apt/sources.list.d/cyberduck.list > /dev/null`

You need to download the GPG public key from `keyserver.ubuntu.com` to verify the integrity of the packages:
`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FE7097963FEFBE72`

Synchronize the repository using 
`sudo apt-get update`

To install or upgrade *Cyberduck CLI* use
`sudo apt-get install duck`

```{note}
You may get a conflict with another package named `duck`. As a workaround, install with a specific version number like `sudo apt-get install duck=6.7.1.28683`.
```

**Arch Linux Package**

- [Package Details](https://aur.archlinux.org/packages/duck/)


**Manual installation**<br/>
Packages can also be found for [download](https://dist.duck.sh/).

````
`````

# Usage

`Usage:duck [options...]`

Run `--help` to get the option screen.

URLs in arguments must be fully qualified. Paths can either denote a remote file `ftps://user@example.net/resource` or folder `ftps://user@example.net/directory/` with a trailing slash. You can reference files relative to your home directory with `/~ftps://user@example.net/~/`.

## Connection Profiles

You can install additional connection profiles in the [application support directory](index#profiles). Use the `--profile` option to reference a [connection profile](../Protocols/index#connection-profiles) file to use not installed in the standard location.

## URI

The `<url>` argument for `--copy`, `--download`, `--upload`, and `--synchronize` must satisfy following rules:

- Each URL must start with a scheme and a colon (`https:`)(unless you specify a `--profile`)
- Depending on the type of protocol you are referencing different rules apply
	- For all protocols where no default hostname is set (e.g. `WebDAV`, `SFTP`, and `FTPS`) you must use a fully qualified URI `https://user@hostname/path`
	- For all protocols where a default hostname is set, but you are allowed to change it (e.g. S3) you may use fully qualified URIs or 
	*Absolute paths:* `s3:/bucket/path`,
	*Relative paths:* `s3:user@path` or `s3:user@/path`. 
	Omitting the first slash in a relative path uses the default home directory for this protocol.
	- For all protocols where a default hostname is set and you are not allowed to change it (e.g. `OneDrive`, `Dropbox`, `Google Drive`) you may use any combination of the above with the following rules: Fully Qualified URIs are parsed as relative paths. `onedrive://Some/Folder/` is parsed as `onedrive:Some/Folder`.
- For all protocols where a default path is set and you are not allowed to change it (e.g. accessing a prebuilt `NextCloud` profile with a path set to `/remote.php/webdav`). You are allowed to change the path but it will be appended to the default path. Making nextcloud:/path really `nextcloud:/remote.php/webdav/path`.

Spaces and other special-characters are not required to be percent-encoded (e.g. `%20` for space) as long as the path is quoted `duck --upload "scheme://hostname/path with/spaces" "/Path/To/Local/File With/Spaces"`).

| Protocol | Fully Qualified URI required | Absolute Path | Relative Path |
| --- | --- | --- | --- |
| Windows Azure Storage | No | `azure:/<container>/<key>` | `azure:<container>/<key>` |
| Backblaze B2 Cloud Storage | No | `b2:/<container>/<key>` | `b2:<container>/<key>` |
| WebDAV (HTTP) | Yes (`dav://<hostname>/<path>`) |||
| WebDAV (HTTPS) | Yes (`dav://<hostname>/<path>`) |||
| Dracoon (Email Address) | Yes (`dracoon://<hostname>/<path>`) |||
| Dropbox | No | `dropbox:/<path>` | `dropbox:<path>` |
| Local | No | `file:/<path>` | `file:<path>` |
| FTP (File Transfer Protocol) | Yes (`ftp://<hostname>/<path>`) |||
| FTPS (Explicit Auth TSL) | Yes (`ftps://<hostname>/<path>`) |||
| Google Drive | No | `googledrive:/<path>` | `googledrive:<path>` |
| Google Cloud Storage | No | `gs:/<path>` | `gs:<path>` |
| Microsoft OneDrive | No | `onedrive:/<path>` | `onedrive:<path>` |
| Amazon S3 | `s3://<hostname>/<container>/<key>` | `s3:/<container>/<key>` <br/>(using `s3.amazonaws.com`) | `s3:<container>/<key>` <br/>(using `s3.amazonaws.com`) |
| SFTP (SSH File Transfer <br/>Protocol) | Yes (`sftp://<hostname>/<path>`) |||
| Spectra S3 (HTTPS) | Yes<br/>(`spectra://<hostname>/<container>/<key>`) |||
| Rackspace Cloud Files (US) | No | `rackspace:/<container>/<key>` | `rackspace:<container>/<key>` |
| Swift (OpenStack Object<br/>Storage) | Yes (`swift://<hostname>/<container>/<key>`) |||

### Examples

- List all buckets in S3 with 
`duck --username <Access Key ID> --list s3:/`
- List all objects in a S3 bucket with
`duck --username <Access Key ID> --list s3:/<bucketname>/`

## Generic options

### `--retry`

Retry requests with I/O failures once per default. Useful on connnection timeout or latency issues.

### `--verbose`

Print protocol transcript for requests and responses. This includes the HTTP headers.

### `--nokeychain`

Do not save passwords in login keychain (macOS), credentials manager (Windows), or plain text password file (Linux).

### `--quiet`

Suppress progress messages.

### `--throttle`

Throttle bandwidth to the number of bytes per second.

## Credentials

You can pass username as part of the URI prepending to the hostname with `username@host`. Alternatively use the `--username` option. You can give the password with the `--password` option or you will be prompted before the connection is opened by the program if no password matching the host is found in your login keychain (OS X) or user configuration shared with Cyberduck (Windows).

### Private Key

When connecting with SFTP you can give a file path to a private key with `--identity` for use with public key authentication.

### Tenant Name

When connecting with `OpenStack Swift` you can set the tenant name (*OpenStack Identity Service, Keystone 2.0*) or project (*OpenStack Identity Service, Keystone 3.0*) with `--username <tenant>:<user>`.

## Downloads with `--download`

### Glob pattern support for selecting files to transfer

You can transfer multiple files with a single command using a glob pattern for filename inclusion such as `duck --download ftps://<hostname>/directory/*.css`.

## Uploads with `--upload`

### Glob pattern support for selecting files to transfer

If your shell supports glob expansion you can use a wildcard pattern to select files for upload like `duck --upload ftps://<hostname>/directory/ ~/*.jpg`.

### Use of `~`

You can use the tilde to abbreviate the remote path pointing to the remote home folder as in `sftp://duck.sh/~/`. It will be expanded when constructing absolute paths.

## Remote directory listing with `--list`

Make sure to include a trailing '/' in the path argument to denote a directory. Use the `-L` option to print permission mask and modification date in addition to the filename.

## Edit with `--edit`

You can edit remote files with your preferred editor on your local system using the `--edit` command. Use the optional `--application` option to specify the absolute path to the external editor you want to use.

## Purge files in CDN with `--purge`

Purge files in CloudFront or Akamai CDN for Amazon S3 or Rackspace CloudFiles connections. For example to invalidate all contents in a bucket run `duck --username AKIAIWQ7UM47TA3ONE7Q --purge s3:/github-cyberduck-docs/`

## Multiple transfer connections with `--parallel`

Transfer files with multiple concurrent connections to a server.

## Cryptomator

Access to your [Cryptomator](../Cryptomator/index) vaults from the command line. When accessing a vault using `--download`, `--list` or `--upload`, you will be prompted to provide the passphrase for the vault if not found in the keychain.

Use `--vault <path>` in conjunction with `--upload` to unlock a vault. This allows uploading into a subdirectory of a vault where the auto-detect feature does otherwise not work.

# Samples

## Watching changes in directory with `fswatch` and upload

`fswatch` is a file change monitor; an application to watch for file system changes. Refer to their [documentation](https://github.com/emcrisostomo/fswatch/wiki).

``fswatch -0 ~/Sites/mywebsite/ | xargs -0 -I {} -t sh -c 'f="{}"; duck --upload ftps://<hostname>/sandbox`basename "${f}"` "${f}" -existing overwrite'``

## Upload build artifacts from continuous integration (Jenkins) to CDN

use a post [build script action](https://plugins.jenkins.io/postbuildscript/).

`cd ${WORKSPACE}; find build -name '*.tar' -print0 | xargs -0 -I {} -t sh -c 'f="{}"; duck --quiet --retry --existing skip --region DFW --upload rackspace://<container>/ "${f}"'`

## Upload files matching glob pattern to Windows Azure

`duck --username kahy9boj3eix --upload azure://kahy9boj3eix.blob.core.windows.net/<containername>/ *.zip`

## Download files matching glob pattern from FTP

`duck -v --download ftp://mirror.switch.ch/mirror/apache/dist/httpd/*.gz ~/Downloads`

## Download file from Amazon S3 public bucket

`duck --verbose --download s3://repo.maven.cyberduck.io/releases/ch/cyberduck/s3/6.1.0/s3-6.1.0.jar ~/Downloads/`

# Application Support Directory

## Profiles

The directory location is printed with `--help` following the list of supported protocols.

`````{tabs}
````{group-tab} macOS

The support directory is `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` on Mac. You can install third party [profiles](../Cyberduck/Profiles) in `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Profiles`.

````
````{group-tab} Windows

Install additional profiles in `%AppData%\Cyberduck\Profiles` on Windows.

````
````{group-tab} Linux

The support directory is `~/.duck/` on Linux. You can install third party [profiles](../Cyberduck/Profiles) in `~/.duck/profiles/`.

````
`````

# Preferences

`````{tabs}
````{group-tab} macOS

You can override default [preferences](../Cyberduck/Preferences#hidden-configuration-options) by setting environment variables in your shell.

`env "property.name=value" duck`

````
````{group-tab} Windows

You can override default [preferences](../Cyberduck/Preferences#hidden-configuration-options) by setting environment variables in your shell.

`set "property.name=value" & duck`

````
````{group-tab} Linux

You can override default [preferences](../Cyberduck/Preferences#hidden-configuration-options) by setting environment variables in your shell.

`env "property.name=value" duck`

````
`````

# Known Issues

## Slow execution due to low entropy in /dev/random

As a workaround run `haveged`, a service to generate random numbers and feed Linux random device.

# Thirdparty References

- [Using Cyberduck and duck CLI to access Oracle Cloud Infrastructure Classic Storage](https://medium.com/oracledevs/using-cyberduck-and-duck-cli-to-access-oracle-cloud-infrastructure-classic-storage-edfeb04c82c4)