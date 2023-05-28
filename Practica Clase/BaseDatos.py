import sqlite3

try:
    bd = sqlite3.connect("Base_de_datos.db")
    print("Base de datos abierta")
    cursor = bd.cursor()

    tablas = [
            """
                CREATE TABLE IF NOT EXISTS usuarios(
                    usuario TEXT NOT NULL,
                    password TEXT NOT NULL
                );
            """
        ]
    for tabla in tablas:
        cursor.execute(tabla);
    print("Tablas creadas correctamente")
#Insert
    usuario="Antonio"
    password = "ueruiiuheq"
    sentencia = "INSERT INTO usuarios(usuario,password) VALUES (?,?)"
    cursor.execute(sentencia, [usuario,password])
    bd.commit()
    print("Insert usuario")

#Select
    cursor_lect = bd.cursor()
    sentencia_lect = "SELECT * FROM usuarios;"
    cursor_lect.execute(sentencia_lect)
    usuarios = cursor_lect.fetchall()
    print(usuarios)

#Update
    cursor = bd.cursor()
    sentencia = "UPDATE usuarios SET password = ? WHERE usuario = ?;"
    cursor.execute(sentencia,["123456", "Antonio"])
    bd.commit()

    #Mostramos los datos tras actualizar
    cursor_lect = bd.cursor()
    sentencia_lect = "SELECT * FROM usuarios;"
    cursor_lect.execute(sentencia_lect)
    datos = cursor_lect.fetchall()
    print(datos)

#Delete
    sentencia = "DELETE FROM usuarios WHERE usuario = ?"
    cursor.execute(sentencia, ["Antonio"])
    bd.commit()

    #Mostramos los datos tras borrar
    cursor_lect = bd.cursor()
    sentencia_lect = "SELECT * FROM usuarios;"
    cursor_lect.execute(sentencia_lect)
    datos = cursor_lect.fetchall()
    print(datos)
    bd.close()

    print("Buscamos valores determinados")
    for user in datos:
        #Nombre
        print(user[0])
        #Password
        print(user[1])

except sqlite3.OperationalError as error:
    print("Error al abrir:", error)
    bd.close()