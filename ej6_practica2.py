#!/usr/bin/env python3
from Crypto.Hash import HMAC, SHA256

# Clave Compartida
password_key_store = bytes('2712A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB', 'utf-8')

# Generación
texto_origen_bytes = bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'utf-8')
hmac_origen = HMAC.new(password_key_store, msg=texto_origen_bytes, digestmod=SHA256)

# hmac_origen.update(bytes('Siguiente texto', 'utf-8')) # Solo para codificar mensajes muy largos

print("HMAC SHA256 generado: " + hmac_origen.hexdigest())

# Transmisión
mac_enviado = hmac_origen.hexdigest()
mensaje_enviado_bytes = texto_origen_bytes
print("Mensaje enviado: " + mensaje_enviado_bytes.decode('utf-8'))

# Verificación
hmac_en_destino = HMAC.new(password_key_store, digestmod=SHA256)
texto_recibido_bytes = mensaje_enviado_bytes
hmac_en_destino.update(texto_recibido_bytes)
try:
	hmac_en_destino.hexverify(mac_enviado)
	print("Mensaje validado ok")
except ValueError:
	print("Mensaje validado ko")
	
