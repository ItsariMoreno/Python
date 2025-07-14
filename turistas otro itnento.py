#turista={folio: nombre, pais, fecha}
Turista = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}



def agregar_turista():
    folio=input("folio: ")
    nombre=input("nombre: ")
    pais=input("pais: ")
    fecha=input("fecha: ")

    Turista[folio]=[nombre,pais,fecha]  
    print(Turista)
    

def buscar_pais():
    pais=input("Ingrese el pais que desea buscar: ")
    for buscar in Turista.values(): #buscar es i y values es el valor "key": "value" #está separando {} en listas
        if buscar[1].lower()== pais.lower(): #lower 1 no funciona pq tienes que poner opciones [0,1,2]
            print(buscar[0])

def turistas_mes():
    buscar_fecha=int(input("ingrese el mes que quiere estimar: "))
    contador=0
    for buscar in Turista.values():
        fecha=buscar[2]#estamos diciendo que busque en fechas
        mes=int(fecha.split("-")[1]) #split sirve para busar luego de - y en pocision 1 o sea se salta el 0 en 01
        if mes==buscar_fecha: #EN EL SPLIT NO PONGAS () = FECHA.SPLIT(("-"))
            contador=contador+1
    if contador >=1:
            print("hubieron: ", contador, " De turistas ese mes")
    else:
            print("sin turistas encontrados ese mes")

def eliminar_turistas():
    buscar_nombre=input("ingrese el nombre del turista que desea eliminar: ")
    for buscar in Turista.values():
        if buscar[0].lower()== buscar_nombre.lower():
            print(buscar_nombre, " Eliminado")
            del Turista[buscar] #con buscar pq buscar obtiene el diccionario completo, con buscar_nombre solo se elimina el nombre del turista
    print(Turista)

def ver_turistas():
    for keys, values in Turista.items(): #items muestra todo 
        print(f"ID: {keys} || nombre: {values[0]} || pais: {values[1]} || fecha ingreso: {values[2]}")

while True: 
    print("===Menú===")
    print("1.-Agregar turista")
    print("2.-Turistas por país")
    print("3.-Turista por mes")
    print("4.-Eliminar turista")
    print("5.- Ver lista turistas")
    print("6.-Salir")
    opcion=int(input("Ingrese que opción desea: "))

    match opcion:
            case 1:
                agregar_turista()
            case 2:
                buscar_pais()
            case 3:
                turistas_mes()
            case 4:
                eliminar_turistas()
            case 5:
                ver_turistas()
            case 6:
                print("Fin de sistema")
                break
            
        