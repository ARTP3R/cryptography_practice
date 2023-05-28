from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
#https://datatracker.ietf.org/doc/html/rfc7914

password = bytes('KeepCoding es un valor seguro', 'utf8')
salt = get_random_bytes(16)

key1, key2 = scrypt(password, salt, 32, N=2**14, r=8, p=1,num_keys=2) #N parametro de consumo de cpu. Potencia de 2 y menor de 2^32

#Generamos dos claves aes-256
print("Clave 1: ", key1.hex())
print("Clave 2: ", key2.hex())
