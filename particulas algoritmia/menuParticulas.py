#menuParticulas.py

from listaParticulas import ListaParticulas
from particula import Particula

listaParticulas = ListaParticulas()

print("Menu Particulas")

while True:
    print ("1) Agregar al inicio")
    print ("2) Agregar al final")
    print("3) Mostrar")
    print("0) Salir")
    opc = input()

    if(opc == "1"):
        id = int(input("id: "))
        origen_x = int(input("origen_x: ")) 
        origen_y = int(input("origen_y: "))
        destino_x = int(input("destino_x: ")) 
        destino_y = int(input("destino_y: ")) 
        velocidad = int(input("velocidad: ")) 
        red = int(input("red: "))
        green = int(input("green: "))
        blue = int(input("blue: "))

        particula = Particula(id , origen_x , origen_y , destino_x , destino_y, velocidad , red ,green , blue)

        listaParticulas.agregar_inicio(particula)
    elif(opc == "2"):
        id = int(input("id: "))
        origen_x = int(input("origen_x: ")) 
        origen_y = int(input("origen_y: "))
        destino_x = int(input("destino_x: ")) 
        destino_y = int(input("destino_y: ")) 
        velocidad = int(input("velocidad: ")) 
        red = int(input("red: "))
        green = int(input("green: "))
        blue = int(input("blue: "))

        particula = Particula(id , origen_x , origen_y , destino_x , destino_y, velocidad , red ,green , blue)

        listaParticulas.agregar_final(particula)

    elif(opc == "3"):
        
        listaParticulas.mostrar()

    elif(opc == "0"):
        break

    else:
        print("Escoja una opcion valida")