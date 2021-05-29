from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QColor, QFont, QPainter, QPen, QBrush
from PyQt5.uic import loadUi
from random import sample, choices
from sys import argv, exit
from Algorithms import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("Interface.ui", self)
        self.c_height = 421
        self.font = QFont()
        self.font.setPointSize(12)
        self.speed = {
            0: ["0.25x", 2.5],
            1: ["0.5x", 2],
            2: ["0.75x", 1.5],
            3: ["1x", 1],
            4: ["1.25x", 0.5],
            5: ["1.5x", 0.2],
            6: ["1.75x", 0.1],
        }
        self.colors = {
            "red": QColor(243, 23, 23),
            "green": QColor(1, 169, 8),
            "blue": QColor(0, 0, 250),
            "black": QColor(0, 0, 0),
            "violet": QColor(166, 0, 218),
            "orange": QColor(255, 146, 0),
        }
        self.sorts_desc = {
            "Bubble Sort": ["O(n²)", "O(1)"],
            "Insertion Sort": ["O(n²)", "O(1)"],
            "Selection Sort": ["O(n²)", "O(1)"],
            "Quick Sort": ["O(nlogn)", "O(nlogn)"],
            "Merge Sort": ["O(nlogn)", "O(n)"],
        }
        self.pen = QPen(self.colors["black"], 3)
        self.generate.clicked.connect(self.generateArray)
        self.lenslider.valueChanged.connect(self.updatelength)
        self.minslider.valueChanged.connect(self.updatemin)
        self.maxslider.valueChanged.connect(self.updatemax)
        self.speedslider.valueChanged.connect(self.updatespeed)
        self.start.clicked.connect(self.startalgorithm)
        self.show()

    def updatelength(self):
        self.len = self.lenslider.value()
        self.lenval.setText(str(self.len))

    def updatemin(self):
        self.mn = self.minslider.value()
        self.minval.setText(str(self.mn))

    def updatemax(self):
        self.mx = self.maxslider.value()
        self.maxval.setText(str(self.mx))

    def updatespeed(self):
        self.sd = self.speedslider.value()
        self.speedval.setText(self.speed[self.sd][0])

    # This will generate new random array
    def generateArray(self):
        self.start.setDisabled(False)
        self.tmcomp.setText("")
        self.spcomp.setText("")
        self.len = self.lenslider.value()
        self.mn = self.minslider.value()
        self.mx = self.maxslider.value()
        if (self.mx - self.mn + 1) >= self.len:
            self.arr = sample(range(self.mn, self.mx + 1), self.len)
        else:
            self.arr = choices(range(self.mn, self.mx + 1), k=self.len)

        self.drawData(["red"] * (self.len))

    # draws rectangle bars on to the screen
    def drawData(self, color):
        self.scene = QGraphicsScene()
        self.c_width = 831 - 13 * self.len
        x_width = self.c_width / (self.len + 1)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        maxele = max(self.arr)
        normalizedData = [i / maxele for i in self.arr]
        for i, height in enumerate(normalizedData):
            x0 = i * (x_width + 13)
            y0 = self.c_height - height * 370
            x1 = x_width
            y1 = self.c_height - y0
            self.brush = QBrush(self.colors[color[i]])
            self.scene.addRect(x0, y0, x1, y1, self.pen, self.brush)
            num = self.scene.addText(str(self.arr[i]))
            num.setPos(x0, y0 - 30)
            num.setFont(self.font)

    # Logic being executed when we click on start button
    def startalgorithm(self):
        self.generate.setDisabled(True)
        self.start.setDisabled(True)
        self.selected_algo = self.algorithm.currentText()
        self.sd = self.speed[self.speedslider.value()][1]
        if self.selected_algo == "Bubble Sort":
            BubbleSort(self.len, self.arr, self.drawData, self.sd)
        elif self.selected_algo == "Insertion Sort":
            InsertionSort(self.len, self.arr, self.drawData, self.sd)
        elif self.selected_algo == "Selection Sort":
            SelectionSort(self.len, self.arr, self.drawData, self.sd)
        elif self.selected_algo == "Merge Sort":
            MergeSort(self.len, 0, self.len - 1, self.arr, self.drawData,
                      self.sd)
        elif self.selected_algo == "Quick Sort":
            QuickSort(self.len, 0, self.len - 1, self.arr, self.drawData,
                      self.sd)

        self.generate.setDisabled(False)
        self.tmcomp.setText(self.sorts_desc[self.selected_algo][0])
        self.spcomp.setText(self.sorts_desc[self.selected_algo][1])


app = QApplication(argv)
mainwindow = MainWindow()
exit(app.exec_())
