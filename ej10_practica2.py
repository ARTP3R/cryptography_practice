#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

texto_cifrado = bytes.fromhex('7edee3ec0b808c440078d63ee65b17e85f0c1adbc0da1b7fa842f24fb06b332c156038062d9daa8ccfe83bace1dca475cfb7757f1f6446840044fe698a631fe882e1a6fc00a2de30025e9dcc76e74f9d9d721e9664a6319eaa59dc9011bfc624d2a63eb0e449ed4471ff06c9a303465d0a50ae0a8e5418a1d12e9392faaaf9d4046aa16e424ae1e26844bcf4abc4f8413961396f2ef9ffcd432928d428c2a23fb85b497d89190e3cfa496b6016cd32e816336cad7784989af89ff853a3acd796813eade65ca3a10bbf58c6215fdf26ce061d19b39670481d03b51bb0eecc926c9d6e9cb05ba56082a899f9aa72f94c158e56335c5594fcc7f8f301ac1e15a938')

# Desciframos con la clave privada

clave_privada = RSA.importKey(open('clave-rsa-oaep-priv.pem').read())
descifrar = PKCS1_OAEP.new(clave_privada, SHA256)
mensaje = (descifrar.decrypt(texto_cifrado)).hex()
print("\nTexto en claro: ", mensaje, "\n")

# Ciframos de nuevo el mensaje con la clave pública
# Ejecutando el script repetidamente se observa que el cifrado es siempre diferente

clave_publica = RSA.importKey(open('clave-rsa-oaep-publ.pem').read())
cifrar = PKCS1_OAEP.new(clave_publica, SHA256)
mensaje2 = bytes.fromhex(mensaje)
texto_cifrado2 = (cifrar.encrypt(mensaje2).hex())
print("\nMensaje cifrado de nuevo: ", texto_cifrado2, "\n")

# Volvemos a descifrar texto_cifrado2 para comprobar que es correcto

mensaje3 = bytes.fromhex(texto_cifrado2)
texto_descifrado2 = (descifrar.decrypt(mensaje3)).hex()
print("Texto en claro: ", texto_descifrado2)
