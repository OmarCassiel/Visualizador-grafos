#listaParticulas.py

from particula import Particula
import json

class ListaParticulas:
    
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        if len(self.__particulas) > 0:
            for p in self.__particulas:
                print(p)
        else:
            print("No hay particulas guardadas")
    
    def __str__(self):
        return "".join(
            str(p) + "\n" for p in self.__particulas
        )
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:#abre un archivo en modo escritura, "archivo es el nombre se nuestro archivo donde se guardan los vuelos, pero solo en el programa"
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent = 5)
                return 1
        except:
            return 0
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:#abre el archivo en modo lectura
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]#aqui se esta volviendo a hacer una lista, tomando el archivo que queremos abrir
                return 1
            
        except:
            return 0
    #sirve para obtener la lista de particulas    
    def obtener_particulas(self):
        return self.__particulas
    
    def convertir_particula_a_grafo(particulas):
        grafo = {}#se inicializa un grafo vacio
        
        for particula in particulas:
            punto_origen = (particula.origen_x, particula.origen_y)
            punto_destino = (particula.destino_x, particula.destino_y)
            distancia = particula.distancia

            #agrega el punto de origen y su arista al dicionario
            if punto_origen not in grafo:
                grafo[punto_origen] = []
            grafo[punto_origen].append([punto_destino, distancia])

            #agrega el punto de destino y su arista al diccionario
            if punto_destino not in grafo:
                grafo[punto_destino] = []
            grafo[punto_destino].append([punto_origen, distancia])

        return grafo



    def __len__(self):
        return(
            len(self.__particulas)
        )

    def __iter__(self):
        self.cont = 0

        return self
    
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            molecula = self.__particulas[self.cont]
            self.cont += 1
            return molecula
        else:
            raise StopIteration

#p1 = Particula(id = 1, origen_x = 20, origen_y = 25, destino_x = 30, destino_y = 40,
                  #velocidad = 50, red = 111 ,green = 132, blue = 123)    
#p2 = Particula(id = "2", origen_x = 30, origen_y = 35, destino_x = 10, destino_y = 10,
                 # velocidad = 20, red = 101, green = 182, blue = 120)
#p3 = Particula(id = "3", origen_x = 60, origen_y = 15, destino_x = 20, destino_y = 80,
                  #velocidad = 50, red = 203, green = 18, blue = 10)

#listaParticulas = ListaParticulas()
#listaParticulas.agregar_final(p1)
#listaParticulas.agregar_final(p2)
#listaParticulas.agregar_inicio(p3)

#listaParticulas.mostrar()