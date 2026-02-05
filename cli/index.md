Command Line Interface (CLI)
====

:::{toctree}
:hidden:
:titlesonly:
support
../tutorials/cli_github_action
:::

[Cyberduck with a command-line interface (CLI)](https://duck.sh/) is available for Mac, Windows & Linux. It is installed
as `duck`.

:::{contents} Content
:depth: 2
:local:
:::

## Installation

:::::{tabs}
::::{group-tab} macOS

**Homebrew**

Available as a [Homebrew](http://brew.sh/) package. Use

```
brew install duck
```

to install.

**MacPorts**

The port is maintained by a third party. Use

```
sudo port install duck
```

to install.

**Snapshot Builds**

```
brew install iterate-ch/cyberduck/duck
```

**Package**

[Download](https://dist.duck.sh) the latest installer package.

::::
::::{group-tab} Windows

**Chocolatey**

Available as a [Chocolatey](https://chocolatey.org) package. Use

```
choco install duck
```

to install.

**MSI Installer**

[Download](https://dist.duck.sh) the latest setup.

**Snapshot Builds**

Not currently available.

:::{image} _images/CLI_Setup.png
:alt: CLI Setup
:width: 500px
:::

::::
:::::{group-tab} Linux

**RPM Package Repository**

To add the `duck` repository to your system you need to put a file `duck.repo` with the following content into
`/etc/yum.repos.d/`.

**Snapshot Builds**

Copy and paste

```
echo -e "[duck-nightly]\n\
name=duck-nightly\n\
baseurl=https://repo.cyberduck.io/nightly/\$basearch/\n\
enabled=1\n\
gpgcheck=0" | sudo tee /etc/yum.repos.d/duck-snapshot.repo > /dev/null
```

to add the configuration.

**Stable Builds**

```
echo -e "[duck-stable]\n\
name=duck-stable\n\
baseurl=https://repo.cyberduck.io/stable/\$basearch/\n\
enabled=1\n\
gpgcheck=0" | sudo tee /etc/yum.repos.d/duck-stable.repo > /dev/null
```

To install *Cyberduck CLI* use
`sudo yum install duck`

**DEB Package Repository**

1. Add the nightly or stable `duck` repository to your `/etc/apt/sources.list` manually:
    ```
    deb https://s3.amazonaws.com/repo.deb.cyberduck.io nightly main
    deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main
    ```
   or using
    ```
    echo -e "deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main" | sudo tee /etc/apt/sources.list.d/cyberduck.list > /dev/null
    ```
2. You need to download the GPG public key from `keyserver.ubuntu.com` to verify the integrity of the packages:
    ```
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FE7097963FEFBE72
    ```
3. Synchronize the repository using
    ```
    sudo apt-get update
    ```
4. To install or upgrade *Cyberduck CLI* use
    ```
    sudo apt-get install duck
    ```

:::{warning}
You may get a conflict with another package named `duck`. As a workaround, install with a specific version number like
`sudo apt-get install duck=6.7.1.28683`.
:::

**Arch Linux Package**

- [Package Details](https://aur.archlinux.org/packages/duck/). *Note*: This is maintained by a third party.

**Manual Installation**

Packages can also be found for [download](https://dist.duck.sh/).

::::
:::::

### Docker Image

_Cyberduck CLI_ is available as a [Docker Image](https://github.com/iterate-ch/cyberduck/pkgs/container/cyberduck). Install from the command line with

    docker pull ghcr.io/iterate-ch/cyberduck:latest

### GitHub Action

_[Cyberduck CLI GitHub Action](https://github.com/iterate-ch/cyberduck-cli-action)_ is available for [GitHub Actions](https://github.com/features/actions). It runs Cyberduck CLI within a docker container. 

    uses: iterate-ch/cyberduck-cli-action@v1
    env:
        USERNAME: <username>
        PASSWORD: <password>
        IDENTITY: <identity file>
    with:
        mode: list|longlist|upload|download|delete|purge|raw
        url: <remote file or directory>
        path: <local file or directory>
        args: '<additional parameters>'

:::{admonition} Tutorial
:class: tip

Follow the [step-by-step instructions](../tutorials/cli_github_action.md) to use the Cyberduck CLI GitHub Action.
:::

## Usage

`Usage:duck [options...]`

Run `--help` to get the option screen.

URLs in arguments must be fully qualified. You can reference files relative to your home directory with
`/~ftps://user@example.net/~/`.

:::{attention}
Paths can either denote a remote file `ftps://user@example.net/resource` or folder `ftps://user@example.net/directory/` with a trailing `/`.
:::

### Connection Profiles

You can install additional [connection profiles](../protocols/profiles/index.md) in
the [application support directory](#profiles). Use the `--profile` option to reference
a [connection profile](../protocols/index.md#connection-profiles) file to use not installed in the standard location.

:::{tip}
Install connection profiles in [Cyberduck](../cyberduck/index.md) from _Preferences → Profiles_
:::

### URI

The `<url>` argument for `--copy`, `--download`, `--upload`, and `--synchronize` must satisfy following rules:

- Each URL must start with a scheme and a colon (`https:`) unless you specify a `--profile`.
- Depending on the type of protocol you are referencing different rules apply
    - For all protocols where no default hostname is set (e.g. `WebDAV`, `SFTP`, and `FTPS`) you must use a fully
      qualified URI: `https://user@hostname/path` or `sftp://user:password@hostname/path`
    - For all protocols where a default hostname is set, but you are allowed to change it (e.g. S3) you may use fully
      qualified URIs or
      *Absolute paths:* `s3:/bucket/path`,
      *Relative paths:* `s3:user@path` or `s3:user@/path`.
      :::{note}
      Omitting the first slash in a relative path uses the default home directory for this protocol.
      :::
    - For all protocols where a default hostname is set and you are not allowed to change it (e.g. `OneDrive`,
      `Dropbox`, `Google Drive`) you may use any combination of the above with the following rules: Fully Qualified URIs
      are parsed as relative paths. `onedrive://Some/Folder/` is parsed as `onedrive:Some/Folder`.
- For all protocols where a default path is set and you are not allowed to change it (e.g. accessing a prebuilt
  `NextCloud` profile with a path set to `/remote.php/webdav`). You are allowed to change the path but it will be
  appended to the default path. Making nextcloud:/path really `nextcloud:/remote.php/webdav/path`.

:::{tip}
Spaces and other special-characters are not required to be percent-encoded (e.g. `%20` for space) as long as the path is
quoted `duck --upload "scheme://hostname/path with/spaces" "/Path/To/Local/File With/Spaces"`.
:::

| Protocol                                             | Fully Qualified URI required                       | Absolute Path                                           | Relative Path                                          |
|------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| [FTP](../protocols/ftp.md) (File Transfer Protocol)  | Yes (`ftp://<hostname>/<path>`)                    |                                                         |                                                        |
| [FTPS](../protocols/ftp.md) (Explicit Auth TSL)      | Yes (`ftps://<hostname>/<path>`)                   |                                                         |                                                        |
| [SFTP](../protocols/sftp/index.md)                   | Yes (`sftp://<hostname>/<path>`)                   |                                                         |                                                        |
| [WebDAV](../protocols/webdav/index.md) (HTTP)        | Yes (`dav://<hostname>/<path>`)                    |                                                         |                                                        |
| [WebDAV](../protocols/webdav/index.md) (HTTPS)       | Yes (`davs://<hostname>/<path>`)                   |                                                         |                                                        |
| [SMB](../protocols/smb.md)                           | Yes (`smb://<hostname>/<path>`)                    |                                                         |                                                        |
| Local Disk                                           | No                                                 | `file:/<path>`                                          | `file:<path>`                                          |
|                                                      |
| [Nextcloud](../protocols/webdav/nextcloud.md)        | Yes (`nextcloud://<hostname>/<path>`)              |                                                         |                                                        |
| [ownCloud](../protocols/webdav/nextcloud.md)         | Yes (`owncloud://<hostname>/<path>`)               |                                                         |                                                        |
| [Amazon S3](../protocols/s3/index.md)                | `s3://<hostname>/<container>/<key>`                | `s3:/<container>/<key>` <br/>(using `s3.amazonaws.com`) | `s3:<container>/<key>` <br/>(using `s3.amazonaws.com`) |
| [Google Storage](../protocols/googlecloudstorage.md) | No                                                 | `gs:/<path>`                                            | `gs:<path>`                                            |
| [OpenStack Swift](../protocols/openstack/index.md)   | Yes (`swift://<hostname>/<container>/<key>`)       |                                                         |                                                        |
| [Azure Blob Storage](../protocols/azure.md)          | No                                                 | `azure:/<container>/<key>`                              | `azure:<container>/<key>`                              |
| [Backblaze B2](../protocols/b2.md)                   | No                                                 | `b2:/<container>/<key>`                                 | `b2:<container>/<key>`                                 |
|                                                      |
| [Microsoft OneDrive](../protocols/onedrive.md)       | No                                                 | `onedrive:/<path>`                                      | `onedrive:<path>`                                      |
| [Microsoft Sharepoint](../protocols/sharepoint.md)   | No                                                 | `sharepoint:/<path>`                                    | `sharepoint:<path>`                                    |
| [Dropbox](../protocols/dropbox.md)                   | No                                                 | `dropbox:/<path>`                                       | `dropbox:<path>`                                       |
| [Google Drive](../protocols/googledrive.md)          | No                                                 | `googledrive:/<path>`                                   | `googledrive:<path>`                                   |
| [Box](../protocols/box.md)                           | No                                                 | `box:/<path>`                                           | `box:<path>`                                           |
|                                                      |
| [DRACOON](../protocols/dracoon.md)                   | Yes (`dracoon://<hostname>/<path>`)                |                                                         |                                                        |
| Spectra S3 (HTTPS)                                   | Yes<br/>(`spectra://<hostname>/<container>/<key>`) |                                                         |                                                        |
| Rackspace Cloud Files (US)                           | No                                                 | `rackspace:/<container>/<key>`                          | `rackspace:<container>/<key>`                          |

#### Examples

:::{admonition} Home Directory
:class: tip

You can use the `~` character to abbreviate the remote path pointing to the home folder on the server as in
`duck --list sftp://duck.sh/~/`.
:::

- List all buckets in S3 with

```
duck --username <Access Key ID> --list s3:/
```

- List all objects in a S3 bucket with

```
duck --username <Access Key ID> --list s3:/<bucketname>/
```

- List a vault on OneDrive without using the `--vault` option

```
duck --list "onedrive:/My Files/<vault name>/"
```

- Download a single file from a vault on OneDrive

```
duck --download "onedrive:/My Files/<vault name>/<file name>" ~/Downloads/ --vault "/My Files/<vault name>/"
```

### Generic Options

#### `--retry`

Retry requests with I/O failures once per default. Useful on connection timeout or latency issues.

#### `--verbose`

Print protocol transcript for requests and responses. This includes the HTTP headers.

#### `--nokeychain`

Do not save passwords in login keychain (macOS), credentials manager (Windows), or plain text password file (Linux).

#### `--quiet`

Suppress progress messages.

#### `--throttle`

Throttle bandwidth to the number of bytes per second.

### Credentials

You can pass username and password as part of the URI prepending to the hostname with `username:password@host`.
Alternatively, use the `--username` option. You can give the password with the `--password` option or you will be
prompted before the connection is opened by the program if no password matching the host is found in your login
keychain (OS X) or user configuration shared with Cyberduck (Windows).

:::{tip}
Use the `--nokeychain` option to disable saving credentials.
:::

:::{warning}
On Linux, credentials are stored in plain text in the [application support directory](support.md#application-support-directory).
:::

#### Private Key

When connecting with SFTP you can give a file path to a private key with `--identity` for use with public key
authentication.

#### Tenant Name

When connecting with `OpenStack Swift` you can set the tenant name (*OpenStack Identity Service, Keystone 2.0*) or
project (*OpenStack Identity Service, Keystone 3.0*) with `--username <tenant>:<user>`.

### Downloads with `--download`

- Download file `<file>` to directory `<folder>` on disk using

```
duck --download protocol:/<file> <folder>/
```

- Download file `<file>` as `<name>` to directory `<folder>` on disk using

```
duck --download protocol:/<file> <folder>/<name>
```

#### Glob Pattern Support for Selecting Files to Transfer

You can transfer multiple files with a single command using a glob pattern for filename inclusion such as

```
duck --download protocol://<hostname>/directory/*.css
```

### Uploads with `--upload`

Note the inclusion or absence of a trailing `/` delimiter character to denote a file or directory on the server.

- Upload the `<folder>` on disk to remote directory `<name>/` using

```
duck --upload protocol:/<name>/ <folder>/
```

- Upload file `<file>` to remote directory `<folder>` using

```
duck --upload protocol:/<folder>/ <file>
```

- Upload file `<file>` as `<name>` to remote directory `<folder>` using

```
duck --upload protocol:/<folder>/<name> <file>
```

#### Glob Pattern Support for Selecting Files to Transfer

If your shell supports glob expansion you can use a wildcard pattern to select files for upload like

```
duck --upload protocol://<hostname>/directory/ ~/*.jpg
```

### Synchronize Folders with `--synchronize`

- Synchronize directory `<name>` with directory `folder` on disk using

```
duck --synchronize protocol:/<name>/ folder/
```

#### Custom Configuration Options for Uploads to S3

Add default metadata for uploads using the [preferences option to read from the environment](#preferences). The property
is documented in [Default metadata](../protocols/s3/index.md#default-metadata).

```
env "s3.metadata.default=Content-Type=application/xml" duck --upload …
```

Set a default ACL for the upload with

```
env "s3.acl.default=public-read" duck --upload …
```

### Remote Directory Listing with `--list`

Make sure to include a trailing `/` in the path argument to denote a directory. Use the `-L` option to print permission
mask and modification date in addition to the filename.

### Edit with `--edit`

You can edit remote files with your preferred editor on your local system using the `--edit` command. Use the optional
`--application` option to specify the absolute path to the external editor you want to use.

### Purge Files in CDN with `--purge`

Purge files in CloudFront or Akamai CDN for Amazon S3 or Rackspace CloudFiles connections. For example to invalidate all
contents in a bucket run

```
duck --username AKIAIWQ7UM47TA3ONE7Q --purge s3:/github-cyberduck-docs/
```

### Multiple Transfer Connections with `--parallel`

Transfer files with multiple concurrent connections to a server.

### Rename or move files using `--move`

You can move or rename remote files using the `--move` command. Use an absolute path for the target filename.

```{code-block}
duck  --move protocol:/<folder>/<name> <file>
```

### Copy files using `--copy`

You can copy files using the `--copy` command. Use an absolute path for the target filename. Server-side [copy support](../cyberduck/copy.md#copy-files-and-folders-between-servers) is limited to some protocols.

```{code-block}
duck  --copy protocol:/<folder>/<name> <file>
```

### Cryptomator

Access to your [Cryptomator](../cryptomator/index.md) Vaults from the command line. When accessing a vault using
`--download`, `--list` or `--upload`, you will be prompted to provide the passphrase for the Vault if not found in the
Keychain.

Use `--vault <path>` in conjunction with `--upload` to unlock a Vault. This allows uploading into a subdirectory of a
Vault where the auto-detect feature does otherwise not work.

## Samples

### Watching Changes in Directory with `fswatch` and Upload

`fswatch` is a file change monitor; an application to watch for file system changes. Refer to
their [documentation](https://github.com/emcrisostomo/fswatch/wiki).

```
fswatch -0 ~/Sites/mywebsite/ | xargs -0 -I {} -t sh -c 'f="{}"; duck --upload ftps://<hostname>/sandbox`basename "${f}"` "${f}" -existing overwrite'
```

### Upload Build Artifacts from Continuous Integration (Jenkins) to CDN

use a post [build script action](https://plugins.jenkins.io/postbuildscript/).

```
cd ${WORKSPACE}; find build -name '*.tar' -print0 | xargs -0 -I {} -t sh -c 'f="{}"; duck --quiet --retry --existing skip --region DFW --upload rackspace://<container>/ "${f}"'
```

### Upload Files Matching Glob Pattern to Windows Azure

```
duck --username kahy9boj3eix --upload azure://kahy9boj3eix.blob.core.windows.net/<containername>/ *.zip
```

### Download Files Matching Glob Pattern from S3

```
duck --user anonymous --verbose --download s3:/profiles.cyberduck.io/Wasabi* ~/Downloads/
```

### Download File from Amazon S3 Public Bucket

```
duck --user anonymous --download s3:/repo.maven.cyberduck.io/releases/ch/cyberduck/s3/6.1.0/s3-6.1.0.jar ~/Downloads/
```

## Application Support Directory

### Profiles

The directory location is printed with `--help` following the list of supported protocols.

::::{tabs}
:::{group-tab} macOS

The support directory is `~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/` on Mac. You can
install third party [profiles](../protocols/profiles/index.md) in
`~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/duck/Profiles`.

:::
:::{group-tab} Windows

Install additional profiles in `%AppData%\Cyberduck\Profiles` on Windows.

:::
:::{group-tab} Linux

The support directory is `~/.duck/` on Linux. You can install third party [profiles](../protocols/profiles/index.md) in
`~/.duck/profiles/`.

:::
::::

## Preferences

::::{tabs}
:::{group-tab} macOS

You can override default [preferences](../cyberduck/preferences.md#hidden-configuration-options) by setting environment
variables in your shell.

`env "<property>=<value>" duck`

:::
:::{group-tab} Windows

You can override default [preferences](../cyberduck/preferences.md#hidden-configuration-options) by setting environment
variables in your shell.

`set "<property>=<value>" & duck`

:::
:::{group-tab} Linux

You can override default [preferences](../cyberduck/preferences.md#hidden-configuration-options) by setting environment
variables in your shell.

`env "<property>=<value>" duck`

:::
::::

## Known Issues

### Slow Execution due to low Entropy in /dev/random

As a workaround run `haveged`, a service to generate random numbers and feed Linux random device.

## Third-Party References

- [Using Cyberduck and duck CLI to access Oracle Cloud Infrastructure Classic Storage](https://medium.com/oracledevs/using-cyberduck-and-duck-cli-to-access-oracle-cloud-infrastructure-classic-storage-edfeb04c82c4)
