# rutas/tareas.py
# Endpoint de tareas, protegido con autenticacion basica (HTTP Basic Auth).

from flask import Blueprint, request, render_template
from seguridad import credenciales_validas

tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.route("/tareas", methods=["GET"])
def tareas():
    # El cliente manda el usuario y la contraseña en el encabezado "Authorization"
    auth = request.authorization

    if auth is None or not credenciales_validas(auth.username, auth.password):
        # Devuelvo 401 y el encabezado WWW-Authenticate para que
        # el navegador muestre la ventanita pidiendo usuario y contraseña
        return (
            "<h1>Acceso denegado</h1><p>Tenes que iniciar sesion.</p>",
            401,
            {"WWW-Authenticate": 'Basic realm="Tareas"'}
        )

    # render_template busca el archivo en la carpeta "templates"
    # y le pasa la variable "usuario" para que la muestre
    return render_template("tareas.html", usuario=auth.username), 200
