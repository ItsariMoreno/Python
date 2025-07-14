# Descripción: Un sistema simple para administrar productos (nombre, cantidad, precio).

# Acciones del menú:

# Agregar producto
# Buscar producto
# Actualizar cantidad/precio
# Mostrar inventario completo
# Eliminar producto
# Salir


# Debe considerar el uso de ciclos para que el sistema se ejecute hasta que el usuario desee salir y el uso de try-except para evitar que se produzcan errores que puedan llevar a que se caiga el programa.

# La opción de mostrar el inventario debe mostrar el nombre del producto y la cantidad de stock que este tiene.

# Retos adicionales:

# Calcular el valor total del inventario.
# Notificar si un producto está agotado.

productos = []

def menu():
    print("*"*70)
    print("1) Agregar producto")
    print("2) Buscar producto")
    print("3) Actualizar cantidad/precio")
    print("4) Mostrar inventario completo")
    print("5) Eliminar producto")
    print("6) Salir")
    opc = input("Ingres opcion: ")
    print("*"*70)
    return opc

def agregar():
    nombre   = input("Ingrese nombre  : ")
    cantidad = int(input("Ingrese cantidad: "))
    precio   = int(input("Ingrese precio  : "))
    productos.append({"nombre":nombre,"cantidad": cantidad,"precio": precio})
    print("Datos agregados a la lista!.")

def buscar():
    if len(productos) == 0:
        print("Error, no hay productos en inventario!.")
        return
    buscado = input("Ingrese nombre producto: ")
    for producto in productos:
        if producto["nombre"] == buscado:
            print(f"Nombre  : {producto["nombre"]}")
            print(f"Cantidad: {producto["cantidad"]}")
            print(f"Precio  : {producto["precio"]}")
            break
    else:
        print("Error, Producto no encontrado!.")

def actualizar():
    if len(productos) == 0:
        print("Error, no hay productos en inventario!.")
        return
    buscado = input("Ingrese nombre producto: ")
    for producto in productos:
        if producto["nombre"] == buscado:
            cantidad = int(input("Ingrese cantidad: "))
            precio   = int(input("Ingrese precio  : "))
            producto["precio"] = precio
            producto["cantidad"] = cantidad
            print("Producto actualizado!.")
            break
    else:
        print("Error, Producto no encontrado!.")

while True:
    opc = menu()
    if opc == "1":
        agregar()
    elif opc == "2":
        buscar()
    elif opc == "3":
        actualizar()
    elif opc == "4":
        print("")
    elif opc == "5":
        print("")
    elif opc == "6":
        print("")
    else:
        print("Opción no válida!.")


