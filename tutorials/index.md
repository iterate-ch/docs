Tutorials
====

:::{toctree}
:hidden:
:titlesonly:
hidden_properties
custom_oauth_client_id
s3_iam_role_mfa
iam
vault_localdisk
sftp_publickeyauth
sftp_publickeyauth_1password
sftp_publickeyauth_bitwarden
sftp_publickeyauth_yubikey
cli_github_action
:::

Find detailed step-by-step instructions for setup, connecting and most common use-cases as well as tutorials for more complicated workarounds.

## [Setup a Custom OAuth Client ID for Google Drive & Google Cloud Storage](custom_oauth_client_id.md)
Workaround to register your own Custom OAuth 2.0 Client ID for [Google Cloud Storage](../protocols/googlecloudstorage.md) and [Google Drive](../protocols/googledrive.md) and use it with a custom connection profile instead when encountering `This app is blocked` error when accessing Google Drive or Google Cloud Storage.

## [Add Hidden Configuration Options to Mountain Duck and Cyberduck](hidden_properties.md)
Configure hidden preferences.

## [AWS Identity & Access Management (IAM)](iam.md)
IAM allows you to create credentials for third parties accessing your S3 account with permission constraints.

## [Access Vaults on Local Disk](vault_localdisk.md)
Both [Cyberduck](../cyberduck/index.md) and [Mountain Duck](../mountainduck/index.md) support accessing vaults on your local disk.

## [Configure Public Key Authentication for SFTP](sftp_publickeyauth.md)
Configure Public Key Authentication for SFTP using OpenSSH tools.

### [Configure 1Password SSH Agent](sftp_publickeyauth_1password.md)
Authenticate with SSH private key saved in 1Password.

### [Configure Bitwarden SSH Agent](sftp_publickeyauth_bitwarden.md)
Authenticate with SSH private key saved in Bitwarden.

### [Use YubiKey](sftp_publickeyauth_yubikey.md)
Authenticate with SSH private key saved on YubiKey.

## [Use Cyberduck CLI GitHub Action](cli_github_action.md)
Use Cyberduck CLI Docker Container in GitHub Actions