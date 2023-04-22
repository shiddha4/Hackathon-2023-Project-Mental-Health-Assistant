from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import sys


def decrypt1(filename, key_path):
    try:
        with open(key_path, 'rb') as filekey:
            key = filekey.read()

        # fernet = fnet(key)
        with open(filename, 'rb') as file:
            ciphertext = file.read()

        # decrypt = fernet.decrypt(original)
        plaintext = AESGCM(key).decrypt(ciphertext[:12], ciphertext[12:], b"")

        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(plaintext)
        return True
    except:
        return False

if __name__ == "__main__":
    decrypt1(sys.argv[1], sys.argv[2])
