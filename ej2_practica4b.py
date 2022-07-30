#!/usr/bin/env python3
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Clave Keystore “cifrado-sim-aes-256”
clave_bytes = bytes.fromhex('E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')

# Datos enunciado
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
dato_cifrado = "zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNIosyKfkNKG9GGSgG1awaZg=="
dato_cifrado_bytes = b64decode(dato_cifrado)

cifrado = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)

# Desencriptado del dato
dato_descifrado_bytes = cifrado.decrypt(dato_cifrado_bytes)

# Quitando el padding
dato_descifrado_unpad_bytes = unpad(dato_descifrado_bytes, AES.block_size, style="pkcs7")

# Decodificando a UTF-8 e imprimiendo
print("Dato en claro: ", dato_descifrado_unpad_bytes.decode("utf-8"))

# Formateando salida
a = str(dato_descifrado_bytes.hex())
b = str(dato_descifrado_unpad_bytes.hex())
la = len(a)
lb = len(b)
padding = a[lb:la]
print("padding: ", padding)
mask = "|"
for i in range(len(padding)-2):
	mask = mask + "*"
mask = mask + "|"
print(a)
print(b + mask)
