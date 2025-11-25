Tutorials
====

:::{toctree}
:hidden:
:titlesonly:
hidden_properties
custom_oauth_client_id
s3_iam_role_mfa
s3_iam_getsessiontoken_bucketpolicy_mfa
s3_microsoft_entra_oidc
s3_google_oidc
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

## [Connect to S3 with assuming role requiring MFA input](s3_iam_role_mfa.md)
Require user to use MFA when connecting to S3 by connecting with IAM role assumed with AWS Security Token Service (STS).

## [Connect to S3 with temporary session token and MFA input](s3_iam_role_mfa.md)
Require user to use MFA when connecting to S3 bucket with policy requiring MFA by requesting temporary credentials obtained from IAM AWS Security Token Service (STS).

## [Authenticate with Microsoft Entra ID to connect to S3](s3_microsoft_entra_oidc.md)
Use Microsoft Entra ID to authenticate with S3 by configuring as an OpenID Connect (OIDC) Identity Provider in AWS IAM.

## [Authenticate with Google to connect to S3](s3_google_oidc.md)
Use Google to authenticate with S3 by configuring as an OpenID Connect (OIDC) Identity Provider in AWS IAM.

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