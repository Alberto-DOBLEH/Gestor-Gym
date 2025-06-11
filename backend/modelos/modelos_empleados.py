from contextlib import nullcontext
from warnings import catch_warnings

from mysql.connector.constants import flag_is_set

from bd import conexion

def obtener_empleados():
    cnx = conexion()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleados")
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def obtener_empleado_porid(id):
    cnx = conexion()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", id)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def inicio_sesion(usuario, contraseña):
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT usuario, contraseña FROM empleados WHERE usuario = %s", usuario)
    serverdata = cursor.fetchone()

    if serverdata is None:
        return 2 # 2 es el caso de que no exista el usuario

    server_pass = serverdata[1]

    if contraseña != server_pass:
        return 3 # 3 es el caso de que no coincida la contraseña

    return 1 # 1 es el caso de que sea exitoso la verificacion







