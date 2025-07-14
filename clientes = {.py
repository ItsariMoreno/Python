clientes = {
    "EL0022": ["elias miranda", 22],
    "LE0026": ["leslie williams", 26],
    "SA0030": ["sani trevlok", 30],
    "MI0019": ["mira elsen", 19],
    "JO0045": ["joran feks", 45]
}
#diccionario= {key : dato} dato puede ser una lista, se llamaria por posicion en la lista   
# Key es el nombre asignado 

compras = {
    "EL0022": ["poleron chiporro", 24000, 10],
    "LE0026": ["zapatillas urbanas", 37990, 5],
    "SA0030": ["chaqueta impermeable", 42990, 8],
    "MI0019": ["mochila escolar", 19990, 12],
    "JO0045": ["pantalón trekking", 28990, 7]
}  
    
def buscarCliente():
    while True:
        nombre=input("Ingrese su nombre: ")
        nombre.title()
        key=BuscarCodigo(nombre) #buscarCodigo le envía nombre al def buscarCodigo 
                                    #(como enviarte una foto de wsp a ti misma)
                                    #Si todo está correcto te devolverá el contenido en "codigo"
        if key == None: #si codigo no es encontrado (None) pedirá los datos para registrar
                #tienes dos posibilidades, registrar aqui o pedir que registren
                key=registrarClientes(nombre) #opcion 1, registra aqui mismo
                #print("Usuario no encontrado, por favor creelo antes de proceder") || opcion 2, retornaria al menú sin guardar nada
                return key
        elif key == clientes: #Clientes es el diccionario
            print("Usuario ya existente")
            continue
            

def BuscarCodigo(nombre):
    for key in clientes:
        if str(clientes[key][0].upper()==str(nombre).upper):
            return key #key puede llevar otro nombre y al estar asignado arriba (linea 21) en codigo, este dato será otorgado a esa variable
                        #por esa razón no se superpone al return de registrar clientes 

def registrarClientes(nombre): #se pone nombre porque asi recibe lo enviado anteriormente en el parentesis
    while True:
        try:
            edad=int(input("ingrese su edad"))
            if edad.isnumeric()==True and edad>0: #comprueba que sean numeros y que sean positivos
                key=nombre[0]+nombre[1]+"00"+str(edad) #crea el codigo a partir de las dos primeras letras del nombre, 00 y la edad 
                print(key) #Solo para comprobar como se registró, al acabar codigo se puede eliminar
                clientes[key]=[nombre, edad] #guarda los datos en el diccionario
                return key #retorna el diccionario (sin esto cuando sales de la funcion no se guardarían los datos y se eliminarían)
            else:  
                raise ("Error al ingresar edad") #cualquier otra cosa da error
                                                 #raise es para tu generar un error especifico, except es generado "automatico"
        except TypeError:
            print("ingrese una opcion valida")
        

def registrarCompra(): #Esta función contiene registrar cliente y registrar compra
    try:
        key= buscarCliente()
        nombreProducto=input("ingrese nombre producto: ")
        totalbruto= input("ingrese ttal precio bruto: ")
        descuento=input("ingrese descuento")
        nombreProducto.title()
        compras[key]=[nombreProducto,totalbruto,descuento]  
    except ValueError:
        print("Error al ingresar datos")
    

def FiltrarCompra(): #filtra por producto
    try:
        BuscarProducto=input("Ingrese el producto que desea buscar: ")
        BuscarProducto.title()
        Encontrar = False  
        for datos in compras.items(): #hace que busque los datos en todo el diccionario (item hace que busque en todo e contenido y no solo en key)
            if datos[0] == BuscarProducto: #0 es la pocision de producto
                print(" ")
                print(f"Producto: {datos[0]} || valor bruto: {datos[1]} || Descuento: {datos[2]} ")
                Encontrar = True #hace que se detenga cuando encontró el producto 
            if not Encontrar:
                print("No se ha encontrado producto")
    except ValueError:
        print("error al ingresar el producto")


def FiltrarPrecio(): #filtra por producto
    try:
        BuscarProducto=int(input("Ingrese el precio producto que desea buscar: "))
        Encontrar = False  
        for key,datos in compras.items(): #hace que busque los datos en todo el diccionario (item hace que busque en todo e contenido y no solo en key)
            if datos[1] == BuscarProducto and BuscarCodigo.isnumeric(): #0 es la pocision de producto
                print(" ")
                print(f" Cliente: {key} || Producto: {datos[0]} || valor bruto: {datos[1]} || Descuento: {datos[2]} ")
                Encontrar = True #hace que se detenga cuando encontró el producto 
            if not Encontrar:
                print("No se ha encontrado producto")
    except ValueError:
        print("error al ingresar el producto")




while True:
        print("")
        print("===MENU===")
        print("1.- comprar producto")
        print("2.- registrar datos cliente")
        print("3.- filtrar compra por total bruto")
        print("4.- filtrar compra por producto")
        print("5.- salir")
        print(" ")
        try:
            opcion=int(input("Ingrese una opción: ")) #opción no es necesario declararlo si lo haces con int
            match opcion: #match conviene más en este caso especifico al ser numeros, cualquier otra opcion arrojará a _
                case 1:
                    buscarCliente()
                    registrarCompra()
                case 2:
                    buscarCliente()
                    registrarClientes()

                case 3:
                    FiltrarPrecio()
                case 4:
                    FiltrarCompra()
                case 5:
                    print("Adios")
                    break
                case 6: #esta opción es solo para ver el inventario general
                        #para saber si ingresó bien el nuevo usuario y producto
                    for key, datos in clientes.items():
                        print("clientes")
                        print(f" Cliente: {key} || Nombre: {datos[0]} || Edad: {datos[1]}")
                    for key,datos in compras.items():    
                        print("producto")
                        print(f" Cliente: {key} || Producto: {datos[0]} || valor bruto: {datos[1]} || Descuento: {datos[2]} ")
                case _:
                    print("Opción no existente  ")
        except ValueError:
            print("Solo ingrese una de las opciones disponibles")
        
