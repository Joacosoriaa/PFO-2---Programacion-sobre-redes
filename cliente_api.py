# cliente_api.py
# Funciones que se comunican con la API del servidor.
# No piden datos ni imprimen nada: solo hacen la peticion y devuelven la respuesta.

import requests
from config import HOST, PUERTO

URL = f"http://{HOST}:{PUERTO}"


def registrar(usuario, contrasena):
    datos = {"usuario": usuario, "contraseña": contrasena}
    return requests.post(URL + "/registro", json=datos)


def iniciar_sesion(usuario, contrasena):
    datos = {"usuario": usuario, "contraseña": contrasena}
    return requests.post(URL + "/login", json=datos)


def obtener_tareas(usuario, contrasena):
    # auth=(usuario, contraseña) hace que requests use autenticacion basica
    return requests.get(URL + "/tareas", auth=(usuario, contrasena))
