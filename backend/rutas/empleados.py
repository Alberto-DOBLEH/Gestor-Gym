from flask import Flask, request, Blueprint, jsonify
from modelos import modelos_empleados

empleados_bp = Blueprint('empleados', __name__)

# Enpoint Muestra todos los Usuarios
@empleados_bp.route("/", methods=["GET"])
def get_empleados():
    resultados = []
    result = modelos_empleados.obtener_empleados()
    claves = ['id_empleado','nombre','primero_apellido','segundo_apellido','RFC','CURP','NSS','numero_telefono','tipo_empleado']
    for objetos in result:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        resultados.append(list2dic)

    return jsonify(resultados)

# Endpoint para obtener la informacion del usuario por medio de la id
@empleados_bp.route("/<int:id>", methods=["GET"])
def get_empleado_byid(id):
    resultados = []
    result = modelos_empleados.obtener_empleado_porid(id)
    claves = ['id_empleado','nombre','primero_apellido','segundo_apellido','RFC','CURP','NSS','numero_telefono','tipo_empleado']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)

    return jsonify(resultados)

# Endpoint para obtener la informacion del usuario por medio del username
@empleados_bp.route("/<string:username>", methods=["GET"])
def get_empleado_by_username(username):
    resultados = []
    result = modelos_empleados.obtener_empleado_por_username(username)
    claves = ['id_empleado','nombre','primero_apellido','segundo_apellido','RFC','CURP','NSS','numero_telefono','tipo_empleado']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)

    return jsonify(resultados)

# Endpoint de inicio de sesion
@empleados_bp.route("/login/", methods=["POST"])
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
@empleados_bp.route("/agregar/",methods=["POST"])
def add_empleados():
    data = request.get_json()

    nombre = data.get("nombre")
    primero_apellido = data.get("primer_apellido")
    segundo_apellido = data.get("segundo apellido")
    RFC = data.get("RFC")
    CURP = data.get("CURP")
    NSS = data.get("NSS")
    numero_telefono  = data.get("numero_telefono")
    tipo_empleado = data.get("tipo_empleado")
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    resultado = modelos_empleados.agregar_empleado(nombre, primero_apellido, segundo_apellido, RFC, CURP, NSS, numero_telefono, tipo_empleado, usuario, contraseña)

    if resultado == 1:
        return jsonify({"estado": "correcto", "codigo": 1, "mensaje": "Usuario Registrado con exito"})
    else:
        return jsonify({"estado": "error", "codigo": 0, "mensaje": "Hubo un problema con el registro"})

#Enpoint para eliminar empleados
@empleados_bp.route("/eliminar/<int:id>", methods=["DELETE"])
def delete_empleado(id):
    result = modelos_empleados.eliminar_empleado(id)

    if result == 2:
        return jsonify({"estado": "error", "codigo": 2, "mensaje": "El usuario no existe"})
    elif result == 0:
        return jsonify({"estado": "error", "codigo": 0, "mensaje": "Hubo un problema al eliminar"})
    else:
        return jsonify({"estado": "correcto", "codigo": 1, "mensaje": "Usuario Eliminado"})
