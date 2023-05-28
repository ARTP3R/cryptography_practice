from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

#https://www.ietf.org/rfc/rfc2898.txt
password = bytes('KeepCoding es un valor seguro', 'utf8')
salt = get_random_bytes(16)
keys = PBKDF2(password, salt, 64, count=1000000, hmac_hash_module=SHA512)
key1 = keys[:32]
key2 = keys[32:]

#Generamos dos claves aes-256
print("Clave 1: ", key1.hex())
print("Clave 2: ", key2.hex())

