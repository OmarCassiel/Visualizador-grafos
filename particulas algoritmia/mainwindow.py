from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from listaParticulas import ListaParticulas
from particula import *
from algoritmos import *
from pprint import pprint
from queue import PriorityQueue
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.listaParticulas = ListaParticulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #botones
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)#agrega particula al inicio
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)#agrega particula al final
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)#muestra las particulas
        self.ui.ordenar_id_pushButton.clicked.connect(self.click_ordenar_id)#muestra las particulas ordenadas por id
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.click_ordenar_distancia)#muestra las particulas ordenadas por distancia
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.click_ordenar_velocidad)#muestra las particulas ordenadas por velocidad

        self.ui.actionAbrir.triggered.connect(self.action_abrir_Archivo)#pestaña para abrir archivos json
        self.ui.actionGuardar.triggered.connect(self.action_guardar_Archivo)#respalda las particulas en un archivo json

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)#muestra las particulas en la tabla
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)#buscar una particula por id
        self.ui.ordenar_id_tabla_pushButton.clicked.connect(self.ordenar_id_tabla)#ordena las particulas en la tabla por id
        self.ui.ordenar_distancia_tabla_pushButton.clicked.connect(self.ordenar_distancia_tabla)#ordena las particulas en la tabla por distancia
        self.ui.ordenar_velocidad_tabla_pushButton.clicked.connect(self.ordenar_velocidad_tabla)#ordena las particulas de la tabla por velocidad

        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)#limpiar el visualizador
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)#dibujar las particulas
        self.ui.puntos_cercanos_pushButton.clicked.connect(self.puntos_cercanos)# une los puntos xy con su punto mas cercano
        self.ui.mostrar_puntos_xy_pushButton.clicked.connect(self.mostrar_puntos_xy)#muestra los puntos xy
        self.ui.convertir_a_grafo_pushButton.clicked.connect(self.convertir_a_grafo)#convierte la particula a grafo
        self.ui.mostrar_visualizador_pushButton.clicked.connect(self.mostrar_visualizador)#muestra los datos de las particulas en la pestaña del vizualizador
        self.ui.dikjstra_pushButton.clicked.connect(self.dikjstra)#en proceso
        self.ui.Prim_pushButton.clicked.connect(self.prim)#en proceso

        self.scene = QGraphicsScene()
        self.ui.visualizador_graphicsView.setScene(self.scene)
        

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinoX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        green = self.ui.green_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, blue, green)
        self.listaParticulas.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinoX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        green = self.ui.green_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, blue, green)
        self.listaParticulas.agregar_final(particula)

    @Slot()
    def click_mostrar(self):
        #self.listaParticulas.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.listaParticulas))

    #def ordenar_particulas(self, key, reverse = False):
        #print(f"ordenar {key.__name__}")
        #particulas = self.listaParticulas.obtener_particulas() 
        #particulas.sort(key=key, reverse=reverse) 
        #self.ui.plainTextEdit.insertPlainText("\n".join(str(particula) for particula in particulas))

    @Slot()
    def click_ordenar_id(self):
         print("ordenar id")
         self.ui.plainTextEdit.clear()
         particulas = self.listaParticulas.obtener_particulas()
         particulas.sort(key=lambda particula: particula.id)
         #self.ui.plainTextEdit.insertPlainText("\n".join(str(particula) for particula in particulas))
         #self.ordenar_particulas(key=lambda particula: particula.id)
         self.click_mostrar()


    @Slot()
    def click_ordenar_distancia(self):
         print("ordenar distancia")
         self.ui.plainTextEdit.clear()
         particulas = self.listaParticulas.obtener_particulas()
         particulas.sort(key=lambda particula: particula.distancia, reverse=True)
         self.click_mostrar()
         #self.ui.plainTextEdit.insertPlainText("\n".join(str(particula) for particula in particulas))

    @Slot()
    def click_ordenar_velocidad(self):
         print("ordenar velocidad")
         self.ui.plainTextEdit.clear()
         particulas = self.listaParticulas.obtener_particulas()
         particulas.sort(key=lambda particula: particula.velocidad)
         #self.ui.plainTextEdit.insertPlainText("\n".join(str(particula) for particula in particulas))
         self.click_mostrar()

    @Slot()
    def action_guardar_Archivo(self):
        #se obtione la direccion de donde se quiere guardar el archivo
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]#esto para tomar el primer elemento de la tupla y obtener solo la direccion
        print(ubicacion)
        if self.listaParticulas.guardar(ubicacion):
            #recibe 3 parametros, la clase el mensaje de la ventana, el mensaje dentro adentro
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def action_abrir_Archivo(self):
        #se obtiene la direccion del archivo que se quiere abrir
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]#esto para tomar el primer elemento de la tupla y obtener solo la direccion
        self.listaParticulas.abrir(ubicacion)

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "ORIGEN X", "ORIGEN Y", "DESTINO X", "DESTINO Y", "VELOCIDAD", "R", "G", "B", "DISTANCIA"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.listaParticulas))

        row = 0

        for particula in self.listaParticulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row +=1

    @Slot()
    def ordenar_id_tabla(self):
        print("ordenar  id tabla")
        self.ui.tabla.clear()
        particulas = self.listaParticulas.obtener_particulas()
        particulas.sort(key=lambda particula: particula.id)
        self.mostrar_tabla()
        
        #self.ui.tabla.setColumnCount(10)
        #headers = ["ID", "ORIGEN X", "ORIGEN Y", "DESTINO X", "DESTINO Y", "VELOCIDAD", "R", "G", "B", "DISTANCIA"]
        #self.ui.tabla.setHorizontalHeaderLabels(headers)

        #self.ui.tabla.setRowCount(len(self.listaParticulas))

        #row = 0

        #for particula in self.listaParticulas:
            #id_widget = QTableWidgetItem(str(particula.id))
            #origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            #origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            #destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            #destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            #velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            #red_widget = QTableWidgetItem(str(particula.red))
            #green_widget = QTableWidgetItem(str(particula.green))
            #blue_widget = QTableWidgetItem(str(particula.blue))
            #distancia_widget = QTableWidgetItem(str(particula.distancia))

            #self.ui.tabla.setItem(row, 0, id_widget)
            #self.ui.tabla.setItem(row, 1, origen_x_widget)
            #self.ui.tabla.setItem(row, 2, origen_y_widget)
            #self.ui.tabla.setItem(row, 3, destino_x_widget)
            #self.ui.tabla.setItem(row, 4, destino_y_widget)
            #self.ui.tabla.setItem(row, 5, velocidad_widget)
            #self.ui.tabla.setItem(row, 6, red_widget)
            #self.ui.tabla.setItem(row, 7, green_widget)
            #self.ui.tabla.setItem(row, 8, blue_widget)
            #self.ui.tabla.setItem(row, 9, distancia_widget)

            #row +=1

    @Slot()
    def ordenar_distancia_tabla(self):
        print("ordenar distancia tabla")
        self.ui.tabla.clear()
        particulas = self.listaParticulas.obtener_particulas()
        particulas.sort(key=lambda particula: particula.distancia, reverse = True)
        self.mostrar_tabla()

    @Slot()
    def ordenar_velocidad_tabla(self):
        print("ordenar velocidad tabla")
        self.ui.tabla.clear()
        particulas = self.listaParticulas.obtener_particulas()
        particulas.sort(key=lambda particula: particula.velocidad)
        self.mostrar_tabla()

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "ORIGEN X", "ORIGEN Y", "DESTINO X", "DESTINO Y", "VELOCIDAD", "R", "G", "B", "DISTANCIA"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        encontrado = False

        for particula in self.listaParticulas:
            if str(id) == str(particula.id):
                #self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el Identificador "{id}" no fue encontrada'
            )

    @Slot()
    def dibujar(self):
        print('dibujar')
        pen = QPen()
        pen.setWidth(2)

        for self.particula in self.listaParticulas:
            color = QColor(self.particula.red, self.particula.green, self.particula.blue)
            pen.setColor(color)

            self.scene.addEllipse(self.particula.origen_x, self.particula.origen_y, 6, 6, pen)
            self.scene.addEllipse(self.particula.destino_x, self.particula.destino_y, 6, 6, pen)
            self.scene.addLine(self.particula.origen_x + 3, self.particula.origen_y + 3, self.particula.destino_x + 3, self.particula.destino_y + 3, pen)
        
    @Slot()
    def limpiar(self):
        print('limpiar')
        self.scene.clear()

    @Slot()
    def mostrar_puntos_xy(self):
         print("mostrar puntos")
         particulas = self.listaParticulas.obtener_particulas()

         pen = QPen()
         pen.setWidth(2)
         
         for particula in particulas:
              color = QColor(particula.red, particula.green, particula.blue)
              pen.setColor(color)

              self.scene.addEllipse(particula.origen_x, particula.origen_y, 6, 6, pen)
              self.scene.addEllipse(particula.destino_x, particula.destino_y, 6, 6, pen)

    @Slot()
    def puntos_cercanos(self):
         print("puntos cercanos")
         particulas = self.listaParticulas.obtener_particulas()
         conexiones = particulas_mas_cercanas(particulas)

         pen = QPen(QColor(255, 0, 0))  # Rojo para las líneas
         pen.setWidth(2)

         for punto1, punto2 in conexiones:
              x1, y1 = punto1
              x2, y2 = punto2
              self.scene.addLine(x1, y1, x2, y2, pen)

    @Slot()
    def convertir_a_grafo(self):
         print("particulas convertidas a grado")
         self.ui.visualizador_plainTextEdit.clear()
         #se obtiene el grafo
         grafo = self.listaParticulas.convertir_particula_a_grafo()

         #cadena para poder imprimir en la interfaz
         lista_adyacencia = ""

         #recorre cada nodo del grafo
         for nodo, conexiones in grafo.items():
              #inicializa la cola de prioridad
              cola_prioridad = PriorityQueue()

              #agrega las conexiones actuales del nodo a la cola
              for conexion in conexiones:
                   destino, distancia = conexion
                   cola_prioridad.put((distancia, destino))
              
              lista_adyacencia += f"{nodo} --> "
              while not cola_prioridad.empty():
                   distancia, destino = cola_prioridad.get()
                   lista_adyacencia += f"{destino}), "

              lista_adyacencia = lista_adyacencia.rstrip(", ")  # Eliminamos la coma final
              lista_adyacencia += "]\n"

        # Imprimimos la lista en consola
         print(lista_adyacencia)
         # Mostramos la lista en el QPlainTextEdit
         self.ui.plainTextEdit.clear()
         self.ui.visualizador_plainTextEdit.insertPlainText(lista_adyacencia)

    #@Slot()
    #def lista_adyacencia(self):
         #print("imprimiendo lista de adyacencia")

    @Slot()
    def mostrar_visualizador(self):
         print("mostrar particulas")
         self.ui.visualizador_plainTextEdit.clear()
         self.ui.visualizador_plainTextEdit.insertPlainText(str(self.listaParticulas))

    @Slot()
    def prim(self):
        #Genera el grafo a partir de las particulas
        grafo = self.listaParticulas.convertir_particula_a_grafo()

        #Seleccionar un nodo inicial aleatorio
        import random
        start = random.choice(list(grafo.keys()))
        print(f"Nodo inicial seleccionado para Prim: {start}")

        #Calcular el AEM usando Prim
        aristas_aem, peso_total = prim(grafo, start)

        #Mostrar resultados en consola
        print(f"Árbol de Expansión Mínima (AEM):")
        for arista in aristas_aem:
            print(arista)
        print(f"Peso total del AEM: {peso_total}")

        #Dibuja el grafo con las aristas del AEM resaltadas
        self.scene.clear()

        #Configura las plumas para dibujar
        pen_normal = QPen()
        pen_normal.setWidth(2)
        pen_normal.setColor(QColor(200, 200, 200))  #Color gris es para conexiones normales

        pen_aem = QPen()
        pen_aem.setWidth(3)
        pen_aem.setColor(QColor(0, 255, 0))  #Color verde es para las aristas del AEM

        #Dibujar las aristas y nodos
        for particula in self.listaParticulas:
            origen_x, origen_y = particula.origen_x, particula.origen_y
            destino_x, destino_y = particula.destino_x, particula.destino_y

            nodo_origen = (origen_x, origen_y)
            nodo_destino = (destino_x, destino_y)

            if (nodo_origen, nodo_destino) in aristas_aem or (nodo_destino, nodo_origen) in aristas_aem:
                pen = pen_aem  #Resaltar arista en el AEM
            else:
                pen = pen_normal  #Arista normal

            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)
            self.scene.addEllipse(origen_x, origen_y, 6, 6, pen)
            self.scene.addEllipse(destino_x, destino_y, 6, 6, pen)


    @Slot()
    def dikjstra(self):
         print("dikjstra")
         #Construye el grafo a partir de las partículas
         grafo = self.listaParticulas.convertir_particula_a_grafo()
         #selecciona al azar un nodo del grafo como nodo inicial
         start = random.choice(list(grafo.keys()))
         #Ejecuta el algoritmo de Dijkstra
         distancias, previos = dijkstra(grafo, start)
         # Muestra las distancias y caminos más cortos
         resultado = f"Distancias desde el nodo {start}:\n"

         for nodo, distancia in distancias.items():
              resultado += f"{nodo}: {distancia}\n"

         resultado += "\nCaminos más cortos:\n"
         for nodo in grafo:
              if nodo != start: 
                   camino = reconstruir_camino(previos, start, nodo)
                   resultado += f"{start} -> {nodo}: {camino}\n"

         self.scene.clear()
         #Configuración de plumas para dibujar
         pen_normal = QPen()
         pen_normal.setWidth(2)
         pen_normal.setColor(QColor(200, 200, 200))  # Color gris para conexiones normales

         pen_dijkstra = QPen()
         pen_dijkstra.setWidth(3)
         pen_dijkstra.setColor(QColor(255, 0, 0))  # Color rojo para el camino más corto

         for particula in self.listaParticulas:
              # Coordenadas de la partícula
             origen_x, origen_y = particula.origen_x, particula.origen_y
             destino_x, destino_y = particula.destino_x, particula.destino_y

             #Determinar si esta conexión está en el camino más corto
             nodo_origen = (origen_x, origen_y)
             nodo_destino = (destino_x, destino_y)

             if nodo_destino in previos and previos[nodo_destino] == nodo_origen:#se usa para saber de que color usara la pluma
                  # Conexión utilizada en el camino más corto
                  pen = pen_dijkstra
             elif nodo_origen in previos and previos[nodo_origen] == nodo_destino:
                  # Conexión utilizada en el camino más corto
                  pen = pen_dijkstra
             else:
                  pen = pen_normal

             # Dibujar la conexión (línea)
             self.scene.addLine(origen_x + 3, origen_y + 3, destino_x + 3, destino_y + 3, pen)

             # Dibujar los nodos (círculos)
             self.scene.addEllipse(origen_x, origen_y, 6, 6, pen)
             self.scene.addEllipse(destino_x, destino_y, 6, 6, pen)

         # Opcional: Mostrar nodo inicial con un color diferente
         pen_start = QPen()
         pen_start.setWidth(3)
         pen_start.setColor(QColor(0, 255, 0))  # Verde para el nodo inicial
         start_x, start_y = start
         self.scene.addEllipse(start_x - 3, start_y - 3, 12, 12, pen_start)


         print(resultado)  # Imprime en la consola.
         
         self.ui.visualizador_plainTextEdit.clear()
         self.ui.visualizador_plainTextEdit.insertPlainText(resultado)

    def wheelEvent(self, event):
                print(event.delta())
                if event.delta() > 0:
                        self.ui.visualizador_graphicsView.scale(1.2, 1.2)
                else:
                        self.ui.visualizador_graphicsView.scale(0.8, 0.8)