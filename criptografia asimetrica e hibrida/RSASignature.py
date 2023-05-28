from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Generamos un par de claves, privada-pública de 1024.
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()

# Firma del mensaje con PKCS#1 v1.5 esquema de firma (RSASP1)
msg = bytes('Asumamos el error de cara a los organismos oficiales','utf8')
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("Firma:", binascii.hexlify(signature))

# Vericar la firma con PKCS#1 v1.5 (RSAVP1)
msg = bytes('Asumamos el error de cara a los organismos oficiales','utf8')
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Firma válida.")
except:
    print("Firma invalida.")

# Verificación inválida PKCS#1 v1.5 signature (RSAVP1)
msg = bytes('Asumamos el error de cara a los organismos oficiales.','utf8')
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Firma válida.")
except:
    print("Firma invalida.")