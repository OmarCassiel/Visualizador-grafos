#algoritmos.py

import math
from queue import PriorityQueue
#x_1 = origen_x
#y_1 = origen_y
#x_2 = destino_x
#y_2 = destino_y
def distancia_euclidiana(x_1, y_1, x_2, y_2):#funcion para calcular la distancia entre dos puntos
    
    distancia =  math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
    
    return distancia
   
def particulas_mas_cercanas(particulas_list):
    puntos = []

    # Generar una lista de puntos con origen y destino de cada partícula
    for particula in particulas_list:
        puntos.append((particula.origen_x, particula.origen_y))
        puntos.append((particula.destino_x, particula.destino_y))

    resultado = []

    # Encontrar el punto más cercano para cada punto
    for punto_i in puntos:
        x1, y1 = punto_i
        min_distancia = float('inf')
        punto_mas_cercano = None
        for punto_j in puntos:
            if punto_i != punto_j:
                x2, y2 = punto_j
                distancia = distancia_euclidiana(x1, y1, x2, y2)
                if distancia < min_distancia:
                    min_distancia = distancia
                    punto_mas_cercano = (x2, y2)

        # Agregar la conexión entre puntos
        if punto_mas_cercano:
            resultado.append((punto_i, punto_mas_cercano))

    return resultado



def dijkstra(grafo, start):
    # Inicializa el diccionario de distancias con infinito para todos los nodos.
    distances = {vertex: float('infinity') for vertex in grafo}
    # La distancia del nodo inicial a sí mismo es 0.
    distances[start] = 0

    # Inicializa el diccionario de nodos previos para reconstruir los caminos.
    previos = {vertex: None for vertex in grafo}

    # Inicializa la cola de prioridad y añade el nodo inicial con distancia 0.
    queue = PriorityQueue()
    queue.put((0, start))  # La cola almacena tuplas (distancia, nodo).

    # Mientras haya elementos en la cola, seguimos procesando.
    while not queue.empty():
        # Extrae el nodo con la menor distancia acumulada.
        current_distance, current_vertex = queue.get()

        # Si la distancia actual ya no es la mínima conocida, lo ignoramos.
        if current_distance > distances[current_vertex]:
            continue

        # Explora los nodos adyacentes al nodo actual.
        for neighbor, weight in grafo[current_vertex]:
            # Calcula la nueva distancia acumulada hasta el nodo vecino.
            distance = current_distance + weight

            # Si esta nueva distancia es menor que la previamente registrada, actualizamos.
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Actualizamos la distancia mínima.
                previos[neighbor] = current_vertex  # Registramos el nodo previo.
                queue.put((distance, neighbor))  # Añadimos el vecino a la cola con la nueva distancia.

    return distances, previos

#tiene el propósito de encontrar y devolver el camino más corto desde un nodo inicial (start) hasta un nodo final (end) en un grafo
def reconstruir_camino(previos, start, end):
    #Almacenará el camino desde start hasta end.
    camino = []# Lista vacía que almacenará el camino más corto
    actual = end# Comenzamos desde el nodo final Se inicializa con el nodo final (end) porque vamos a retroceder desde ahí hacia el nodo inicial.

    # Seguimos hacia atrás desde el nodo objetivo hasta el nodo de inicio.
    while actual is not None:
        camino.insert(0, actual)  # Insertamos cada nodo al principio de la lista.
        actual = previos[actual]

    # Si el primer nodo no es el nodo de inicio, no hay camino.
    if camino[0] != start:
        return []

    return camino

def prim(grafo, start):

    visitados = set()  #Conjunto de nodos ya visitados
    visitados.add(start)  #Marcamos el nodo inicial como visitado

    aristas_aem = []  #Lista para almacenar las aristas del AEM
    peso_total = 0  #Peso acumulado del AEM

    #Cola de prioridad para seleccionar la arista de menor peso
    cola = PriorityQueue()

    #Añadimos todas las aristas del nodo inicial a la cola
    for vecino, peso in grafo[start]:
        cola.put((peso, start, vecino))

    #Mientras haya nodos por visitar y la cola no este vacia
    while not cola.empty() and len(visitados) < len(grafo):
        peso, origen, destino = cola.get()  #Extrae la arista de menor peso
        
        if destino not in visitados:  #Si el destino aún no ha sido visitado
            visitados.add(destino)  #Marcamos el nodo destino como visitado
            aristas_aem.append((origen, destino))  #Agregamos la arista al AEM
            peso_total += peso  #Sumamos el peso al total

            #Agregamos las aristas del nodo recien visitado a la cola
            for vecino, peso in grafo[destino]:
                if vecino not in visitados:
                    cola.put((peso, destino, vecino))

    return aristas_aem, peso_total
