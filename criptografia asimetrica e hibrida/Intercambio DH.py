from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

# Ejemplo adaptado de https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/#:~:text=Diffie%2DHellman%20key%20exchange%20(D,secret%20using%20an%20insecure%20channel.
# Generamos algunos parámetros que pueden ser reusados.
parameters = dh.generate_parameters(generator=2, key_size=1024,
                                     backend=default_backend())


#Generamos una clave privada para el intercambio.
private_key = parameters.generate_private_key()

#En el mundo real, en un handshake recibimos la clave pública desde un tercero. En este ejemplo, generamos la clave pública partiendo de otra
#privada que hemos generado. 
peer_private_key = parameters.generate_private_key()
peer_public_key = peer_private_key.public_key()

#Generamos la clave compartida con la publica de destino.
shared_key = private_key.exchange(peer_public_key)

# Derivamos la clave compartida para obtener la de sesión.
derived_key = HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt=None,
     info=b'handshake data',
     backend=default_backend()
).derive(shared_key)

print("Clave derivada en origen:  ", derived_key.hex())


same_shared_key = peer_private_key.exchange(
    private_key.public_key()
)

#En destino se realiza el mismo algoritmo de derivación
same_derived_key = HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt=None,
     info=b'handshake data',
     backend=default_backend()
).derive(same_shared_key)


print("Clave derivada en destino: ", same_derived_key.hex())


