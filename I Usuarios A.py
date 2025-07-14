Usuarios = {
    "00000000-0": ["Usuario", "hotmail@gmail.com", "Contraseña321+"],
    "12345678-9": ["Usuario2", "correo@gmail.com", "Contraseña123+"]
}

import re

############## VALIDADORES ##############

def validar_rut(rut):
    return bool(re.match(r"^[0-9]{7,8}-[0-9kK]$", rut))

def validar_correo(correo):
    return correo.endswith(".com") or correo.endswith(".cl") and "@" in correo

def validar_usuario(usuario):
    return " " not in usuario and usuario.isalnum()

def validar_contrasena(contrasena):
    if " " in contrasena:
        print("La contraseña no debe contener espacios.")
        return False
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena) and
        any(c in "!#$%&'?\"()*+,-./:;<=>?@[\\]^_`{|}~" for c in contrasena)):
        return True
    print("Contraseña no cumple con los requisitos.")
    return False

############## SOLICITUDES ##############

def solicitar_dato_valido(mensaje, validador):
    while True:
        valor = input(mensaje)
        if validador(valor):
            return valor
        print("Dato inválido.")

def solicitar_contrasena():
    while True:
        contrasena = input("Ingrese una contraseña segura: ")
        if validar_contrasena(contrasena):
            return contrasena

############## FUNCIONES PRINCIPALES ##############

def registrar_usuario():
    rut = solicitar_dato_valido("Ingrese su RUT (formato XXXXXXXX-X): ", validar_rut)
    if rut in Usuarios:
        print("Este RUT ya está registrado.")
        return
    usuario = solicitar_dato_valido("Ingrese su nombre de usuario (sin espacios): ", validar_usuario)
    correo = solicitar_dato_valido("Ingrese su correo: ", validar_correo)
    contrasena = solicitar_contrasena()
    Usuarios[rut] = [usuario, correo, contrasena]
    print("Usuario registrado correctamente.")

def solicitar_dato():
    campo = input("¿Desea buscar por rut, usuario o correo?: ").lower()
    valor = input(f"Ingrese el {campo}: ")
    for rut, datos in Usuarios.items():
        if ((campo == "rut" and rut == valor) or
            (campo == "usuario" and datos[0] == valor) or
            (campo == "correo" and datos[1] == valor)):
            contrasena = solicitar_contrasena()
            if datos[2] == contrasena:
                print(f"Bienvenido: {datos[0]}\nRUT: {rut} | Usuario: {datos[0]} | Correo: {datos[1]} | Contraseña: {datos[2]}")
                return rut, datos
            else:
                print("Contraseña incorrecta.")
                return None
    print("Usuario no encontrado.")
    return None

def actualizar_datos():
    resultado = solicitar_dato()
    if not resultado:
        return
    rut, datos = resultado
    campo = input("¿Qué desea actualizar? (usuario/correo/contraseña/rut): ").lower()
    if campo == "usuario":
        nuevo = solicitar_dato_valido("Nuevo nombre de usuario: ", validar_usuario)
        datos[0] = nuevo
    elif campo == "correo":
        nuevo = solicitar_dato_valido("Nuevo correo: ", validar_correo)
        datos[1] = nuevo
    elif campo == "contraseña":
        datos[2] = solicitar_contrasena()
    elif campo == "rut":
        nuevo = solicitar_dato_valido("Nuevo RUT: ", validar_rut)
        Usuarios[nuevo] = datos
        del Usuarios[rut]
    else:
        print("Campo inválido.")
        return
    print("Datos actualizados correctamente.")

def eliminar_usuario():
    resultado = solicitar_dato()
    if not resultado:
        return
    rut, datos = resultado
    confirmar = input("¿Está seguro que desea eliminar este usuario? (si/no): ").lower()
    if confirmar == "si":
        del Usuarios[rut]
        print("Usuario eliminado correctamente.")

############## MENÚ ##############

def mostrar_usuarios():
    for rut, datos in Usuarios.items():
        print(f"RUT: {rut} | Usuario: {datos[0]} | Correo: {datos[1]} | Contraseña: {datos[2]}")

while True:
    print("""
===== MENÚ =====
1. Registrar Usuario
2. Ingresar Usuario
3. Modificar Datos
4. Eliminar Usuario
5. Mostrar Todos los Usuarios
6. Salir
================
""")
    opcion = input("Seleccione una opción: ")
    if opcion == "1": registrar_usuario()
    elif opcion == "2": solicitar_dato()
    elif opcion == "3": actualizar_datos()
    elif opcion == "4": eliminar_usuario()
    elif opcion == "5": mostrar_usuarios()
    elif opcion == "6": print("Adiós"); break
    else: print("Opción inválida.")
