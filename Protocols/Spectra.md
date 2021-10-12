Spectra BlackPearl Deep Storage Gateway
===

![Spectra Drive Icon](_images/spectra_128x128.png)

> S3 Gateway to Deep Storage. The Spectra Logic BlackPearl Converged Storage System provides an easy, cloud-like interface to on-premise storage solutions, including to disk, tape, and cloud targets for maximum protection.

# Connecting

- {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Spectra%20S3%20(HTTPS).cyberduckprofile>` the Spectra S3 (HTTPS) Connection Profile for preconfigured settings.
- {download}`Download<https://github.com/iterate-ch/cyberduck/raw/master/profiles/Spectra%20S3%20(HTTP).cyberduckprofile>` the Spectra S3 (HTTP) Connection Profile for preconfigured settings.

Refer to [Profiles](../Cyberduck/Connection#connection-profiles) for documentation about connection profiles. Choose Spectra BlackPearl Deep Storage Gateway (HTTP) from the list of protocols when editing a [bookmark](../Cyberduck/Bookmarks) or use the `spectra://` scheme when using the [CLI](../CLI/index).

# Additional Information

## Transfer → Retries

Reading a file from Spectra S3 might trigger a Retry wait for up to 300 seconds when the file is not yet in the cache.

![Cache Retry](_images/Cache_Retry.png)

## Transfer → Multiple Connections

Use the lower right toggle to set the number of concurrent connections for file transfers. Refer to [Multiple Connections](../Cyberduck/Transfer#multiple-connections). This allows saturating the bandwidth when running in a fast local network.

![10GbE Transfer](_images/10GbE_Transfer.png)

# Limitations

## Rename and Move File

Not supported.

# References

- [S3 Gateway to Deep Storage](https://www.spectralogic.com/products/blackpearl/)
- [The first RESTful interface to deep storage](https://www.spectralogic.com/products/spectra-s3/)
- [Official Cyberduck BlackPearl Documentation](https://developer.spectralogic.com/cyberduck/)
- [BlackPearl and Cyberduck Deliver End-to-End Hybrid Cloud Storage Solution](https://edge.spectralogic.com/index.cfm?&fuseaction=home.displayFile&DocID=4839)