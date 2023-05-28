import ed25519

privKey, pubKey = ed25519.create_keypair()
print("Private key (32 bytes):", privKey.to_ascii(encoding='hex'))
print("Public key (32 bytes): ", pubKey.to_ascii(encoding='hex'))

msg = bytes('Firmamos esto con la curva 25519','utf8')
signature = privKey.sign(msg, encoding='hex')
print("Firma Generada (64 bytes):", signature)
#signature = b'78613ae771b5b220d2a72008d7cf3bc6f232547692b02d38ffc671c70eb2015dc697252fbefa087995b2379e1422044cd1dcd03b631351188e1ae62a5dc27701'

try:
    pubKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
