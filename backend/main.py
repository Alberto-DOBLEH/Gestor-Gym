from flask import Flask, request, jsonify

from modelos import modelos_empleados
app = Flask(__name__)



# Enpoint Muestra todos los Usuarios
@app.route("/empleados/", methods=["GET"])
def get_empleados():
    resultados = []
    result = modelos_empleados.obtener_empleados()
    claves = ['id_empleado','nombre','primero_apellido','segundo_apellido','RFC','CURP','NSS','numero_telefono','tipo_empleado']
    for objetos in result:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        resultados.append(list2dic)

    return jsonify(resultados)

# Endpoint para obtener la informacion del usuario por medio de la id
@app.route("/empleados/<int:id>", methods=["GET"])
def get_empleado_byid(id):
    resultados = []
    result = modelos_empleados.obtener_empleado_porid(id)
    claves = ['id_empleado','nombre','primero_apellido','segundo_apellido','RFC','CURP','NSS','numero_telefono','tipo_empleado']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)

    return jsonify(resultados)

# Endpoint de inicio de sesion
@app.route("/empleados/login/", methods=["POST"])
def login():
    data = request.get_json()

    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"estado": "error", "codigo": 5, "mensaje": "Faltan campos obligatorios"}), 400

    resultado = modelos_empleados.inicio_sesion(usuario, contraseña)

    if resultado == 2:
        return jsonify({"estado": "error", "codigo": 2, "mensaje": "Usuario no encontrado"}), 404
    elif resultado == 3:
        return jsonify({"estado": "error", "codigo": 3, "mensaje": "Contraseña incorrecta"}), 401
    else:
        return jsonify({"estado": "ok", "codigo": 1, "mensaje": "Inicio de sesión exitoso"}), 200

#Enpoint para registrar empleados


#Enpoint para eliminar empleados

if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)