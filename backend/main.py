from flask import Flask

from rutas.clientes import clientes_bp
from rutas.empleados import empleados_bp

app = Flask(__name__)

#Registro BluePrintas
app.register_blueprint(empleados_bp, url_prefix="/empleados")
app.register_blueprint(clientes_bp, url_prefix="/clientes")


if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)