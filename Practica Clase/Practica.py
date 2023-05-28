import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sqlite3

# Usuarios, DNI (43795713N), 
#Felipe-> cifrado del dni (AES/CBC/PKCS7)

textoPlano_bytes = bytes("43795713N", "utf-8")
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
iv_bytes = bytes.fromhex('47e6831df094b7a6c0ef1fbe0da96ad3')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
print(texto_cifrado_b64)
indice=1

try:
    bd = sqlite3.connect("Base_de_datos.db")
    print("Base de datos abierta")
    cursor = bd.cursor()

    tablas = [
            """
                CREATE TABLE IF NOT EXISTS usuarios(
                    usuario TEXT NOT NULL,
                    dni TEXT NOT NULL,
                    indice TEXT NOT NULL
                );
            """
        ]
    for tabla in tablas:
        cursor.execute(tabla);
    print("Tablas creadas correctamente")
#Insert
    usuario="Felipe"
    dni = texto_cifrado_b64
    sentencia = "INSERT INTO usuarios(usuario,dni,indice) VALUES (?,?,?)"
    cursor.execute(sentencia, [usuario,dni,indice])
    bd.commit()
    print("Insert usuario")

#Select
    cursor_lect = bd.cursor()
    sentencia_lect = "SELECT * FROM usuarios;"
    cursor_lect.execute(sentencia_lect)
    usuarios = cursor_lect.fetchall()
    print(usuarios)


except sqlite3.OperationalError as error:
    print("Error al abrir:", error)
    bd.close()