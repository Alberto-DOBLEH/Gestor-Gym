
from bd import conexion

def obtener_empleados():
    cnx = conexion()
    cursor = cnx.cursor()
    cursor.execute("SELECT e.id_empleado,e.nombre,e.primer_apellido,e.segundo_apellido,e.RFC,e.CURP,e.NSS,e.numero_telefono,te.nombre as 'Ocupacion' FROM empleados e JOIN tipo_empleado te ON e.tipo_empleado = te.id_tipo_empleado ")
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def obtener_empleado_porid(id):
    cnx = conexion()
    cursor = cnx.cursor()
    cursor.execute("SELECT e.id_empleado,e.nombre,e.primer_apellido,e.segundo_apellido,e.RFC,e.CURP,e.NSS,e.numero_telefono,te.nombre as 'Ocupacion' FROM empleados e JOIN tipo_empleado te ON e.tipo_empleado = te.id_tipo_empleado WHERE e.id_empleado = %s", id)
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
        cursor.close()
        cnx.close()
        return 2 # 2 es el caso de que no exista el usuario

    server_pass = serverdata[1]

    if contraseña != server_pass:
        cursor.close()
        cnx.close()
        return 3 # 3 es el caso de que no coincida la contraseña

    cursor.close()
    cnx.close()
    return 1 # 1 es el caso de que sea exitoso la verificacion

def agregar_empleado(nombre, primero_apellido, segundo_apellido, RFC, CURP, NSS, numero_telefono, tipo_empleado, usuario, contraseña):
    cnx = conexion()
    cursor = cnx.cursor()

    comand = "INSERT INTO empleados(nombre, primer_apellido, segundo_apellido, RFC, CURP, NSS, numero_telefono, tipo_empleado, usuario, contraseña) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = [nombre, primero_apellido, segundo_apellido, RFC, CURP, NSS, numero_telefono, tipo_empleado, usuario, contraseña]

    try:
        cursor.execute(comand, data)
        cursor.close()
        cnx.close()
        return 1
    except:
        cursor.close()
        cnx.close()
        return 0

def eliminar_empleado(id):
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", id)
    server_data = cursor.fetchall()

    if server_data is None:
        cursor.close()
        cnx.close()
        return 2

    try:
        cursor.execute("DELETE FROM empleados WHERE id_empleado = %s", id)
        cursor.close()
        cnx.close()
        return 1
    except:
        cursor.close()
        cnx.close()
        return 0

def obtener_empleado_por_username(username):
    cnx = conexion()
    cursor = cnx.cursor()
    cursor.execute("SELECT e.id_empleado,e.nombre,e.primer_apellido,e.segundo_apellido,e.RFC,e.CURP,e.NSS,e.numero_telefono,te.nombre as 'Ocupacion' FROM empleados e JOIN tipo_empleado te ON e.tipo_empleado = te.id_tipo_empleado WHERE e.usuario = %s", username)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data