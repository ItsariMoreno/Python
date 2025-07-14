from random import *
listaa=[]
for i in range (8):
    lista=(randint(1,100))
    listaa.append(lista)
    
print (listaa)
print (len(listaa))


#lista.append(x)	Agrega un elemento al final de la lista.
#lista.extend(otra_lista)	Agrega los elementos de otra lista.
#lista.insert(i, x)	Inserta x en la posición i.
#lista.remove(x)	Elimina la primera aparición de x.
#lista.pop([i])	Elimina y devuelve el elemento en la posición i (último si no se indica i).
#lista.clear()	Elimina todos los elementos de la lista.
#lista.index(x)	Devuelve la posición de la primera aparición de x.
#lista.count(x)	Cuenta cuántas veces aparece x.
#lista.sort()	Ordena la lista en orden ascendente.
#lista.reverse()	Invierte el orden de los elementos.
#lista.copy()	Devuelve una copia superficial de la lista.
#len(lista)	Devuelve la cantidad de elementos.
#max(lista)	Devuelve el valor máximo.
#min(lista)	Devuelve el valor mínimo.
#sum(lista)	Devuelve la suma de los elementos.
#sorted(lista)	Devuelve una nueva lista ordenada.
#list(objeto)	Convierte un objeto iterable en una lista.
#isalpha()	Solo letras	"abc".isalpha() → True
#xisdigit()	Solo dígitos	"123".isdigit() → True
#isalnum()	Letras o dígitos	"abc123".isalnum() → True
#islower()	Todo en minúsculas	"abc".islower() → True
#isupper()	Todo en mayúsculas	"ABC".isupper() → True
#isspace()	Solo espacios	" ".isspace() → True
#startswith(x)	¿Empieza con x?	"hola".startswith("h") → True
#endswith(x)	¿Termina con x?	"hola".
#lower()	Todo en minúsculas	"HOLA".lower() → "hola"
#upper()	Todo en mayúsculas	"hola".upper() → "HOLA"
#capitalize()	Primera letra en mayúscula	"python".capitalize() → "Python"
#title()	Primera letra de cada palabra en mayús.	"hola mundo".title() → "Hola Mundo"
#swapcase()	Invierte mayúsculas ↔ minúsculas	"PyThOn".swapcase() → "pYtHoN"

#################DICCIONARIOS#################333
# ✅ Crear diccionarios
d = {}                     # Diccionario vacío
d = dict()                 # Otra forma de crear uno vacío
d = {"clave": "valor"}     # Diccionario con una clave y un valor

# ✅ Agregar o modificar elementos
d["nombre"] = "Pedro"      # Agrega nueva clave o actualiza si ya existe

# ✅ Acceder a elementos
valor = d["nombre"]        # Devuelve el valor asociado a la clave (error si no existe)
valor = d.get("edad")      # Devuelve None si no existe la clave
valor = d.get("edad", 0)   # Devuelve 0 si no existe la clave

# ✅ Verificar si existe una clave
existe = "nombre" in d     # True
no_existe = "edad" in d    # False

# ✅ Eliminar elementos
del d["nombre"]            # Elimina la clave y su valor
valor = d.pop("edad", "No existe")  # Elimina y devuelve el valor, o un valor por defecto si no existe

# ✅ Limpiar diccionario
d.clear()                  # Elimina todos los elementos del diccionario

# ✅ Obtener claves, valores y pares
claves = d.keys()          # Devuelve todas las claves (vista dinámica)
valores = d.values()       # Devuelve todos los valores (vista dinámica)
pares = d.items()          # Devuelve tuplas de (clave, valor)

# ✅ Recorrer diccionario
for clave in d:
    print(clave, d[clave])

for clave, valor in d.items():
    print(clave, valor)

# ✅ Copiar diccionario
copia = d.copy()           # Copia superficial (shallow copy)

# ✅ Actualizar con otro diccionario
d.update({"edad": 30})     # Agrega o actualiza claves desde otro diccionario

# ✅ Establecer valor si la clave no existe
d.setdefault("pais", "Chile")  # Si "pais" no existe, se agrega con "Chile"

# ✅ Cantidad de elementos
cantidad = len(d)          # Devuelve el número de pares clave:valor

