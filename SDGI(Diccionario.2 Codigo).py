Lista_Productos=[]
#producto={ "nombre":nombre,
#          "cantidad":stock,
#            "Precio": 1500,
#            "codigo": "Abc123"}  EJEMPLO

opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""

def contarMayusculas(codigo):
    contarMayusculas=0
    for letra in str(codigo):
        if letra.isupper()==True:
            contarMayusculas=contarMayusculas+1
    return contarMayusculas 

def contarNumeros(codigo):
    contarNumeros=0
    for numeros in str(codigo):
        if numeros.isnumeric()==True:
            contarNumeros+=1
    return contarNumeros


def ValidarCaracteres(codigo):
    if len(codigo) >= 5:
        return True
    else:
        return False

def ValidarCodigo(codigo):
    if contarMayusculas(codigo)>=2:
        if contarNumeros(codigo)>=1:
            if ValidarCaracteres==True:
                return True
            else:
                print("El codigo debe contener al menos 5 caracteres")
                return False
        else:
            print("El codigo debe tener al menos un numero")
            return False
    else:
        print("El codigo debe tener al menos dos mayusculas")
        return False
            

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ").lower()
    while True:
        codigo=input("Ingrese el código del producto")
        if ValidarCodigo(codigo)==True:
            print("El codigo es correcto")
            break
        else:
            print("El codigo es incorrecto")
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")
        
    
def guardarProducto(nombre,precio,stock):
    if producto == None:
        producto={"nombre": nombre, "cantidad": stock, "precio": precio}
        Lista_Productos.append(producto)
        return "Se guardado correctamente el producto"

    else: 
        return"Producto ya creado"
            
    
def buscarProducto(nombre):
    for producto in Lista_Productos:
        if producto ["nombre"]== nombre:
            return producto 
    return None

def actualizarProducto(nombre,nuevoPrecio,nuevoStock):
    producto_Encontrado= buscarProducto(nombre)
    if producto_Encontrado!= None:
        indice=Lista_Productos.index(producto_Encontrado)
        producto_Encontrado["cantidad"]= nuevoStock
        producto_Encontrado["precio"]=nuevoPrecio
        Lista_Productos[indice]=producto_Encontrado
        print("Producto Actualizado con éxito")

    else:
        print("No existe un producto con ese nombre")

def mostarInventarioCompleto():
    print("-"*60)
    if(len(Lista_Productos)==0):
        print("Aún no hay productos agregados")
        return

    for producto in Lista_Productos:
        
        print(f"Nombre: {producto["nombre"]} \t Precio: ${producto["precio"]} \t Stock: {producto["cantidad"]} unidades")
    
    print("-"*60)

def eliminar_producto(nombre):
    productoEncontrado=buscarProducto(nombre)
    if productoEncontrado!= None:
        Lista_Productos.remove(productoEncontrado)
        return True
    else:
        return False
        

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                #guardarProducto(*nuevoProducto)
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])

        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ").lower()
            productoEncontrado= buscarProducto(nombreProducto)

            if productoEncontrado !=  None:
                print(f"Nombre: {productoEncontrado["nombre"]} \t Precio: ${productoEncontrado["precio"]} \t Stock: {productoEncontrado["cantidad"]} unidades")
        case "3":

            print("*Ingrese los datos del producto a actualizar*")
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                actualizarProducto(*nuevoProducto) #entrega lo que contiene [] en forma numerica
        case "4":
            mostarInventarioCompleto()
        case "5":
            nombreProducto=input("Ingrese el nombre del producto a eliminar: ").lower()
            eliminar_producto(nombreProducto)
            if eliminar_producto(nombreProducto)== True:
                print("Eliminado")
            else:
                print("No se ha eliminado")
        case "6":
            print("Adios")
            break
               

