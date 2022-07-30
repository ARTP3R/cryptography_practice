#!/usr/bin/env python3
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json
import hashlib

peticion = {"idUsuario":1,"usuario":"José Manuel Barrio Barrio","tarjeta":4231212345676891}

respuesta = {"idUsuario": 1, "movTarjeta": [{"id": 1, "comercio": "Comercio Juan", "importe": 5000}, {"id": 2, "comercio": "Rest Paquito", "importe": 6000}], "Moneda": "EUR", "Saldo": 23400}

json_peticion = json.dumps(peticion)

texto_plano_bytes = bytes(json_peticion, 'UTF-8')

# Hasheamos contraseña de texto plano a hex (64 carateres) y a bytes
clave_hex = hashlib.sha256()
clave_hex.update(bytes("contraseña simetrica", "utf8"))
print("SHA256: " + clave_hex.digest().hex())
clave_bytes = bytes.fromhex(clave_hex.digest().hex())

nonce_mensaje_bytes = get_random_bytes(8)


datos_asociados_bytes = bytes(str(peticion["idUsuario"]), 'utf-8')
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

descifrar = ChaCha20_Poly1305.new(key=clave_bytes, nonce=b64decode(mensaje_enviado["nonce"]))
descifrar.update(b64decode(mensaje_enviado["datos asociados"]))
texto_plano_descifrado_bytes = descifrar.decrypt_and_verify(b64decode(mensaje_enviado["texto cifrado"]), b64decode(mensaje_enviado["tag"]))
print('Datos descifrados en claro: ',texto_plano_descifrado_bytes.decode('utf-8'))
