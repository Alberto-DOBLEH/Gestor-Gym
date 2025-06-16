from bd import conexion


def obtener_membresias():
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT m.id_membresia,e.nombre as 'empleado',tm.nombre as 'tipo_membresia',c.nombre as 'cliente', m.inicio_membresia, m.final_membresia,m.estatus FROM membresias m JOIN empleados e ON m.id_empleado = e.id_empleado JOIN tipo_membresia tm ON m.tipo_membresia = tm.id_tipo_membresia JOIN clientes c ON m.id_cliente = c.id_cliente ")
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def obtener_membresias_nombre(nombre):
    cnx = conexion()
    cursor = cnx.cursor()

    command = "SELECT m.id_membresia,e.nombre as 'empleado',tm.nombre as 'tipo_membresia',c.nombre as 'cliente', m.inicio_membresia, m.final_membresia,m.estatus FROM membresias m JOIN empleados e ON m.id_empleado = e.id_empleado JOIN tipo_membresia tm ON m.tipo_membresia = tm.id_tipo_membresia JOIN clientes c ON m.id_cliente = c.id_cliente WHERE LOWER(c.nombre) LIKE LOWER(%s)"
    pattern = f"%{nombre}%"

    cursor.execute(command, pattern)

    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def agregar_membresia(id_empleado, id_cliente, tipo_membresia, estatus, inicio_membresia, final_membresia):
    cnx = conexion()
    cursor = cnx.cursor()

    command = """
    INSERT INTO membresias(
    id_membresia,
    id_empleado,
    id_cliente,
    tipo_membresia,
    estatus,
    inicio_membresia,
    final_membresia)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """

    data = [id_empleado, id_cliente, tipo_membresia, estatus, inicio_membresia, final_membresia]

    try:
        cursor.execute(command, data)
        cursor.close()
        cnx.close()
        return 1
    except:
        cursor.close()
        cnx.close()
        return 0
