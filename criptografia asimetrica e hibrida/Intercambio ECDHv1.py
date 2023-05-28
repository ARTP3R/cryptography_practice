from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

#En esta clase no hemos usado ninguna autenticación.
class ECDHExchange:
    def __init__(self, curve):
        self._curve = curve
        # Generamos una clave privada efímera para usar en el intercambio
        self._private_key = ec.generate_private_key(
            curve, default_backend())

        self.enc_key = None
        self.mac_key = None

    def get_public_bytes(self):
        public_key = self._private_key.public_key()
        raw_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo)
        return raw_bytes

    def generate_session_key(self, peer_bytes):
        peer_public_key = serialization.load_pem_public_key(
            peer_bytes,
            backend=default_backend())
        shared_key = self._private_key.exchange(
            ec.ECDH(),
            peer_public_key)

        # Derivamos 64 bytes de "key material" para generar dos claves de 32 bytes.
        key_material = HKDF(
            algorithm=hashes.SHA256(),
            length=64,
            salt=None,
            info=None,
            backend=default_backend()).derive(shared_key)

        # Obtenemos la clave de cifrado
        self.enc_key = key_material[:32]

        # Obtenemos la clave de mac
        self.mac_key = key_material[32:64]

# Test para demostrar su funcionamiento. Nos debemos fijar en que usamos la pública del otro.
client_x = ECDHExchange(ec.SECP384R1())
client_y = ECDHExchange(ec.SECP384R1())
client_x.generate_session_key(client_y.get_public_bytes())
client_y.generate_session_key(client_x.get_public_bytes())

print("Clave Cifrado cliente X: ", client_x.enc_key.hex())
print("Clave Cifrado cliente Y: ", client_y.enc_key.hex())

print("Clave Mac cliente X:     ", client_x.mac_key.hex())
print("Clave Mac cliente Y:     ", client_y.mac_key.hex())

#Test para verificar el resultado
if client_x.enc_key == client_y.enc_key and client_x.mac_key == client_y.mac_key:
    print("El resultado es [OK]")
else:
    print("El resultado es [ERROR]")
