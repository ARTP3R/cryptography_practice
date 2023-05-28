from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()

privKeyPEM = RSA.import_key(keyPair.exportKey())

aes_key = get_random_bytes(16)

print("aes_key antes: ", aes_key.hex())

cipher = PKCS1_v1_5.new(pubKey)
ciphertext = cipher.encrypt(aes_key)
print(ciphertext.hex())

sentinel = get_random_bytes(16)
print("sentinel:" + sentinel.hex())

cipher = PKCS1_v1_5.new(privKeyPEM)
aes_key = cipher.decrypt(ciphertext,sentinel,expected_pt_len=16)
print("aes_key despues: ", aes_key.hex())

""" El descifrado de PKCS#1 v1.5 es intrínsecamente vulnerable a los ataques de tiempo (véase el ataque de Bleichenbacher). Utilice en su lugar PKCS#1 OAEP.

Esta implementación intenta mitigar el riesgo con algunas construcciones de tiempo constante. Sin embargo, no son suficientes por sí mismas: el tipo de protocolo que implementes y la forma en que manejes los errores marcan una gran diferencia.

En concreto, debes hacer que sea muy difícil para la parte (maliciosa) que envió el texto cifrado entender rápidamente si el descifrado tuvo éxito o no.

Para ello, se recomienda que tu protocolo sólo cifre textos planos de longitud fija (expected_pt_len), que el centinela sea una cadena de bytes aleatoria de la misma longitud, y que el procesamiento continúe durante el mayor tiempo posible incluso si el centinela es devuelto (es decir, en caso de descifrado incorrecto). """