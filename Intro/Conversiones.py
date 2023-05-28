#Conversiones UTF8 a Hexadecimal y UTF8 a b64


#Cadena UTF8 a Hex
string_hex = bytes("Hola pepito ñ", "UTF-8").hex()
print(string_hex)

import base64

#Cadena UTF8 a Base64
string_b64 = base64.b64encode(bytes("Hola", "UTF-8"))
print(string_b64.decode('UTF-8'))

print("Decodificando....Base64 to UTF8")
print(base64.b64decode("S2VlcENvZGluZyBtb2xhIG11Y2hv").decode('utf-8'))

print("Codificando...Hex a UTF8: ", bytes.fromhex('486f6c612070657069746f20c3b1').decode('utf-8'))
