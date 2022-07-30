import hashlib

mensaje = hashlib.sha256()
mensaje.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA256: " + mensaje.digest().hex())

mensaje = hashlib.sha512()
mensaje.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA512: " + mensaje.digest().hex())