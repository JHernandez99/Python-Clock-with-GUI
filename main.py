from PyQt5 import QtWidgets, uic
import sys
from PySide2.QtCore import  QTime, QDate, Qt
from PySide2.QtCore import *
from PySide2.QtGui import *

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        ui = uic.loadUi('untitled.ui',self)
        self.show()
        label_fecha = self.findChild(QtWidgets.QLabel, 'lbl_fecha')
        boton = self.findChild(QtWidgets.QPushButton, 'btn_salir')
        boton.clicked.connect(self.displayTime)
        currentData = QDate.currentDate()
        fecha = currentData.toString(Qt.DefaultLocaleLongDate)
        label_fecha.setText(fecha)
        self.displayTime()



    def displayTime(self):
        displayLCD = self.findChild(QtWidgets.QLCDNumber, 'lcdNumber')
        while True:
            QtWidgets.QApplication.processEvents()
            currentTime = QTime.currentTime()
            tiempo = currentTime.toString('hh:mm:ss')
            displayLCD.display(tiempo)



app = QtWidgets.QApplication(sys.argv)
windows = Ui()
app.exec_()
