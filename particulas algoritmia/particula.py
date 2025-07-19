#particula.py

from algoritmos import * #nuestra funcion para calcular la distancia entre dos puntos

class Particula:
    #constructor
    def __init__(self, id = "", origen_x = "", origen_y = "", destino_x = "", destino_y = "",
                  velocidad = "", red = "" ,green = "", blue = ""):
        #atributos
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    #metodos

    def __str__(self): #nos sirve para convertir los atributos de nuestro objeto en string y poder imprimirlo
        return(
            "Identificador: " + str(self.__id) + "\n"
            "Origen x: " + str(self.__origen_x) + "\n"
            "Origen y: " + str(self.__origen_y) + "\n"
            "Destino x: " + str(self.__destino_x) + "\n"
            "Destino y: " + str(self.__destino_y) + "\n"
            "Velocidad: " + str(self.__velocidad) + "\n"
            "Red: " + str(self.__red) + "\n"
            "Green: " + str(self.__green) + "\n"
            "Blue: " + str(self.__blue) + "\n"
            "Distancia: " + str(self.__distancia) + "\n"
        )
    
    def to_dict(self):#nos convierte la informacion de la particula en diccionario
        return{
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
    
    #def __lt__(self, other):
        #return self.id < other.id
    

    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x
    
    @property
    def origen_y(self):
        return self.__origen_y
    
    @property
    def destino_x(self):
        return self.__destino_x
    
    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red
    
    @property
    def green(self):
        return self.__green
    
    @property 
    def blue(self):
        return self.__blue
    
    @property
    def distancia(self):
        return self.__distancia

#p1 = Particula(id = 1, origen_x = 20, origen_y = 25, destino_x = 30, destino_y = 40,
                  #velocidad = 50, red = 111 ,green = 132, blue = 123)    
#p2 = Particula(id = "2", origen_x = "30", origen_y = "35", destino_x = "10", destino_y = "10",
                 # velocidad = "20", red = "101" ,green = "182", blue = "120", distancia = "25.3")
#print(p1)
#print(p2)