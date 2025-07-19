# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 671)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.groupBox)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 6, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 7, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 8, 1, 1, 1)

        self.ordenar_id_pushButton = QPushButton(self.groupBox)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.gridLayout.addWidget(self.ordenar_id_pushButton, 12, 0, 1, 2)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.gridLayout.addWidget(self.ordenar_distancia_pushButton, 13, 0, 1, 2)

        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.gridLayout.addWidget(self.ordenar_velocidad_pushButton, 14, 0, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 9, 0, 1, 2)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 10, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 11, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ordenar_id_tabla_pushButton = QPushButton(self.tab_4)
        self.ordenar_id_tabla_pushButton.setObjectName(u"ordenar_id_tabla_pushButton")

        self.gridLayout_3.addWidget(self.ordenar_id_tabla_pushButton, 1, 0, 1, 1)

        self.ordenar_velocidad_tabla_pushButton = QPushButton(self.tab_4)
        self.ordenar_velocidad_tabla_pushButton.setObjectName(u"ordenar_velocidad_tabla_pushButton")

        self.gridLayout_3.addWidget(self.ordenar_velocidad_tabla_pushButton, 1, 1, 1, 1)

        self.ordenar_distancia_tabla_pushButton = QPushButton(self.tab_4)
        self.ordenar_distancia_tabla_pushButton.setObjectName(u"ordenar_distancia_tabla_pushButton")

        self.gridLayout_3.addWidget(self.ordenar_distancia_tabla_pushButton, 1, 2, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_4)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 2, 0, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_4)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setDragEnabled(False)

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 2, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_4)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 2, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_4)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mostrar_puntos_xy_pushButton = QPushButton(self.tab)
        self.mostrar_puntos_xy_pushButton.setObjectName(u"mostrar_puntos_xy_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_puntos_xy_pushButton, 2, 0, 1, 2)

        self.puntos_cercanos_pushButton = QPushButton(self.tab)
        self.puntos_cercanos_pushButton.setObjectName(u"puntos_cercanos_pushButton")

        self.gridLayout_5.addWidget(self.puntos_cercanos_pushButton, 2, 2, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 1, 2, 1, 1)

        self.visualizador_graphicsView = QGraphicsView(self.tab)
        self.visualizador_graphicsView.setObjectName(u"visualizador_graphicsView")

        self.gridLayout_5.addWidget(self.visualizador_graphicsView, 0, 0, 1, 7)

        self.visualizador_plainTextEdit = QPlainTextEdit(self.tab)
        self.visualizador_plainTextEdit.setObjectName(u"visualizador_plainTextEdit")

        self.gridLayout_5.addWidget(self.visualizador_plainTextEdit, 0, 7, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 1, 0, 1, 2)

        self.mostrar_visualizador_pushButton = QPushButton(self.tab)
        self.mostrar_visualizador_pushButton.setObjectName(u"mostrar_visualizador_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_visualizador_pushButton, 1, 3, 1, 1)

        self.dikjstra_pushButton = QPushButton(self.tab)
        self.dikjstra_pushButton.setObjectName(u"dikjstra_pushButton")

        self.gridLayout_5.addWidget(self.dikjstra_pushButton, 2, 4, 1, 1)

        self.convertir_a_grafo_pushButton = QPushButton(self.tab)
        self.convertir_a_grafo_pushButton.setObjectName(u"convertir_a_grafo_pushButton")

        self.gridLayout_5.addWidget(self.convertir_a_grafo_pushButton, 1, 4, 1, 1)

        self.Prim_pushButton = QPushButton(self.tab)
        self.Prim_pushButton.setObjectName(u"Prim_pushButton")

        self.gridLayout_5.addWidget(self.Prim_pushButton, 2, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID (ascendente)", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia (descendente)", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u" Ordenar por velocidad (ascendente)", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.ordenar_id_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID (ascendente)", None))
        self.ordenar_velocidad_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad (ascendente)", None))
        self.ordenar_distancia_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia (descendente)", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.mostrar_puntos_xy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar puntos XY", None))
        self.puntos_cercanos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar puntos cercanos", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.mostrar_visualizador_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.dikjstra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dikjstra", None))
        self.convertir_a_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Convertir a grago", None))
        self.Prim_pushButton.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Visualizador", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

