import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes('Vamos a aprender a cifrar con un AES-CTR que es una especie de cifrador de flujo bajo uno de bloque', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
nonce = bytes.fromhex('47e6831df094b7a6')
cipher = AES.new(clave, AES.MODE_CTR,nonce=nonce)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
nonce_b64 = b64encode(cipher.nonce).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
mensaje_json = json.dumps({'nonce':nonce_b64, 'texto cifrado':texto_cifrado_b64})
print(mensaje_json)

#Descifrado

try:
    b64 = json.loads(mensaje_json)
    nonce_desc_bytes = b64decode(b64['nonce'])
    texto_cifrado_bytes = b64decode(b64['texto cifrado'])
    cipher = AES.new(clave, AES.MODE_CTR, nonce=nonce_desc_bytes)
    mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 