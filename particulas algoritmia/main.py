from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys 
#aplicacion de qt
app= QApplication()

#crear nueva ventana 
window = MainWindow()

window.show()

sys.exit(app.exec_())

#pyside2-uic mainwindow.ui > ui_mainwindow.py