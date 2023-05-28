
from flask import Flask, jsonify,request
import json
import slqlite3


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hola, todo va bien!"})

@app.route("/tarjetas", methods=['POST'])
def tarjetas():

    #Obtenemos el body en formato json
    request_data = request.get_json()
    
    #Obtenemos un campo determinado
    nombre = request_data["nombre"]

    #Montamos un json para su respuesta
    tarjetas = {"tarjeta": 423456789021234}

    #Recuperamos datos de la cabecera
    jwt = request.headers.get('jwt')

    #Escribir log
    app.logger.info(jwt)
    app.logger.info (nombre)


    return tarjetas





#Iniciamos el servidor
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)