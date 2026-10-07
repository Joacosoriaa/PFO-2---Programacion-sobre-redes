# cliente.py
# Cliente de consola para probar la API del servidor.
# Antes de usarlo hay que tener corriendo servidor.py
# Este archivo solo maneja el menu; las peticiones estan en cliente_api.py

import requests
import cliente_api

# Aca guardo los datos del usuario cuando hace login
sesion = {"usuario": None, "contrasena": None}


def mostrar_respuesta(respuesta):
    print("Codigo:", respuesta.status_code)
    print("Respuesta:", respuesta.json())


def opcion_registrar():
    usuario = input("Nuevo usuario: ")
    contrasena = input("Contraseña: ")
    respuesta = cliente_api.registrar(usuario, contrasena)
    mostrar_respuesta(respuesta)


def opcion_iniciar_sesion():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    respuesta = cliente_api.iniciar_sesion(usuario, contrasena)
    mostrar_respuesta(respuesta)

    # Si el login salio bien, me guardo los datos para usar en /tareas
    if respuesta.status_code == 200:
        sesion["usuario"] = usuario
        sesion["contrasena"] = contrasena


def opcion_ver_tareas():
    if sesion["usuario"] is None:
        print("Primero tenes que iniciar sesion (opcion 2).")
        return

    respuesta = cliente_api.obtener_tareas(sesion["usuario"], sesion["contrasena"])
    print("Codigo:", respuesta.status_code)
    print("HTML recibido:")
    print(respuesta.text)


def menu():
    while True:
        print()
        print("===== GESTION DE TAREAS =====")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Ver tareas")
        print("4. Salir")
        opcion = input("Elegi una opcion: ")

        try:
            if opcion == "1":
                opcion_registrar()
            elif opcion == "2":
                opcion_iniciar_sesion()
            elif opcion == "3":
                opcion_ver_tareas()
            elif opcion == "4":
                print("Chau!")
                break
            else:
                print("Opcion invalida")
        except requests.exceptions.ConnectionError:
            print("No se pudo conectar con el servidor. ¿Esta corriendo servidor.py?")


if __name__ == "__main__":
    menu()
