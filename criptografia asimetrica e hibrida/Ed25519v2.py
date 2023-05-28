from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography import exceptions
from cryptography.hazmat.primitives import serialization
import binascii


private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(bytes("Vamos a generar este mensaje autenticado", "utf8"))

public_key = private_key.public_key()

try:
    public_key.verify(signature, bytes("Vamos a generar este mensaje autenticado", "utf8"))

except exceptions.InvalidSignature:
  print("Error validando la firma!")
else:
  print("Mensaje firmado correctamente")

pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

der = private_key.private_bytes(encoding=serialization.Encoding.DER,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
print ("\nClave privada formato PEM:\n",pem.decode())
print ("Clave privada formato DER:\n",der.hex())

pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
der = public_key.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)

print ("\nClave pública formato PEM:\n",pem.decode())
print ("Clave pública formato DER:\n",der.hex())
