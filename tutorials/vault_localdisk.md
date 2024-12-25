Access Cryptomator Vaults on Local Disk
===

1. Create a new [bookmark](../cyberduck/bookmarks) to connect to your local disk in Cyberduck or Mountain Duck. You can
   access any directory on your local disk that you may preset in the _Path_ option. This includes for example the
   folders of your local synchronized [Dropbox](../protocols/dropbox), [Google Drive](../protocols/googledrive)
   and [OneDrive](../protocols/onedrive) contents.

   :::{image} _images/Local_Disk_Connection.png
   :alt: Local Disk Connection
   :width: 600px
   :::

1. Choose _Connect_ and navigate to the directory containing your vault.

1. Double-clicking the vault in Cyberduck or opening the vault in Finder or Windows Explorer when connected with Mountain Duck will show _Unlock Vault_ prompt if you have _[Auto Detect](../cryptomator/index.md#auto-detect)_ enabled. Alternatively choose to _[Unlock Vault](../cryptomator/index.md#unlock-vault)_.

1. Enter the vault _Passphrase_ required to unlock and decrypt the vault contents. Optionally choose _[Save Password](../cryptomator/index.md#save-passphrase)_ if you want to store the passphrase for future usage.

   :::::{tabs}
   ::::{group-tab} Mountain Duck

   :::{image} _images/Access_Cryptomator_Vault_Mountain_Duck.png
   :alt: Mountain Duck Cryptomator Vault
   :width: 600px
   :::

   ::::
   ::::{group-tab} Cyberduck

   :::{image} _images/Access_Cryptomator_Vault_Cyberduck.png
   :alt: Cyberduck Access Cryptomator Vault
   :width: 600px
   :::

   ::::
   :::::

2. Choose the _Continue_ button to show the decrypted contents of the vault.
