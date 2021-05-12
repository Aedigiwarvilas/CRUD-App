import PyQt5
import sys

class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.show()

app=PyQt5.QtWidgets.QApplication(sys.argv)
mainwindow=MainWindow()
sys.exit(app.exec_())