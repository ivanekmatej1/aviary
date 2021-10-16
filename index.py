import matplotlib.pyplot as plt
import numpy as np
import PyQt5.QtWidgets as pw
import sys

from PyQt5.QtWidgets import QPushButton, QLabel


class MyWindow(pw.QMainWindow):
    label: QLabel
    b1: QPushButton

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Main Window")
        self.initUI()

    def initUI(self):
        self.label = pw.QLabel(self)
        self.label.setText("My first label")
        self.label.move(50, 50)

        self.b1 = pw.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.uponClick)

    def uponClick(self):

        self.label.setText("Function plotted")
        self.update()

    def update(self):

        self.label.adjustSize()


def window():
    app = pw.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
