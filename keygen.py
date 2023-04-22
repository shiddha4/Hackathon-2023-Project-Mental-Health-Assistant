import sys
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def keygen(key_ID):
    key_path = "keys/" + key_ID + ".key"
    key = secrets.token_bytes(32)  # Generate a random secret key for good AES-256 encryption
    # key = fnet.generate_key()  # crappy AES-128 encryption

    with open(key_path, 'wb') as filekey:
        filekey.write(key)


if __name__ == "__main__":
    keygen(sys.argv[1])
