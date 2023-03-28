SFTP To Go
====

> [SFTP To Go](https://sftptogo.com/) is a managed secure cloud storage that allows direct access to files using the SFTP, FTPS and S3 protocols.

## Connecting

### SFTP

SFTP To Go allows both password and public-key authentication. 

To connect using username and password, login to SFTP To Go's dashboard and go to the credentials page:

1. Expand the credentials you'd like to use to connect to copy the hostname, username and password.
2. Create a new [bookmark](../cyberduck/bookmarks.md) and enter the following information:

- Protocol: `SFTP (SSH File Transfer Protocol)`
- Server: `Hostname copied from SFTP To Go's dashboard`
- Username: `Username copied from SFTP To Go's dashboard`
- Password: `Password copied from SFTP To Go's dashboard`

To connect using public key authentication, login to SFTP To Go's dashboard and go to the credentials page:

1. Expand the credentials you'd like to use to connect in order to copy the hostname and username.
2. Create a new [bookmark](../cyberduck/bookmarks.md) and enter the following information:

- Protocol: `SFTP (SSH File Transfer Protocol)`
- Server: `Hostname copied from SFTP To Go's dashboard`
- Username: `Username copied from SFTP To Go's dashboard`
- SSH Private key: `path to private key that matches the public key imported in SFTP To Go`

#### FTPS

Login to SFTP To Go's dashboard and go to the credentials page:

1. Expand the credentials you'd like to use to connect in order to copy the hostname, username and password.
2. Create a new [bookmark](../cyberduck/bookmarks.md) and enter the following information:

- Protocol: `FTP-SSL (Explicit AUTH TLS)`
- Server: `Hostname copied from SFTP To Go's dashboard`
- Username: `Username copied from SFTP To Go's dashboard`
- Password: `Password copied from SFTP To Go's dashboard`

#### S3

Login to SFTP To Go's dashboard and go to the credentials page:

1. Expand the root credentials to copy the S3 endpoint and secrets.

Enter the following information in the [bookmark](../cyberduck/bookmarks.md):

- Protocol: `Amazon S3`
- Server: Copy the bucket from SFTP To Go' dashboard and use them in the following pattern: `<bucket>.s3.amazonaws.com`
- Access Key ID: `Access key ID copied from SFTP To Go's dashboard`
- Secret Access Key: `Secret access key copied from SFTP To Go's dashboard`
- Path: `Bucket name copied from SFTP To Go's dashboard`

## References

- [Connecting via SFTP](https://sftptogo.com/docs/how-to-connect/connect-using-sftp)
- [Connecting via FTPS](https://sftptogo.com/docs/how-to-connect/connect-using-ftps)
- [Connecting via Amazon S3](https://sftptogo.com/docs/how-to-connect/connect-using-amazon-s3)


