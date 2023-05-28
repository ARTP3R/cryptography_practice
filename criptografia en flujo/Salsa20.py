from Crypto.Cipher import Salsa20
from base64 import b64decode, b64encode

textoPlano = bytes('Si has llegado hasta aquí tienes posibilidades de ser un fuera de serie', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca')
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = bytes.fromhex('fbdbffb77f5966b2')
print('nonce  = ', nonce_mensaje.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = Salsa20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode())


#Descifrado...
decipher = Salsa20.new(key=clave, nonce=nonce_mensaje)
plaintext = decipher.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))


#nonce  =  fbdbffb77f5966b2
#Mensaje cifrado en HEX =  bbc80c978117d14a0d08e01e84fcbfa30f5af52d7e2fb27ef9c995cb16621ce89f1726f8264fad31c8bc80edde320f4a64e0c904b211d2259edc6dab2b346c8ec744ab05501ae8132f043dd15842de94d2ec150760514123deaf4e6b0bca
#Mensaje cifrado en B64 =  u8gMl4EX0UoNCOAehPy/ow9a9S1+L7J++cmVyxZiHOifFyb4Jk+tMci8gO3eMg9KZODJBLIR0iWe3G2rKzRsjsdEqwVQGugTLwQ90VhC3pTS7BUHYFFBI96vTmsLyg==
#Mensaje en claro =  Cualquier desarrollador que use este libro será capaz de cifrar y descifrar con poco esfuerzo