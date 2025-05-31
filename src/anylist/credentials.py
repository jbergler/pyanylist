import os
import json
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

CREDENTIALS_KEY_CLIENT_ID = "clientId"
CREDENTIALS_KEY_ACCESS_TOKEN = "accessToken"
CREDENTIALS_KEY_REFRESH_TOKEN = "refreshToken"

def derive_key(password):
    sha = hashlib.sha256(password.encode()).digest()
    return sha[:32]

def encrypt_credentials(credentials, secret):
    plain = json.dumps(credentials).encode()
    key = derive_key(secret)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    pad_len = 16 - (len(plain) % 16)
    plain += bytes([pad_len] * pad_len)
    encrypted = encryptor.update(plain) + encryptor.finalize()
    return json.dumps({
        "iv": iv.hex(),
        "cipher": encrypted.hex(),
    })

def decrypt_credentials(credentials, secret):
    encrypted = json.loads(credentials)
    key = derive_key(secret)
    iv = bytes.fromhex(encrypted["iv"])
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plain = decryptor.update(bytes.fromhex(encrypted["cipher"])) + decryptor.finalize()
    pad_len = plain[-1]
    plain = plain[:-pad_len]
    return json.loads(plain.decode())