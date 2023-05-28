from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import binascii

#Generamos un par de claves
#keyPair = RSA.generate(2048)
keyPair = RSA.generate(3072)


#Generamos la clave pública
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('utf8'))
print("--------------------------------------------------")
#Generamos la clave privada.
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('utf8'))

print("--------------------------------------------------")

#Cifrado

#msg = bytes('Cifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidez','utf8')
#print(len(msg))
# Si estas usando RSA 2048 y sha256. Se pasa a byte 2048, le quitas 2, lo vuelves a pasar a byte. Luego a eso le restas el doble del hash (512) y todo ello entre 8, te da 190.
msg = bytes('Cifrar con RSA grandes textos es una estupidez','utf-8')

#Si no se añade el hash, funciona pero con sha1 by default
#encryptor = PKCS1_OAEP.new(pubKey)
encryptor = PKCS1_OAEP.new(pubKey, SHA256)
encrypted = encryptor.encrypt(msg)

#print("Cifrado:", binascii.hexlify(encrypted))
print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")

#Descifrado
#decryptor = PKCS1_OAEP.new(keyPair)
decryptor = PKCS1_OAEP.new(keyPair,SHA256)
decrypted = decryptor.decrypt(encrypted)
print('Descifrado:', decrypted)