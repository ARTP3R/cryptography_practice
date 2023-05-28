from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets

salt = secrets.token_bytes(16)
master_secret = secrets.token_bytes(64)
key1, key2 = HKDF(master_secret, 32, salt, SHA512, 2)

print("Clave key1: ", key1.hex())
print("Clave key2: ", key2.hex())