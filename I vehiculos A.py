import datetime

Vehiculos = {}

def validar_patente(patente):
    if len(patente) != 6:
        print("❌ La patente debe tener exactamente 6 caracteres.")
        return False
    letras = sum(1 for c in patente if c.isalpha() and c.isupper())
    numeros = sum(1 for c in patente if c.isdigit())
    if letras != 4 or numeros != 2:
        print("❌ La patente debe tener 4 letras mayúsculas y 2 números.")
        return False
    return True

def validar_sexo(sexo):
    if sexo.upper() not in ["M", "F"]:
        print("❌ Sexo inválido. Debe ser 'M' o 'F'.")
        return False
    return True

def registrar_vehiculo():
    while True:
        patente = input("Ingrese la patente (6 caracteres, 4 letras mayúsculas y 2 números): ").upper()
        if not validar_patente(patente):
            continue
        if patente in Vehiculos:
            print("❌ Esta patente ya está registrada.")
            continue
        break

    nombre = input("Ingrese el nombre del dueño: ").title()

    while True:
        sexo = input("Ingrese el sexo del dueño (M/F): ").upper()
        if validar_sexo(sexo):
            break

    marca = input("Ingrese la marca del vehículo: ").title()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    Vehiculos[patente] = [nombre, sexo, marca, fecha]
    print("✅ Vehículo registrado con éxito.")

def eliminar_vehiculo():
    patente = input("Ingrese la patente del vehículo a eliminar: ").upper()
    if patente in Vehiculos:
        del Vehiculos[patente]
        print("✅ Vehículo eliminado.")
    else:
        print("❌ No se encontró un vehículo con esa patente.")

def mostrar_todos():
    if not Vehiculos:
        print("No hay vehículos registrados.")
        return
    print("\n=== Vehículos Registrados ===")
    for pat, datos in Vehiculos.items():
        print(f"Patente: {pat} || Dueño: {datos[0]} || Sexo: {datos[1]} || Marca: {datos[2]} || Fecha: {datos[3]}")

def filtrar_por_marca():
    marca = input("Ingrese la marca que desea buscar: ").title()
    encontrados = False
    for pat, datos in Vehiculos.items():
        if datos[2] == marca:
            print(f"Patente: {pat} || Dueño: {datos[0]} || Sexo: {datos[1]} || Marca: {datos[2]} || Fecha: {datos[3]}")
            encontrados = True
    if not encontrados:
        print("❌ No se encontraron vehículos con esa marca.")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Registrar vehículo")
    print("2. Eliminar vehículo por patente")
    print("3. Mostrar todos los vehículos registrados")
    print("4. Filtrar vehículos por marca")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        registrar_vehiculo()
    elif opcion == "2":
        eliminar_vehiculo()
    elif opcion == "3":
        mostrar_todos()
    elif opcion == "4":
        filtrar_por_marca()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("❌ Opción inválida.")
