# seguridad.py
# Funciones para manejar contraseñas de forma segura.
# Usamos werkzeug, que viene instalado junto con Flask.

from werkzeug.security import generate_password_hash, check_password_hash
from base_de_datos import buscar_hash_usuario


def hashear_contrasena(contrasena):
    # Convierte la contraseña en un hash (con sal aleatoria).
    # Ejemplo: "1234" -> "scrypt:32768:8:1$...."
    return generate_password_hash(contrasena)


def credenciales_validas(usuario, contrasena):
    # Devuelve True si el usuario existe y la contraseña coincide con el hash
    hash_guardado = buscar_hash_usuario(usuario)
    if hash_guardado is None:
        return False
    return check_password_hash(hash_guardado, contrasena)
