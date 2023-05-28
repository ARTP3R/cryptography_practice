import os
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA256

try:

    key = bytes.fromhex('d335f1fc1620685b24140c7167b603af7a647a53')
    hotp = HOTP(key, 8, SHA256())
    counter=1

    hotp_value = hotp.generate(counter)
    print("Otp generado:", hotp_value.decode("utf8"))
    hotp.verify(hotp_value, counter)

    print("Verificado")
    counter = counter + 1
    hotp.verify(hotp_value, counter)

except:
    print("No verificado, para el counter ", counter)