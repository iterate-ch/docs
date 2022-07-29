Seagate Lyve Cloud
====

> Lyve™ is an edge-to-cloud mass storage platform from Seagate®—built for the distributed enterprise to capture the unstructured data explosion.

## Connection

- Protocol: `S3 (HTTPS)`
- Server: `<your endpoint>`
- Access Key ID: `<your access key>`
- Secret Access Key: `<your secret access key>`

```{hint}
Available [endpoints](https://help.lyvecloud.seagate.com/en/s3-api-endpoint.html) are
- US-East-1 (Virginia): `https://s3.us-east-1.lyvecloud.seagate.com`
- US-West-1 (California): `https://s3.us-west-1.lyvecloud.seagate.com`
- AP-Southeast-1 (Singapore): `https://s3.ap-southeast-1.lyvecloud.seagate.com`
```

### Create access keys

You have to create service accounts within the *Lyve Cloud console* to use third party tools:

1. [Sign in](https://console.lyvecloud.seagate.com) to your Lyve Cloud via web browser.
2. Select *Service Accounts* from the sidebar menu and choose *Create Service Account*.
3. Enter the name and permissions.
4. Choose *Create*. The access key will be generated and the details of the key will be displayed in a popup window.

```{note}
The prompt contailing the access key information will only be displayed once. Make sure to save the details for future use.
```

## References

- [Using Cyberduck with Lyve Cloud](https://help.lyvecloud.seagate.com/en/using-cyberduck.html)
- [Using Mountain Duck with Lyve Cloud](https://help.lyvecloud.seagate.com/en/using-mountain-duck.html)