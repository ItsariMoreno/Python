# CASO IV ayuda
nombre = input("Por favor, ingrese sus datos: \nNombre: ")
while True:
    rut = input("Rut (Con puntos y guión): ")
    if all (c.isdigit() or c in ["k", ".", "-"] for c in rut):
        print("El rut es válido.")
        break
    else:
        print("Error, debe ingresar RUT con puntos y guión.")

while True:
    correo = input("Correo: ")
    if "@" in correo and (correo.endswith(".com") or correo.endswith(".cl")):
        print("El correo ingresado es válido.")
        break
    else:
        print("Correo inválido, ingrese nuevamente.")

telefono = int(input("Teléfono: "))

print (f"NOMBRE:\t {nombre}.\nRUT:\t {rut}\nCORREO:\t {correo}\nTELÉFONO:\t {telefono}")