import jwt

encoded_jwt = jwt.encode({"felipe": "Keepcoding"}, "KeepCoding", algorithm="HS256")

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"KeepCoding", algorithms="HS256")

print(decode_jwt)

