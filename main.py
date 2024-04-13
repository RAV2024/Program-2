import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)

        self.button = self.findChild(QPushButton, 'button')
        self.button.clicked.connect(self.on_click)
        self.show_circle = False

    def on_click(self):
        self.show_circle = True
        self.update()

    def paintEvent(self, event):
        if self.show_circle:
            painter = QPainter(self)
            painter.setPen(Qt.NoPen)
            color = QColor('yellow')
            painter.setBrush(color)

            size = random.randint(10, 100)
            x = random.randint(0, self.width() - size)
            y = random.randint(0, self.height() - size)

            painter.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
