from __future__ import print_function
import base64, textwrap
import jks
import os
from cryptography import x509
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding


def print_pem(der_bytes, type):
    print("-----BEGIN %s-----" % type)
    print("\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)))
    print("-----END %s-----" % type)
    print(" ")
  

path=os.path.dirname(__file__)
print(path)

keystore=path + "/KeyStoreEjemplo"
ks = jks.KeyStore.load(keystore, "123456")
# Si cualquiera de las claves almacenadas usa una password diferente a la del keystore, se debe hacer con el siguiente comando
#ks.entries["key1"].decrypt("key_password")

for alias, pk in ks.private_keys.items():
    print("Private key: %s" % pk.alias)
    if pk.algorithm_oid == jks.util.RSA_ENCRYPTION_OID:
        print_pem(pk.pkey, "RSA PRIVATE KEY")
    else:
        print_pem(pk.pkey_pkcs8, "PRIVATE KEY")

    for c in pk.cert_chain:
        print_pem(c[1], "CERTIFICATE")
        certificado = x509.load_der_x509_certificate(c[1])
        public_key = certificado.public_key()
        print("Formato Der")
        print(public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo).hex())
        print(" ")
        print_pem(public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo), "PUBLIC KEY")

    print()


for alias, c in ks.certs.items():
    print("Certificate: %s" % c.alias)
    print_pem(c.cert, "CERTIFICATE")
    print()

for alias, sk in ks.secret_keys.items():
    print("Secret key: %s" % sk.alias)
    print("  Algorithm: %s" % sk.algorithm)
    print("  Key size: %d bits" % sk.key_size)
    print("  Key: %s" % "".join("{:02x}".format(b) for b in bytearray(sk.key)))