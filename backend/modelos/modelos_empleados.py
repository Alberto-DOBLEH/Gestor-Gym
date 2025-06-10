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
