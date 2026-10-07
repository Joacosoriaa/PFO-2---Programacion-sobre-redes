# base_de_datos.py
# Todo lo que tiene que ver con SQLite esta en este archivo.
# El resto del programa no escribe SQL, solo llama a estas funciones.

import sqlite3
from config import BASE_DE_DATOS


def conectar():
    # Abre una conexion con el archivo de SQLite
    conexion = sqlite3.connect(BASE_DE_DATOS)
    return conexion


def crear_base_de_datos():
    # Crea la tabla de usuarios si todavia no existe.
    # OJO: no guardamos la contraseña, guardamos su hash.
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena_hash TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


def guardar_usuario(usuario, contrasena_hash):
    # Guarda un usuario nuevo.
    # Devuelve True si se guardo, o False si el usuario ya existia.
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        # Uso "?" para pasar los datos y evitar inyeccion SQL
        cursor.execute(
            "INSERT INTO usuarios (usuario, contrasena_hash) VALUES (?, ?)",
            (usuario, contrasena_hash)
        )
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        # Salta este error si el usuario ya existe (columna UNIQUE)
        return False
    finally:
        # finally se ejecuta siempre, haya error o no
        conexion.close()


def buscar_hash_usuario(usuario):
    # Devuelve el hash de la contraseña del usuario, o None si no existe
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT contrasena_hash FROM usuarios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    conexion.close()

    if fila is None:
        return None
    return fila[0]
