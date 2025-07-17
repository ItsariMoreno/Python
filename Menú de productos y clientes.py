Clientes={"CL001": ["Laura Díaz", 25], "CL002": ["Benjamin Fernandez", 25]}
Productos={"CL001":["Poleron GAP", 24000, 10], "CL002":["polera", 14000, 10]}
#diccionario= {key : dato} dato puede ser una lista, se llamaria por posicion en la lista   
# Key es el nombre asignado 

def ingresar_cliente(): #Busca que el cliente no esté registrado, si no está usa def registrar
    while True:
        try:
            nombre=input("Ingrese nombre del cliente: ").strip() #strip elimina el espacio al inicio y final (deja el intermedio)
            if " " not in nombre: #si no hay espacio (para validar que ingresó tmb apellido)
                print("Debe ingresar un nombre y apellido")
                continue
            else:
                for key, cliente in Clientes.items(): #Revisa los diccionarios BUSCAR PRODUCTO
                    if cliente[0].title()==nombre.title(): #busca coincidencia entre el diccioario y el nombre|| title sirve para poner mayuscula las iniciales de cada palabra
                        print(f"El cliente ya existe {cliente[0]} codigo {key}")
                        return key,cliente[0] #retorna el codigo y el nombre del cliente
                    
                print("Usuario no encontrado...Registrando cliente")
                codigo= registrar_clientes(nombre) #este es un definir anidado, pedimos los datos y eso llama a otro def que da el codigo
                try:
                            producto=input("Ingrese el nombre del producto: ")
                            registrar_productos(producto,codigo)
                            return key, cliente
                except ValueError:
                            print("Por favor ingrese un nombre valido")

        except ValueError:
            print("Por favor ingrese un nombre valido")

def registrar_clientes(nombre): #Registra el cliente en el diccionario cliente
    try:
        edad=int(input("ingrese su edad: "))
        codigo=crear_Codigo(nombre,edad) 
        Clientes[codigo] =[nombre.title(), edad] #guardar en el diccionario
        print(nombre, "Su codigo de usuario es: ", codigo)
        return codigo
    except ValueError:
        print("Ingrese una edad válida")
        return

def registrar_productos(producto, codigo): #Registra el producto en el diccionario productos
    while True:
        try:
            total=int(input("Ingrese el valor del producto: "))
            descuento=int(input("Ingrese el descuento del producto: "))
            if total <0 or descuento <0: #para evitar numeros negativos
                print("Ingrese un valor válido")
                continue
            else:
                Productos[codigo]=[producto.title(), total, descuento] #guardar los productos en el diccionario 
                return(f"El producto: {producto} de valor: $ {total} y descuento de: $ {descuento} ha sido guardado en el codigo: {codigo}") #retorna en pantalla lo refistrado
        except ValueError:
            print("Ingrese valores validos")
            
 ################################################ DEF DE SOPORTE #############################################################3

def crear_Codigo(nombre, edad): #Crea el codigo para la lib, registrar cliente y retorna el codigo creado para usarlo en reg, producto
    codigo=nombre[0] + nombre[1] + "00" + str(edad)
    codigo=codigo.upper() ##############    LUEGO ELIMINAR ES PARA COMPROBAR QUE FUNCIONA BIEN
    return codigo

def mostrar_datos_clientes (codigo): #Busca el codigo del cliente en su diccionario y retorna su nombre y edad
    for cliente, datos in Clientes.items():
        if codigo in cliente: 
            print("Los datos del cliente son: ")
            return print(f"Codigo: {cliente} || Nombre: {datos[0]} || Edad: {datos[1]}")
    return("Cliente no encontrado")

    
def mostrar_datos_productos(codigo): #Busca el codigo del producto en su diccionario y retorna el producto
    for productos,datos in Productos.items():
        if codigo in productos:
            print("El producto del cliente son: ")
            valorF= datos[1] - (datos[1]* datos[2] /100)
            print(f"Producto: {datos[0]}|| Precio Bruto: ${datos[1]} || Descuento: {datos[2]}% || Valor Final:${round(valorF)} ")
    return("Cliente sin productos")
########################################## DEF PARA EL RESTO DE OPCIONES ############################################################3
def opcion_3(): #encontrar producto a partir del total bruto
    while True:
        try:
            total_bruto=int(input("Ingrese el total bruto del producto (sin punto): "))
            if total_bruto < 0:
                raise ValueError
            else:
                encontrar= False
                for productos, datos in Productos.items():
                    if total_bruto in datos:
                        print("El producto del cliente son: ")
                        valorF= datos[1] - (datos[1]* datos[2] /100)
                        print(f"codigo de cliente: {productos} || Producto: {datos[0]}|| Precio Bruto: ${datos[1]} || Descuento: {datos[2]}% || Valor Final:${round(valorF)} ") 
                        encontrar=True
                if not encontrar:
                        print("Producto no encontrado")
                        break
                return
        except ValueError:
            print("Ingrese un digito valido")

def opcion_4():#encontrar producto por edad (sigo sorprendida de que realmente pida esto pero ok)
    while True:
        try:
            edad=int(input("ingrese la edad del cliente: "))
            if edad < 0:
                raise ValueError
            else:
                encontrar=False
                for clientes,datos in Clientes.items():
                    if edad in datos:
                       codigo= clientes
                       print(f"Cliente de codigo: {codigo} || nombre {datos[0]}")
                       mostrar_datos_productos(codigo)  #if edad in datos e hace NO es buscar exclusivamente por el codigo si no que busca
                       encontrar=True                   #en todas las listas hasta encontrar algo que coincida, por eso si encuentra algo que
                if not encontrar:                       #coincide devuelve el codigo y es por eso que podemos buscar luego en la otra libreria 
                    print("Producto no encontrado")     #con "def mostrar datos producto" a partir del codigo 
                    break
                return               
        except ValueError:
            print("Ingrese un digito valido")

def opcion_5():#encontrar cliente por total bruto
        while True:
            try:
                total_bruto=int(input("Ingrese el total bruto del producto (sin punto): "))
                if total_bruto < 0:
                    raise ValueError
                else:
                    encontrar=False
                    for clientes,datos in Productos.items():
                        if total_bruto in datos:
                            codigo= clientes   
                            print(f"Cliente de codigo: {codigo} || con un total bruto de: ${datos[1]}")
                            mostrar_datos_clientes(codigo)  
                            encontrar=True
                    if not encontrar:
                        print("Producto no encontrado")
                        break
                    return
            except ValueError:
             print("Ingrese un digito valido")

def main ():
    while True:
            print("\n Menú \n")
            print("1.- Comprar producto")
            print("2.- Mostrar datos cliente")
            print("3.- Filtrar Compras por Total Bruto")
            print("4.- Filtrar Compra por edad")
            print("5.- Filtrar Cliente por Total Bruto")
            print("6.- Monstrar todo el inventario y clientes")
            print("7.- Salir")
            print("")
            try:
                opcion=int(input("Ingrese la opcion que desea: ")) #opción no es necesario declararlo (opcion=0) pq solo pedimos numeros
                match opcion: #match conviene más en este caso especifico al ser numeros, cualquier otra opcion arrojará a _ (letras incluidas en el caso de que opcion no tenga int arriba)
                    case 1:
                        ingresar_cliente() #debe pedir nombre, buscar codigo, si no existe codigo registrar un cliente
                    case 2:
                        try:
                            codigo=input("Ingrese el codigo del usuario que desea buscar: ").strip().upper()

                            if len(codigo) > 6 or len(codigo) <5: #comprueba que tenga la cantidad de numeros adecuados
                                raise ValueError #devuelve el error except
                            else:
                                mostrar_datos_clientes(codigo)
                                mostrar_datos_productos(codigo)
                        except ValueError:
                            print("Ingrese un valor valido")
                    case 3:
                        opcion_3() 
                    case 4:
                        opcion_4() 
                    case 5:
                        opcion_5() 
                    case 6: #esta opción es solo para ver el inventario general para saber si ingresó bien el nuevo usuario y producto 
                        for key, datos in Clientes.items():
                            print("clientes")
                            print(f" Cliente: {key} || Nombre: {datos[0]} || Edad: {datos[1]}")
                        for key,datos in Productos.items():    
                            print("producto")
                            print(f" Cliente: {key} || Producto: {datos[0]} || valor bruto: {datos[1]} || Descuento: {datos[2]} ")    
                    case 7:
                        print("Adiós"); break
                    
                    case _:
                        print("Opción no valida, ingrese una existente")
                        continue
            except ValueError:
                print("Solo ingrese una de las opciones disponibles")
main()