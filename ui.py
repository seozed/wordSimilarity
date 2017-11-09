# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel

from PyQt5.QtCore import QCoreApplication, QSize


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('切换题目', self)
        qbtn.resize(QSize(150,50))
        qbtn.move(175, 10)


        label = QLabel('Hello', self)
        label.move(175,70)


        qbtn_a = QPushButton('A', self)
        qbtn_a.resize(QSize(150,50))
        qbtn_a.move(175, 120)

        qbtn_b = QPushButton('B', self)
        qbtn_b.resize(QSize(150,50))
        qbtn_b.move(175, 170)

        qbtn_c = QPushButton('C', self)
        qbtn_c.resize(QSize(150, 50))
        qbtn_c.move(175, 220)

        qbtn_d = QPushButton('D', self)
        qbtn_d.resize(QSize(150, 50))
        qbtn_d.move(175, 270)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('word similar')
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())