from flask import Flask, request, Blueprint, jsonify
from modelos import modelos_clientes

clientes_bp = Blueprint('clientes', __name__)

#Endpoint para agregar clientes
@clientes_bp.route("/agregar/", methods=["POST"])
def add_clientes():
    data = request.get_json()

    nombre  = data.get("nombre")
    primer_apellido = data.get("primer_apellido")
    segundo_apellido = data.get("segundo_apellido")
    numero_telefono = data.get("numero_telefono")

    resultado = modelos_clientes.agregar_cliente(nombre, primer_apellido, segundo_apellido, numero_telefono)

    if resultado == 0:
        return jsonify({"estado": "error", "codigo": 0, "mensaje": "hubo un error al agregar el cliente"})

    return jsonify({"estado": "correcto", "codigo": 1, "mensaje": "cliente agregado con exito"})

#Enpoint para eliminar clientes
@clientes_bp.route("/eliminar/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    result = modelos_clientes.eliminar_cliente(id)

    if result == 2:
        return jsonify({"estado": "error", "codigo": 2, "mensaje": "El cliente no existe"})
    elif result == 0:
        return jsonify({"estado": "error", "codigo": 0, "mensaje": "Hubo un problema al eliminar"})
    else:
        return jsonify({"estado": "correcto", "codigo": 1, "mensaje": "Cliente Eliminado"})

#Endpoint para obtener todos los clientes
@clientes_bp.route("/", methods=["GET"])
def get_clientes():
    resultados = []
    result = modelos_clientes.obtener_clientes()
    claves = ['id_cliente','nombre','primer_apellido','segundo_apellido', 'numero_telefono']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)

    return jsonify(resultados)


#Enpoint para obtener clientes por nombre
@clientes_bp.route("/<string:nombre>", methods=["GET"])
def get_clientes_nombre(nombre):
    resultados = []
    result = modelos_clientes.obtener_clientes_por_nombre(nombre)
    claves = ['id_cliente', 'nombre', 'primer_apellido', 'segundo_apellido', 'numero_telefono']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)

    return jsonify(resultados)

