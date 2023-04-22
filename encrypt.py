import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import sys


def encrypt(filename, key_path):
    # read key
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    # fernet = fnet(key)  # encryption key

    with open(filename, 'rb') as file:  # read in original file
        original = file.read()

    # Encrypt message
    nonce = secrets.token_bytes(12)  # GCM mode needs 12 fresh bytes every time
    ciphertext = nonce + AESGCM(key).encrypt(nonce, original, b"")

    # encrypted = fernet.encrypt(original)  # encrypt

    with open(filename, 'wb') as encrypted_file:  # write back to file as encrypted
        encrypted_file.write(ciphertext)






if __name__ == "__main__":  # init
    encrypt(sys.argv[1], sys.argv[2])
