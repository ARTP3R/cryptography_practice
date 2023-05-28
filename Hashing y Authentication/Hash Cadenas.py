import hashlib

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

m = hashlib.sha1()
m.update(bytes("Hola", "utf8"))
print("SHA1:   " + m.digest().hex())

m = hashlib.sha256()
m.update(bytes("Hola", "utf8"))
print("SHA256: " + m.digest().hex())

m = hashlib.sha512()
m.update(bytes("Hola", "utf8"))
print("SHA512: " + m.digest().hex())