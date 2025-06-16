from random import *
Jugador=str(input("Ingresa tu nombre: "))
print("Bienvenido ",Jugador," Has ingresado al juego de la")
print("=========Ruleta Rusa========")

while True:
    try:
        jugar=str(input("====¿Desea jugar?===="))
        if     jugar.lower() == "no":
            print("...Cobarde")
            print("-Disparo-")
            print(";;;;;;;;;;;; ", Jugador, " Usted ha fallecido ;;;;;;;;;;;;")
            continue
        elif jugar.lower() =="si":
            
            partida=True
            while partida == True:  
                print(" ")
                print("...")
                print(" ")
                Cantidad_Balas=int(input("===¿Cuantas balas desea insertar?:"))       
                print("...")
                print(" ")
                Bala=1
                while Bala<=Cantidad_Balas and partida ==True:
                    apretar=(input("===Apriete el gatillo (Ingrese cualquier tecla)==="))
                    print(" ")
                    Disparo= (randint(1,5))
                    print(" ")
                
                    if Disparo== 1 or Disparo == 3 or Disparo== 4 or Disparo== 5  and Bala<=Cantidad_Balas:
                        print("Numero de Bala: ",Bala," Suerte")
                        print(" ")
                        print(" ")
                        print("La bala era falsa")
                        print(" ")
                        print("El número del randit es: ", Disparo)
                        if Bala<Cantidad_Balas:
                            print(" Felicidades ", Jugador, " sigue jugando...Por ahora")
                        Bala=Bala+1 

                    if Disparo == 2:
                        print("Numero de Bala: ",Bala," Suerte")
                        print("La bala estaba cargada")
                        print(" ")
                        print(" -Disparo- ")   
                        print(":::::::::::::::::::::::::::::::::::::: ",Jugador," Usted Falleció :::::::::::::::::::::::::::::::::::")
                        partida=False
                        
                if Bala>Cantidad_Balas:
                    print("Ha superado todas las balas")
                    Bala=Bala-1
                    print("Numero de balas superadas: (", Bala, ")")
                    print(" ===Felicidades ",Jugador," Usted ha ganado la ruleta===")
                    print(" ")
                    print(" ")
                    
                Jugar_Nuevamente=(input("¿Desea volver a jugar?: "))
                if Jugar_Nuevamente == "No" or Jugar_Nuevamente == "no":
                    Partida=False
                    print(" ")
                    print("Nos vemos a la próxima ", Jugador)
                    print(" ")
                    break
                else:
                    partida=True
    except ValueError as error:
        print("Error tipo: ", error, " debe ingresar si o no")
        continue
    else:
        if jugar.lower() != "si" or jugar.lower() != "no":
            print("Error, debe ingresar solo si o no")
            continue



                    
                
                
            