from base64 import b64decode
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

#Versión con gestión de padding.   CLIENTE (key, iv, algoritmo)---> SERVIDOR (key,iv, algoritmo)
# Ej algoritmo: triple des, modo CBC y padding pkcs7 

key = bytes.fromhex("2b7e151628aed2a6abf715891defefef123456781232aaff")
iv = bytes.fromhex("10100111111111FA")
cipher = DES3.new(key, DES3.MODE_CBC,iv)
#CIFRADO
#Cliente

plaintext = bytes('A really secret messagessssss','utf8')
msg = cipher.encrypt(pad(plaintext, DES3.block_size,  style='pkcs7'))
mensaje_cifrado = iv + msg
b64_msg = b64encode(msg).decode('utf8')
print("Base64 cifrado:", b64_msg)
print("Mensaje descifrado: ", msg.hex())

# https://gchq.github.io/CyberChef/ --> cbc/nopadding
#DESCIFRAMOS EL MENSAJE
#Servidor
cipher2 = DES3.new(key,DES3.MODE_CBC,iv)
mensaje_en_claro = unpad(cipher2.decrypt(msg), DES3.block_size,style='pkcs7')
#mensaje_en_claro = cipher2.decrypt(msg)
print("Descifrado, hex: ", mensaje_en_claro.hex())
print("Descifrado, string: ", mensaje_en_claro.decode('utf-8'))
