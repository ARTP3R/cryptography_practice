from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check

password = bytes('KeepCoding es un valor seguroKeepCoding es un valor seguroKeepCoding es un valor seguroKeepCoding es un valor seguro', 'utf8')
b64pwd = b64encode(SHA256.new(password).digest())
#b64pwd = password
#print(len(b64pwd))

bcrypt_hash = bcrypt(b64pwd, 12)
#print(bcrypt_hash.hex())

password_to_test = bytes('KeepCoding es un valor seguroKeepCoding es un valor seguroKeepCoding es un valor seguroKeepCoding es un valor seguro', 'utf8')

try:
    b64pwd = b64encode(SHA256.new(password).digest())
    bcrypt_check(b64pwd, bcrypt_hash)
    print("Password correcta")
except ValueError:
    print("Password incorrecta")