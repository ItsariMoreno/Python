Vehiculos={"ABCD12": ["Chris Ibarra","M","Toyota"],
           "ABCD13": ["Monse Nuñez", "F", "Kia"],
           "ABCD14":["Marita Flores", "F", "Toyota"]}
#Vehiculos={ "patente":["nombre_dueño","sexo_dueño","marca_vehiculo","Fecha_registro"]}


def validar_patente():
    while True:
        patente=input("Ingrese la patente del vehiculo: ")
       #patente.upper()
        if cantidad_caracteres(patente) == True:
            if cantidad_numeros(patente)==True:
                if validar_mayusculas(patente)==True:
                        
                        return patente 
        else:
            continue

def cantidad_caracteres(patente):
    if len(patente)==6:
        return True
    else:
        print("La patente no cumple la cantidad de caracteres solicitada")
        
def cantidad_numeros(patente):
    contar_numeros=0
    for numeros in str(patente):
        if numeros.isnumeric()==True:
            contar_numeros=contar_numeros+1
    if contar_numeros ==2:
        return True
    else:
        print("Cantidad de números invalida")
                  
def validar_mayusculas(patente):
    contar_mayusculas=0
    for mayusculas in str(patente):
        if mayusculas.isupper()==True:
            contar_mayusculas=contar_mayusculas+1
    if contar_mayusculas==4:
        return True
    else:
        print("No cumple con la cantidad de mayusculas")

def ingresar_datos():
    patente=validar_patente()
    nombre=validar_nombre()
    sexo=validar_sexo()
    modelo=validar_modelo()
    Vehiculos[patente]=[nombre,sexo,modelo]
    return Vehiculos

def validar_sexo():
    while True:
        sexo=input("Ingrese su sexo [M/F]: ")
        Mf="MF"
        for genero in str(sexo.upper()):
            if genero in Mf:
                return sexo
            else:
                print("Sexo no válido")
                continue
        
def validar_modelo():
    while True:
        try: 
            modelo=input("Ingrese la modelo del vehiculo: ")
            if str(modelo).isalpha():
                print("Marca valida")
                modelo.title()
                return modelo
            else:
                print("Modelo invalida, ingrese nuevamente por favor")
        except TypeError:
            print("Error al ingresar vehiculo")

def validar_nombre():
    while True:
        try:
            nombre=input("Ingrese su nombre y apellido: ")
            nombre.strip()
            if  all(caracter.isalpha() or  caracter==" " for caracter in str(nombre)): #valida todas las letras de la palabra
                    nombre.title()
                    return nombre
            else:
                print("Nombre invalido")
        except TypeError:
            print("Error al ingresar nombre")   

def filtrar_vehiculo():
    modelo=input("Indique el modelo desea filtrar: ")
    modelo=modelo.title()
    encontrar=False  
    for patentes,datos in Vehiculos.items():
        if datos[2] == modelo:
            print("="*10)
            print(f"Patente: {patentes} || Dueño: {datos[0]} || Sexo: {datos[1]} || Marca vehiculo {datos[2]}")
            print("="*10)
            print("\n")
            encontrar=True
        if not encontrar:
            print("Modelo no encontrado")
       
    return("Error al ingresar datos")

def eliminar_vehiculo():
    print("Usted eliminará un vehiculo")
    eliminar=validar_patente()
    if eliminar != None:
        del Vehiculos[eliminar]
        return("Vehiculo eliminado")

                
while True:
        print("\n")
        print("===Menú Aduanas de Chile===")
        print("1.- Ingresar vehiculo.")
        print("2.-Eliminar vehiculo.")
        print("3.-Buscar vehiculo.")
        print("4.-Ver vehiculos.")
        print("5.- Cerrar.")
        print("="*7)
        try: 
            opcion=int(input("Ingrese opción que desea: "))
            match opcion:
                case 1:
                    ingresar_datos()
                case 2:
                    eliminar_vehiculo()
                case 3:
                    filtrar_vehiculo()
                case 4:
                    print("="*10)
                    for patentes,datos in Vehiculos.items():
                        print(f"Patente: {patentes} || Dueño: {datos[0]} || Sexo: {datos[1]} || Marca vehiculo {datos[2]}")
                    print("="*10)
                    print("\n")
                case 5:
                    print("Adios")
                    break
                case _:
                    print("Opción invalida.")
        except ValueError:
            print("Error al ingresar datos.")
        