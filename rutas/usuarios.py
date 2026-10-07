# rutas/usuarios.py
# Endpoints para registrar usuarios e iniciar sesion.

from flask import Blueprint, request, jsonify
from base_de_datos import guardar_usuario
from seguridad import hashear_contrasena, credenciales_validas

# Un Blueprint es como una "mini app" con sus propias rutas.
# Despues lo registramos en la app principal (servidor.py).
usuarios_bp = Blueprint("usuarios", __name__)


def leer_datos_del_json():
    # Lee el JSON que manda el cliente y saca el usuario y la contraseña.
    # Acepto "contraseña" (como pide la consigna) y tambien "contrasena"
    # por si la consola no permite escribir la ñ.
    datos = request.get_json(silent=True)
    if datos is None:
        return None, None

    usuario = datos.get("usuario")
    contrasena = datos.get("contraseña") or datos.get("contrasena")
    return usuario, contrasena


@usuarios_bp.route("/registro", methods=["POST"])
def registro():
    usuario, contrasena = leer_datos_del_json()

    # Valido que hayan mandado los dos datos
    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos. Enviar usuario y contraseña"}), 400

    # Hasheo la contraseña antes de guardarla
    contrasena_hash = hashear_contrasena(contrasena)

    if guardar_usuario(usuario, contrasena_hash):
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    else:
        return jsonify({"error": "El usuario ya existe"}), 409


@usuarios_bp.route("/login", methods=["POST"])
def login():
    usuario, contrasena = leer_datos_del_json()

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos. Enviar usuario y contraseña"}), 400

    if credenciales_validas(usuario, contrasena):
        return jsonify({"mensaje": "Login exitoso. Bienvenido " + usuario}), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401
