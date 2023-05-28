
   
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cliente -> Cifrando el dato, para lo cual, algoritmo (AES/CBC/PKCS7)
#Cifrado
textoPlano_bytes = bytes('KeepCoding mola un montón.k', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
iv_bytes = bytes.fromhex('47e6831df094b7a6c0ef1fbe0da96ad3')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
#Provocamos un fallo por padding incorrecto
#texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
iv_b64 = b64encode(cipher.iv).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
mensaje_json = json.dumps({'iv':iv_b64, 'texto cifrado':texto_cifrado_b64})
print(mensaje_json)

#Descifrado
#Servidor, necesita descifrarlo. Recupera el json, y obtiene los campos. Iv entrada, y obtiene el texto cifrado entrada. Aplica el algoritmo (AES/CBC/PKCS7)
try:
    b64 = json.loads(mensaje_json)
    iv_desc_bytes = b64decode(b64['iv'])
    texto_cifrado_bytes = b64decode(b64['texto cifrado'])
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")
    #mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
    print("En hex: ", mensaje_des_bytes.hex())
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 