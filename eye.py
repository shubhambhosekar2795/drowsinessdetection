

from PyQt5.QtWidgets import *
import os


import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QInputDialog 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
	
        self.setMinimumSize(QSize(1366, 768))    
        self.setWindowTitle("CAR DASHBOARD DESKTOPAPP") 


        oImage = QImage("image.jpg")
        sImage = oImage.scaled(QSize(1366,768))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     
        self.setPalette(palette)

 #   def __init__(self):
  #      QtGui.QWidget.__init__(self)
        pybutton = QPushButton('', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(44,44)
        pybutton.move(1032, 260)
        pybutton.setIcon(QtGui.QIcon("carsleep.jpg"))
        pybutton.setIconSize(QtCore.QSize(44,44))
        pybutton.setToolTip("This Will Open The AppFrame")

 #   def showNameDialog(self):
  #  	text=QInputDialog.getText('Drowshbv.dkabvga.ekhbkvsegvbf.kugvbHkUERGHKVUEKGI/erkeghrughyDetect')
   # 	text.move(1032, 260)
    #	print(text)        

    def clickMethod(self):
        os.system("python Drowsiness_Detection.py")
        mainWin.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
#   app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
