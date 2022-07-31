#!/usr/bin/env python3
# Funciona con python 3.10 y 3.9

import jwt
import json
import hashlib
from ssl import VerifyFlags

# librerías para cripto AES CBC
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

peticion = {"idUsuario":1,"usuario":"José Manuel Barrio Barrio","tarjeta":4231212345676891}


respuesta = {"idUsuario": 1, "movTarjeta": [{"id": 1, "comercio": "Comercio Juan", "importe": 5000}, {"id": 2, "comercio": "Rest Paquito", "importe": 6000}], "Moneda": "EUR", "Saldo": 23400}

# PETICIÓN

# Hasheamos los datos que requieren privacidad si se intercepta y se compromete la contraseña.
# En destino se puede comparar el hash como una capa más de integridad de la petición.
hash_nombre = hashlib.sha3_256()
hash_nombre.update(bytes(peticion["usuario"],"UTF-8"))
usuario = hash_nombre.hexdigest()
hash_tarjeta = hashlib.sha3_256()
hash_tarjeta.update(bytes(str(peticion["tarjeta"]),"UTF-8"))
# ^ integer pasado a cadena y a bytes
tarjeta = hash_tarjeta.hexdigest()
print("\nhash usuario:        ", usuario)
print("hash tarjeta:        ", tarjeta)

# Montamos el JWT y enviamos
jwt_peticion = jwt.encode({"idUsuario":1,"usuario":usuario,"tarjeta":tarjeta}, "contraseña simetrica ya compartida", algorithm="HS256")
print("peticion JWT:        ", jwt_peticion)
print("Petición enviada.")
# Llega a destino y se decodifica el JSON
decoded_jwt = jwt.decode(jwt_peticion,"contraseña simetrica ya compartida", algorithms="HS256")
print("JWT recibido:        ", decoded_jwt)
print("================================")

# Encontramos al usuario en la BD sin complicarnos con el código
if peticion["idUsuario"] == respuesta["idUsuario"]:
	print("\nUsuario", respuesta["idUsuario"], "encontrado en base de datos.") # por ejemplo
if "los hashes del usuario 1 en destino coinciden":
	print("Prueba hash de integridad ok\n")
else:
	print("petición incorrecta o comprometida\n")

# RESPUESTA

# Generación de claves RSA
# En terminal: openssl genrsa -out private2.pem 2048
# En terminal: openssl rsa -in private.pem -pubout -out public.pem

# Claves RSA mejor desde ficheros para evitar errores de entrada
public_key = open("./public.pem").read()
private_key = open("./private.pem").read()

# Clave pública sin asociar a ninguna privada
public_key2 = open("./public2.pem").read()


print("================================")
encoded = jwt.encode({"idUsuario": 1, "movTarjeta": [{"id": 1, "comercio": "Comercio Juan", "importe": 5000}, {"id": 2, "comercio": "Rest Paquito", "importe": 6000}], "Moneda": "EUR", "Saldo": 23400}, private_key, algorithm="RS256")
print(encoded)

# Cifrado AES-CBC PKCS7 en otra capa de seguridad
# Ingredientes
textoPlano_bytes = bytes(encoded, 'UTF-8')
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d') 
iv_bytes = bytes.fromhex('47e6831df094b7a6c0ef1fbe0da96ad3')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)

# a cifrar
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
iv_b64 = b64encode(cipher.iv).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
mensaje_json = json.dumps({'iv':iv_b64, 'texto cifrado':texto_cifrado_b64})

print("\nrespuesta enviada\n")

# descifrando respuesta
b64 = json.loads(mensaje_json)
iv_desc_bytes = b64decode(b64['iv'])
texto_cifrado_bytes = b64decode(b64['texto cifrado'])
cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")

print("================================")
decode = jwt.decode(mensaje_des_bytes, public_key,algorithms="RS256", options={"verify_signature": True})

print("Datos solicitados formato JSON: ", decode)

