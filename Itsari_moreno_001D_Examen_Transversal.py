#productos = {modelo: [marca, pantalla, RAM, disco (ssd (solido) o dd (mecanico)), GB de DD, procesador, video], ...]
productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {
'8475HD': [387990,10],
'2175HD': [327990,4],
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21],
'123FHD': [290890,32],
'342FHD': [444990,7],
'GF75HD': [749990,2],
'UWU131HD': [349990,1],
'FS1230HD': [249990,0],
}


def stock_marca(marca):
    encontrar=False
    i=0
    for key, values in productos.items():
        if marca.upper() in values[0].upper():
                buscar=key
                cantidad= mostrar_stock(buscar)
                if cantidad > 0 or cantidad is None:
                    i= i+ cantidad
                    encontrar=True
    print("El stock es:", i)
    if not encontrar:
         print("El stock es: 0")
         
                     
def mostrar_stock(buscar):
    cantidad=0
    for key, values in stock.items():
          if buscar == key:
                cantidad=values[1]
                return cantidad
  
               
            
def busqueda_precio(p_min, p_max):
    lista=[]

    for key, values in stock.items():
        precio=values[0]
        disponible=values[1]
        if p_min <= precio and p_max >= precio and disponible > 0 and key in productos:
           
               codigo= productos[key][0]
               lista.append((key,codigo))
               
    if lista:
          print("los notebooks entre los precios consultas son:")
          for key, datos in lista:
              print(f"{key} -- {datos}")
    else:
          print("no hay notebooks en ese rango de precios.")
          



def actualizar_precio(modelo, p):
    encontrar=False
    for key, values in stock.items():
          if modelo == key:
            stock[modelo][0]=p
            encontrar=True
            return True
    if not encontrar:
         return False


while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        try:
            opcion= int(input("Ingrese opción:"))
            match opcion:
                case 1:
                    try:
                        marca=input("Ingrese marca a consultar:")
                        stock_marca(marca)
                    except ValueError:
                        print("Error al ingresar marca, intente de nuevo")
                        pass  
                        
                case 2:
                    try:  
                        p_min=int(input("Ingrese precio mínimo:"))
                        p_max=int(input("Ingrese precio máximo:"))
                        if p_min < 0 or p_max < 0:
                            raise ValueError 
                        else:
                             busqueda_precio(p_min, p_max)
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                case 3:
                    while True:
                        try:
                            actualizar=False
                            modelo=input("Ingrese modelo a actualizar:")
                            p=int(input("Ingrese precio nuevo:"))
                            actualizar=actualizar_precio(modelo, p) 
                            if actualizar == True:
                                print("Precio actualizado!!")
                                break
                            elif actualizar== False:
                                print("El modelo no existe!!")
                                reintentar= input("Desea actualizar otro precio (s/n)?:").lower()
                                match reintentar:
                                    case "si":
                                        continue
                                    case "sí":
                                        continue
                                    case "no":
                                        break
                                    case _:
                                        print("Debe seleccionar una opción válida!!")
                        except ValueError:
                            print("Debe seleccionar una opción válida!!")
                case 4:
                        print("Programa finalizado.")
                        break 
                case _:
                    print("Debe seleccionar una opción válida!!")
        except ValueError:
            print("Debe seleccionar una opción válida!!")
