from flask import Flask, request, jsonify
from modelos import modelos_empleados
app = Flask(__name__)


# Enpoint Muestra todos los Usuarios
@app.route("/empleados", methods=["GET"])
def get_empleados():
    resultados = []
    result = modelos_empleados.obtener_empleados()
    claves = ['id', 'nombres', 'correo']
    for objetos in result:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        resultados.append(list2dic)

    return jsonify({"data":resultados})



if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)