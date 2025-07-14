Usuarios={
"00000000-0":["Usuario", "hotmail@gmail.com", "Contraseña321+"],
"12345678-9": ["Usuario2","correo@gmail.com", "Contraseña123+"]} ###### estructura de diccionario [a modificar]




########################################OPCION 1##############################################
def registrar_usuario():

    rut=solicitar_rut()
    contrasena=solicitar_contrasena()
    correo=solicitar_correo()
    usuario=solicitar_usuario()
    Usuarios[rut]=[usuario,correo,contrasena]
    return Usuarios
   

def solicitar_usuario():
    while True:
        try:
            usuario=input("Ingrese su nombre de usuario: ")
            if " " in usuario:
                print("No puede ingresar espacios.")
                continue
            return usuario
        except Exception as error:
            print("error al ingresar el nombre")

    

def solicitar_rut():
    while True:
        try:
            rut=input("Ingrese su rut [debe contener guíon y sin puntos ]: ")
            if len(rut) >10 or len(rut) <9: 
                print("Cantidad de digitos invalidos")
                continue
            elif "-" not in rut: 
                print("Rut invalido, debe ingresar guion")
                continue
            for char in rut:    
                if char  in "123456789-kK":
                    print("rut valido")
                    return rut
                else:
                    raise Exception
        except Exception as error:
            print("Ingrese un rut valido")
        
def solicitar_correo():
    try:
        correo=input("Ingrese su gmail: ")
        if "@" in correo and (correo.endswith(".com") or correo.endswith(".cl")):
            print("El correo ingresado es válido.")
            return correo     
        else:
            print("Correo inválido, ingrese nuevamente.")
    except TypeError:
        print("Ingrese un correo válido")

####################### VALIDAR CONTRASEÑA ##################
def solicitar_contrasena():
 while True: 
            print("\n Ingrese una contraseña segura, debe contener: \n -8 carácteres mínimo \n -un símbolo \n -una mayúscula \n -un número")
            contrasena=input("Ingrese una contraseña: ")
        
            contar_caracteres(contrasena)
            contar_numeros(contrasena)
            contar_mayusculas(contrasena)
            contar_signos(contrasena)
            if validar_contrasena(contrasena) == True:
                return contrasena 
            else:
                continue
    
def contar_caracteres(contrasena):
    return len(contrasena)

def  contar_numeros(contrasena):
    contar_numeros=0
    for numeros in str(contrasena):
        if numeros.isnumeric()==True:
            contar_numeros=contar_numeros+1
    return contar_numeros

def contar_signos(contrasena):
    contar_signos=0
    simbolos="!#$%&'?\"()*+,-./:;<=>?@[\]^_`{|}~"
    for signos in str(contrasena):
        if signos in simbolos: 
            contar_signos=contar_signos+1
    return contar_signos

def contar_mayusculas(contrasena):
    contar_mayusculas=0
    for mayusculas in str(contrasena):
        if mayusculas.isupper()==True:
            contar_mayusculas=contar_mayusculas+1
    return contar_mayusculas
        
def validar_contrasena(contrasena):
    for espacio in contrasena:
        if espacio == " ":
            print("No puede ingresar espacios.")
            return False
    if contar_caracteres(contrasena)>=8:
        if contar_numeros(contrasena)>=1:
            if contar_signos(contrasena)>=1:
                if contar_mayusculas(contrasena)>=1:
                    return True 
                else:
                         print("Su contraseña debe tener: Mínimo 1 mayúscula.") 
                         return False
            else:
                     print("Su contraseña debe tener: Mínimo 1 signo.")
                     return False
        else:
            print("Su contraseña debe tener: Mínimo 1 número.")
            return False 
    else:
        print("Su contraseña debe tener: Mínimo 8 carácteres.")
        return False

##########################OPCION 2########################################

def solicitar_dato():
    while True:
        try:
            buscar=input("¿Por que desea buscar? [rut, correo o usuario]: ")
            match buscar.lower():
                case "rut":
                    rut_solicitado=solicitar_rut()
                    rut_encontrado=buscar_rut(rut_solicitado)
                    if rut_encontrado != None:
                        contrasena_pedida=solicitar_contrasena()
                        if rut_encontrado[2]==contrasena_pedida:
                            print(f"Bienvenido: {rut_encontrado[0]} sus datos son: ")
                            print(f"Rut: {rut_solicitado} || Usuario: {rut_encontrado[0]} || Correo: {rut_encontrado[1]} || Contraseña: {rut_encontrado[2]}") #rut solicitado me arrojará el rut que pidieron y este al retornar rut encontrado solo debes rotornar sus errores, asi evitas error por no encontrar TODOS los values
                            return rut_solicitado,rut_encontrado
                        else:
                            print("Contraseña incorrecta")
                        break
                    else:
                        print("El usuario no ha sido encontrado")
                case "correo":
                    correo_solicitado=solicitar_correo()
                    rut,correo_encontrado=buscar_correo(correo_solicitado)
                    if correo_encontrado != None:
                        contrasena_pedida=solicitar_contrasena()
                        if correo_encontrado[2]== contrasena_pedida:
                            print(f"Bienvenido: {correo_encontrado[0]} sus datos son: ")
                            print(f"Rut: {rut} || Usuario: {correo_encontrado[0]} || Correo {correo_encontrado[1]}|| Contraseña: {correo_encontrado[2]}")    
                            return rut, correo_encontrado
                        else:
                            print("Contraseña incorrecta")
                    else:
                        print("El usuario no ha sido encontrado")
                case "usuario":
                    usuario_solicitado=solicitar_usuario()
                    rut,usuario_encontrado=buscar_usuario(usuario_solicitado)
                    if usuario_encontrado != None:
                        contrasena_pedida=solicitar_contrasena()
                        if usuario_encontrado[2]==contrasena_pedida:
                            print(f"Rut: {rut}|| Usuario: {usuario_encontrado[0]}|| Correo {usuario_encontrado[1]}|| Contraseña: {usuario_encontrado[2]}")  
                            return rut, usuario_encontrado
                        else:
                            print("Contraseña incorrecta")
                    else:
                        print("El usuario no ha sido encontrado")
                case _:
                    print("Opción no valida")
                    continue
        except ValueError:
            print("Debe ingresar datos validos")    

def buscar_rut(rut_solicitado):
        if rut_solicitado in Usuarios: #buscar en keys
            return Usuarios[rut_solicitado]
        return None
 
def buscar_correo(correo_solicitado):
    for rut, correo_encontrado in Usuarios.items(): #buscar dentro de valores en key/value
        if correo_encontrado[1] == correo_solicitado: #buscar en posicion dentro de valor
            return rut,correo_encontrado
    return None, None

def buscar_usuario(usuario_solicitado):
    for rut, usuario_encontrado in Usuarios.items():
        if usuario_encontrado[0] == usuario_solicitado:
            return rut, usuario_encontrado
    return None, None

def comprobar_contrasena(contrasena_pedida):
    for rut, contrasena_encontrada in Usuarios.items():
        if contrasena_encontrada[2] == contrasena_pedida:
            return rut, contrasena_encontrada
    return None, None
   


#############################OPCION 3################################

def actualizar_datos():
    while True:
        try:
            buscar=input("¿Qué desea actualizar? [rut, correo, usuario o contraseña]: ")
            match buscar.lower():
                case "rut":
                     rut_solicitado=solicitar_rut()
                     if rut_solicitado in Usuarios:
                         nuevo_rut=solicitar_rut()
                         Usuarios[nuevo_rut]= Usuarios[rut_solicitado]
                         del Usuarios[rut_solicitado]
                         print("Rut actualizado")
                         print(f"Rut: {nuevo_rut} || Usuario: {Usuarios[nuevo_rut][0]} || Correo {Usuarios[nuevo_rut][1]}|| Contraseña: {Usuarios[nuevo_rut][2]}")
                         break
                case "correo":
                    correo_solicitado=solicitar_correo()
                    rut,correo_encontrado=buscar_correo(correo_solicitado)
                    if correo_encontrado != None:
                       nuevo_correo=solicitar_correo()
                       Usuarios[rut][1]=nuevo_correo
                       print("Correo actualizado correctamente")
                       print(f"Rut: {rut} || Usuario: {correo_encontrado[0]} || Correo {Usuarios[rut][1]}|| Contraseña: {correo_encontrado[2]}")    
                       break
                case "usuario":
                    usuario_solicitado=solicitar_usuario()
                    rut,usuario_encontrado=buscar_usuario(usuario_solicitado)
                    if usuario_encontrado != None:
                        nuevo_usuario=solicitar_usuario()
                        Usuarios[rut][0]=nuevo_usuario
                        print("Usuario ingresado correctamente")
                        print(f"Rut: {rut}|| Usuario: {Usuarios[rut][0]}|| Correo {usuario_encontrado[1]}|| Contraseña: {usuario_encontrado[2]}")  
                        break
                case "contraseña":
                    contrasena_solicitada=solicitar_contrasena()
                    rut, nueva_contrasena=comprobar_contrasena(contrasena_solicitada)
                    if nueva_contrasena != None:
                        nueva_contrasena=solicitar_contrasena()
                        Usuarios[rut][2]=nueva_contrasena
                        print("Contraseña actualizada")
                        print(f"Rut: {rut}|| Usuario: {usuario_encontrado[0]}|| Correo {usuario_encontrado[1]}|| Contraseña: {Usuarios[rut][2]}")  
                        break
                case _:
                    print("Opción no valida")
                    continue
        except ValueError:
            print("Debe ingresar datos validos")    

#########################################3
def eliminar_datos():
    usuario_borrar=solicitar_dato()
    if eliminar_datos is None:
        print("No se encontró usuario")
        return
    rut, eliminar_usuario= usuario_borrar
    eliminar=input("¿Desea eliminarlo? [ingrese si para eliminar]")
    if eliminar.lower() == "si":
        while True:
            contrasena_solicitada=solicitar_contrasena()
            if  eliminar_usuario[2]== contrasena_solicitada:
                del Usuarios[rut]
                print("Usuario eliminado correctamente")
                break
            else:
                print("Contraseña invalida")
                continue
    else: 
        print("Cancelado")
        return None

#################### MENÚ ##################################

while True:
    print("="*6)
    print("1.- Registrar Usuario") #CORRECTO
    print("2.- Ingresar Usuario")
    print("3.- Modificar Datos")
    print("4.- Eliminar Usuario")
    print("5.- Salir")
    print("6.- mostrar todos los usuarios")
    print("="*6)

    try:
        opcion=(int(input("Seleccione una opción: ")))
        if opcion>6 or opcion <= 0:
            raise ValueError
        else:
            match opcion:
                case 1:
                    registrar_usuario() 
                case 2:
                    solicitar_dato()
                case 3:
                    actualizar_datos()
                case 4:
                    eliminar_datos()
                case 5:
                    print("Adios")
                    break
                case 6:
                    #print(Usuarios.items()) #ver todos los usuarios
                    for keys,values in Usuarios.items():
                        print(f"Rut: {keys} || Usuario: {values[0]} || Correo {values[1]} || Contraseña {values[2]}")

    except ValueError:
        print("Ingrese un dato válido")