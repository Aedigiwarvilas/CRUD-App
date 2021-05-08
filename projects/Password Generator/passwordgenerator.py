from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from sys import exit, argv
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from pyperclip import copy, paste
from random import sample, choice, shuffle


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("passwordgenerator.ui", self)
        self.L = [ascii_lowercase, ascii_uppercase, digits, punctuation]
        self.generate.clicked.connect(self.passgenerate)
        self.copy.clicked.connect(self.passcopy)
        self.check.clicked.connect(self.passcheck)
        self.paste.clicked.connect(self.passpaste)
        self.show()

    def passgenerate(self):
        try:
            password = []
            l = int(self.length.currentText())
            w = self.weak.isChecked()
            m = self.medium.isChecked()
            s = self.strong.isChecked()
            self.color = ["red", "blue", "green"]
            if w == True:
                L = sample(self.L, 2)
                j = 0
                for i in range(l):
                    password.append(choice(L[i % 2]))
            elif m == True:
                j = 1
                L = sample(self.L, 3)
                for i in range(l):
                    password.append(choice(L[i % 3]))
            elif s == True:
                j = 2
                L = sample(self.L, 4)
                for i in range(l):
                    password.append(choice(L[i % 4]))
            shuffle(password)
            password = "".join(password)
            self.res1.setStyleSheet("color:{}".format(self.color[j]))
            self.res1.setText(password)
        except:
            pass

    def passcheck(self):
        try:
            password = self.lineEdit.text()
            L = [False, False, False, False]
            for i in password:
                if i in self.L[0] and L[0] == False:
                    L[0] = True
                elif i in self.L[1] and L[1] == False:
                    L[1] = True
                elif i in self.L[2] and L[2] == False:
                    L[2] = True
                elif i in self.L[3] and L[3] == False:
                    L[3] = True

            if all(L):
                j = 2
                self.res2.setText("Strong")
            elif L.count(False) == 1:
                j = 1
                self.res2.setText("Medium")
            elif L.count(True) in (1, 2):
                j = 0
                self.res2.setText("Weak")
            else:
                self.res2.setText("")
            self.res2.setStyleSheet("color:{}".format(self.color[j]))
        except:
            pass

    def passcopy(self):
        try:
            copy(self.res1.text())
        except:
            pass

    def passpaste(self):
        try:
            self.lineEdit.setText(paste())
        except:
            pass


app = QApplication(argv)
mainwindow = MainWindow()
exit(app.exec_())
