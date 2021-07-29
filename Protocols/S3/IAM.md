AWS Identity & Access Management (IAM)
===

IAM allows you to create credentials for third parties accessing your S3 account with permission constraints.

# Console

You can manage IAM users using the [AWS Console](https://console.aws.amazon.com/iam/home).

# IAM Tools Setup

- Download the [IAM Command Line Toolkit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html). Unzip the download and move the folder `IAMCli-1.2.0` into the `bin` folder in your user home directory.
- In a Terminal.app window, set the home environment for IAM

		echo 'export JAVA_HOME=`/usr/libexec/java_home`' >> ~/.bash_profile
		echo 'export AWS_IAM_HOME=~/bin/IAMCli-1.2.0' >> ~/.bash_profile

- Set the environment variable to point to the credentials file.

		echo 'export AWS_CREDENTIAL_FILE=$AWS_IAM_HOME/aws-credential.template' >> ~/.bash_profile

- Add the path to the IAM programs to your path

		echo 'export PATH=$AWS_IAM_HOME/bin:$PATH' >> ~/.bash_profile

- Update the environment of the current shell (alternatively open a new Terminal.app window).

		. ~/.bash_profile

- Edit the credentials file `aws-credential.template` with your AWS identifiers.

# Create a new IAM User

Add a new IAM user and generate the access credentials. This will print out the *Access Key ID* and *Secret Access Key* to use when logging in with Cyberduck.

	iam-usercreate -u <username>;iam-useraddkey -u <username>

# Attach a Policy

Add a new policy for the user. This example gives the user access to all of your S3 resources.

	iam-useraddpolicy  -u <username> -e Allow -a s3:* -r arn:aws:s3:::* -o -p `uuidgen`

## Restrict access to a Specific Bucket

- Allow user to list contents of the bucket.

		iam-useraddpolicy  -u <username> -e Allow -a s3:ListBucket -r arn:aws:s3:::bucketname -o -p `uuidgen`
- Allow users to download files in the bucket.

		iam-useraddpolicy  -u <username> -e Allow -a s3:GetObject -r arn:aws:s3:::bucketname/* -o -p `uuidgen`

# Connecting

When you only have access to a specific bucket in the AWS account and don't have the permission to list all buckets, make sure to put `bucketname.s3.amazonaws.com` in the *Server* field of the bookmark.

# References

- [AWS Identity and Access Management (IAM) Documentation](http://aws.amazon.com/documentation/iam/)