import os
import sys
import subprocess
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QSpinBox, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QRadioButton, QAction, QLineEdit, QMessageBox, QLabel


class Root(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setFixedSize(400, 600)
        self.title = "Password Generator"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 600
        self.InitWindow()

    def InitWindow(self):

        self.setWindowIcon(QtGui.QIcon("flamingo.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.image = QLabel(self)
        self.image.setPixmap(QtGui.QPixmap("flamingo.png"))
        self.image.resize(100, 100)
        self.image.move(150, 80)
        self.image.show()

        self.button = QPushButton('Alphanumerical Password', self)
        self.button.clicked.connect(self.Alphanumerical)
        self.button.resize(180, 40)
        self.button.move(120, 260)

        self.button2 = QPushButton('Secure Password', self)
        self.button2.clicked.connect(self.Secure)
        self.button2.resize(180, 40)
        self.button2.move(120, 310)

        self.button3 = QPushButton('', self)
        self.button3.setIcon(QtGui.QIcon("gear.png"))
        self.button3.clicked.connect(self.Info)
        self.button3.move(20, 20)
        self.button3.resize(30, 30)

        self.image = QLabel(self)
        self.image.setPixmap(QtGui.QPixmap("file.png"))
        self.image.resize(250, 250)
        self.image.move(120, 30)
        self.image.show()

        self.label = QLabel(self)
        self.label.setText("Friendly Password Generator")
        self.label.move(120, 550)
        self.label.resize(400, 20)

        self.label2 = QLabel(self)
        self.label2.setText("Type of Password")
        self.label2.move(150, 220)
        self.label2.resize(400, 20)

        self.font = QFont("SansSerif")
        self.font.setBold(True)

        self.label3 = QLabel(self)
        self.label3.setFont(self.font)
        self.label3.setText("Generate a password \n")
        self.label3.move(130, 410)
        self.label3.resize(400, 40)

        self.show()


    def Alphanumerical(self):
        self.pw = subprocess.run(['pwgen', '-s', '10', '1'], capture_output = True, text=True).stdout
        self.label3.setText("Your password is: \n" + '   ' + str(self.pw))

    def Secure(self):
        self.pw = subprocess.run(['pwgen', '-s', '-y', '10', '1'], capture_output = True, text=True).stdout
        self.label3.setText("Your password is: \n" + '   ' + str(self.pw))

    def Info(self):
        self.info = QMessageBox()
        self.top2 = 400
        self.left2 = 200
        self.width2 = 400
        self.height2 = 600
        self.info.setGeometry(self.top2, self.left2, self.width2, self.height2)
        self.info.setWindowTitle("Information")
        self.info.setText("\nThis tool is a free/open-source software \
that provides the user a secure password. It is very important \
to set strong passwords, in case of a cyber attack, it will be \
very difficult for an attacker to break the password. \n\n Version: 1.0 \n\n License: GPL v3.0")
        self.info.show()

App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
