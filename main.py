import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Кружечки')

        layout = QVBoxLayout()
        self.btn = QPushButton('НАЖМИ')
        self.btn.setFixedSize(100, 50)
        self.btn.clicked.connect(self.draw_circle)
        layout.addWidget(self.btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        self.color = QColor()
        self.diameter = 0
        self.circle_x = 0
        self.circle_y = 0

    def draw_circle(self):
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.diameter = random.randint(20, 100)
        self.circle_x = random.randint(0, self.width() - self.diameter)
        self.circle_y = random.randint(0, self.height() - self.diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.circle_x, self.circle_y, self.diameter, self.diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
