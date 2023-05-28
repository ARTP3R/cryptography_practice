from ssl import VerifyFlags
import jwt
#Generamos claves RSA
#openssl genrsa -out private2.pem 2048
#openssl rsa -in private.pem -pubout -out public.pem

#Mejor leerlo desde ficheros para evitar problemas de formato en entrada de claves
public_key = open("/Users/feliperodriguezfonte/Documents/Criptografía - 4 edición/Mi Codigo fuente/Hashing y Authentication/public.pem").read()
private_key = open("/Users/feliperodriguezfonte/Documents/Criptografía - 4 edición/Mi Codigo fuente/Hashing y Authentication/private.pem").read()

#Clave pública sin asociar a ninguna privada
public_key2 = open("/Users/feliperodriguezfonte/Documents/Criptografía - 4 edición/Mi Codigo fuente/Hashing y Authentication/public2.pem").read()

print("================================")
encoded = jwt.encode({"usuario": "Felipe Rodríguez", "rol": "profesor", "acceso": "administrador"}, private_key, algorithm="RS256")
print(encoded)
print("================================")
decode = jwt.decode(encoded, public_key,algorithms="RS256", options={"verify_signature": True})
print(decode)
print("================================")
#Forzamos fallo con la verificación de clave pública incorrecta
decode2 = jwt.decode(encoded, public_key2,algorithms="RS256", options={"verify_signature": True})
print(decode2)