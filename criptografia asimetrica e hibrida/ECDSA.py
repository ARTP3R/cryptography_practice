from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

key = ECC.generate(curve='P-256')
privKey = key.export_key(format='PEM')
print("Clave Privada: \n", privKey)
publicKey = key.public_key().export_key(format='PEM')
print("Clave Pública: \n", publicKey)

# Generación de firma
# Modificado partiendo de  https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
message = bytes('Se debe hacer una propuesta de mejora del contrato de venta','utf8')
key_orig = ECC.import_key(privKey)
h = SHA256.new(message)

#El tipo de firma es el sugerido en el documento de fips-186-3.
signer = DSS.new(key_orig, 'fips-186-3')
signature = signer.sign(h)


# Verificación de firma
key_dest = ECC.import_key(publicKey)
h = SHA256.new(message)
verifier = DSS.new(key_dest, 'fips-186-3')
try:
    verifier.verify(h, signature)
    print ("Mensaje autenticado")
except ValueError:
    print ("Mensaje no autenticado")

