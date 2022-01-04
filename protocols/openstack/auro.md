AURO
====

```{image} _images/Auro_Logo.jpg
:alt: AURO Logo
:height: 128px
```

> AURO is 100% Canadian owned and operated provider of public cloud infrastructure based on OpenStack.

# Connecting

- Protocol: `Swift (OpenStack Object Storage)`
- Server: `api.van1.auro.io`
- Port: `5000`
- Username: `<os-tenant-name>:<os-username>`
- Password: `<os-password>`

The server name is found in the Cloud Dashboard under `Project/Compute/Access & Security/API Access`. Use the Identity server, not the Object Store server.

The username is a concatenation of your OpenStack tenant name and OpenStack user name. These values can be found in your [OpenStack RC file](https://login.van1.auro.io/project/access_and_security/api_access/openrc/).

# References

- [Swift Usage](https://www.auro.io/support/CLI/swift/)