import os
import time
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA256

key = bytes.fromhex('d335f1fc1620685b24140c7167b603af7a647a53')
print(key.hex())
totp = TOTP(key, 8, SHA256(), 30)
time_value = time.time()
totp_value = totp.generate(time_value)

try:
    print("Otp generado:", totp_value.decode("utf8"))
    totp.verify(totp_value, time_value)
    print("Verificación correcta")

    #Forzamos una verificación incorrecta, del valor anterior
    # time.sleep (31)
    # time_value = time.time()
    # totp.verify(totp_value, time_value)

except: 
    print('Verificacion incorrecta')