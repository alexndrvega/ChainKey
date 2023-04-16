# /src/chainkey/encryption.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa

from os import urandom
import base64

# key generation
def key_generation(password, salt, iterations=100000):
    pbk = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return pbk.derive(password.encode())

# data encryptor
def data_encryptor(data, password):
    salt = urandom(16)
    key = key_generation(password, salt)

    iv = urandom(16) # init vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(salt + iv + encrypted_data).decode('utf-8')

# data decryptor
def data_decryptor(encrypted_data, password):
    encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))

    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    encrypted_data = encrypted_data[32:]

    key = key_generation(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    seed_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return seed_data.decode()