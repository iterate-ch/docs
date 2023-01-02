Encryption Security Architecture
====

Please refer to [Cryptomator](https://docs.cryptomator.org/en/latest/security/architecture/) security overview for more details.

## Masterkey

 Each vault has its own 256 bit encryption as well as MAC masterkey used for encryption of file specific keys and file authentication, respectively. Both keys are encrypted using RFC 3394 key wrapping with a KEK derived from the user's password using scrypt.

The wrapped keys (with some additional metadata) are remotely stored in a JSON file named masterkey.cryptomator located in the root directory of a vault.

## Filename Encryption

Cryptomator uses AES-SIV to encrypt file as well as directory names. Additionally to the name, a unique directory ID of its parent directory is passed as associated data. This prevents undetected moving of files between directories.

## File Header Encryption

The file header stores certain metadata, which is needed for file content encryption. It consists of 88 bytes.

- 16 bytes nonce used during header payload encryption
- 40 bytes AES-CTR encrypted payload consisting of:
	- 8 bytes filled with 1 for future use (formerly used for file size)
	- 32 bytes file content key
	- 32 bytes header MAC of the previous 56 bytes

## File Content Encryption

The cleartext is broken down into multiple chunks, each up to 32 KiB + 48 bytes consisting of:

- 16 bytes nonce
- up to 32 KiB encrypted payload using AES-CTR with the file content key
- 32 bytes MAC of
	- file header nonce (to bind this chunk to the file header)
	- chunk number as 8 byte big endian integer (to prevent undetected reordering)
	- nonce
	- encrypted payload

## References

[Security Architecture Overview](https://docs.cryptomator.org/en/latest/security/architecture/#)