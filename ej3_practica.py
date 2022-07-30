#!/usr/bin/env python3
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

texto_plano_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado', 'UTF-8')
clave_bytes = bytes.fromhex('979DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje_bytes = bytes(b64decode("9Yccn/f5nJJhAt2S")) # nonce_mensaje_bytes = get_random_bytes(16)

#datos_asociados_bytes = bytes('Datos no cifrados sólo autenticados', 'utf-8')
datos_asociados_bytes = bytes('datos firmados sin cifrar', 'utf-8')
cifrar = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_mensaje_bytes)
cifrar.update(datos_asociados_bytes)

texto_cifrado, tag = cifrar.encrypt_and_digest(texto_plano_bytes)
print("texto cifrado: ", b64encode(texto_cifrado))
print("tag: ", b64encode(tag))

mensaje_enviado = {
    "nonce": b64encode(nonce_mensaje_bytes).decode(),
    "datos asociados": b64encode(datos_asociados_bytes).decode(),
    "texto cifrado": b64encode(texto_cifrado).decode(),
    "tag": b64encode(tag).decode()
    }
json_mensaje = json.dumps(mensaje_enviado)
print("--------------------------")
print("Mensaje enviado / recibido: ", json_mensaje)

# RECEPTOR DEL MENSAJE
print("--------------------------")
print("Descifrando y verificando...")
try:
    descifrar = ChaCha20_Poly1305.new(key=clave_bytes, nonce=b64decode(mensaje_enviado["nonce"]))
    descifrar.update(b64decode(mensaje_enviado["datos asociados"]))
    texto_plano_descifrado_bytes = descifrar.decrypt_and_verify(b64decode(mensaje_enviado["texto cifrado"]),
        b64decode(mensaje_enviado["tag"]))
    print('Datos descifrados en claro: ',texto_plano_descifrado_bytes.decode('utf-8'))
except (ValueError, KeyError) as error_descifrar:
    print("Error encontrado: ", error_descifrar)

