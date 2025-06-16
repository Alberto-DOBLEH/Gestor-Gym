from flask import Flask, request, Blueprint, jsonify
from modelos import modelos_membresias

membresias_bp = Blueprint('membresias', __name__)

# Enpoint para obtener todas las membresias
@membresias_bp.route("/", methods=["GET"])
def get_membresias():
    resultados = []
    result = modelos_membresias.obtener_membresias()
    claves = ['id_membresia','empleado','tipo_membresia','cliente','incio_membresia','final_membresia','estatus']
    for objetos in result:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        resultados.append(list2dic)

    return jsonify(resultados)


# Enpoint para obtener membresia por nombre
@membresias_bp.route("/<string:nombre>", methods=["GET"])
def get_membresias_nombre(nombre):
    resultados = []
    result = modelos_membresias.obtener_membresias_nombre(nombre)
    claves = ['id_membresia','empleado','tipo_membresia','cliente','incio_membresia','final_membresia','estatus']
    for objetos in result:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        resultados.append(list2dic)

    return jsonify(resultados)

#Enpoint para registrar empleados
@membresias_bp.route("/agregar/",methods=["POST"])
def add_membresias():
    data = request.get_json()

    id_empleado = data.get("id_empleado")
    id_cliente = data.get("id_cliente")
    tipo_membresia = data.get("tipo_membresia")
    estatus = data.get("estatus")
    inicio_membresia = data.get("inicio_membresia")
    final_membresia = data.get("final_membresia")


    resultado = modelos_membresias.agregar_membresia(id_empleado, id_cliente, tipo_membresia, estatus, inicio_membresia, final_membresia)

    if resultado == 1:
        return jsonify({"estado": "correcto", "codigo": 1, "mensaje": "Usuario Registrado con exito"})
    else:
        return jsonify({"estado": "error", "codigo": 0, "mensaje": "Hubo un problema con el registro"})