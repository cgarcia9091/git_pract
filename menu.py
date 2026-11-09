usuarios = {
    "belu": "belu",
    "admin": "admin"
}

usuario_logueado = None


def mostrar_menu():
    print("\nMENU DE OPCIONES")
    print("Sistema de usuarios")
    print("1 - Registrarse")
    print("2 - Loguearse")
    print("3 - Mostrar usuarios")
    print("4 - Salir")


def registrar_usuario():
    print("\nREGISTRO DE USUARIOS")

    nuevo_usuario = input("Ingrese un nombre de usuario: ")

    if nuevo_usuario in usuarios:
        print("El usuario ya existe")
        return

    nueva_contraseña = input("Ingrese una contraseña: ")

    usuarios[nuevo_usuario] = nueva_contraseña

    print("Usuario registrado correctamente")


def iniciar_sesion():
    global usuario_logueado

    print("\nINICIAR SESION")

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario not in usuarios:
        print("El usuario no existe")
        return

    if usuarios[usuario] != contraseña:
        print("Credenciales incorrectas")
        return

    usuario_logueado = usuario
    print(f"Inicio de sesion exitoso. Bienvenido {usuario}")


def mostrar_usuarios():
    print("\nMOSTRAR USUARIOS")

    for usuario in usuarios:
        print("-", usuario)


def main():
    while True:
        mostrar_menu()

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            iniciar_sesion()

        elif opcion == "3":
            mostrar_usuarios()

        elif opcion == "4":
            print("Saliendo del menu...")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


main()

print("Fin del programa")
