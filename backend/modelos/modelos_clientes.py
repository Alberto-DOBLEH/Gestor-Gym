from bd import conexion

def agregar_cliente(nombre, primer_apellido, segundo_apellido, numero_telefono):
    cnx = conexion()
    cursor = cnx.cursor()

    command = "INSERT INTO clientes(nombre, primer_apellido, segundo_apellido, numero_telefono) VALUES (%s,%s,%s,%s)"
    data = (nombre, primer_apellido, segundo_apellido, numero_telefono)

    try:
        cursor.execute(command, data)
        cursor.close()
        cnx.close()
        return 1
    except:
        return 0

def eliminar_cliente(id):
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", id)
    server_data = cursor.fetchall()

    if server_data is None:
        cursor.close()
        cnx.close()
        return 2

    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", id)
        cursor.close()
        cnx.close()
        return 1
    except:
        cursor.close()
        cnx.close()
        return 0

def obtener_clientes():
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

def obtener_clientes_por_nombre(nombre):
    cnx = conexion()
    cursor = cnx.cursor()
    pattern = f"%{nombre}%"

    cursor.execute("SELECT * FROM clientes WHERE LOWER(nombre) LIKE LOWER(%s)", pattern)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    return data

