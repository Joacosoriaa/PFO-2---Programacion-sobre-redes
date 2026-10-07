# servidor.py
# PFO 2 - Sistema de Gestion de Tareas con API y Base de Datos
# Este archivo solo arma la aplicacion y la pone en marcha.
# La logica esta repartida en los otros modulos:
#   config.py         -> configuracion
#   base_de_datos.py  -> SQLite
#   seguridad.py      -> hash de contraseñas
#   rutas/            -> endpoints de la API
#   templates/        -> paginas HTML

from flask import Flask
from config import HOST, PUERTO
from base_de_datos import crear_base_de_datos
from rutas.usuarios import usuarios_bp
from rutas.tareas import tareas_bp


def crear_app():
    app = Flask(__name__)

    # Para que los mensajes JSON muestren la ñ tal cual y no como ñ
    app.json.ensure_ascii = False

    # Registro los Blueprints (cada uno trae sus rutas)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(tareas_bp)

    return app


if __name__ == "__main__":
    crear_base_de_datos()
    app = crear_app()
    print(f"Servidor iniciado en http://{HOST}:{PUERTO}")
    app.run(host=HOST, port=PUERTO, debug=True)
