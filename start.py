from PyQt5.QtWidgets import *
import os



















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
#   app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
