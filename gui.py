import sys
from trainingDaemon import TrainingDaemon
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QPushButton, QLCDNumber)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.daemon = TrainingDaemon(delay=1, debug=True)
        self.initUI()
        # self.timer = QBasicTimer()
        # self.timer.start(10, self)

    def timerEvent(self, e):
        picture_path = self.daemon.current_exercise.exercice.picture_path if self.daemon.current_exercise is not None else None
        if picture_path is not None:
            picture = QPixmap(picture_path)
            picture = picture.scaledToHeight(400)
            self.lbl.setPixmap(picture)
        else:
            self.lbl.setText('No picture')
        self.timer_step.display(self.daemon.current_time)

    def initUI(self):

        # self.program_list = QComboBox(self)
        # self.qbtn = QPushButton('STATE', self)
        # self.lbl = QLabel('pic here', self)
        # self.lbl.setGeometry(100,100, 600, 400)
        # self.timer_step = QLCDNumber(self)
        # self.timer_step.setGeometry(100,0, 200, 50)


        self.scroll = QScrollArea(self)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.scroll_Layout = QtWidgets.QVBoxLayout(self.scroll)
        for _ in range(12):
            self.scroll_Layout.addWidget(QLabel('test'))

        self.setGeometry(300, 300, 1000, 400)
        self.setWindowTitle('Never A Fat Ass Again')
        self.show()

    def select_program(self, selected_program):
        self.daemon.set_program(selected_program)

    def state_button(self):
        if not self.daemon.state:
            self.daemon.set_state_running()
        else:
            self.daemon.set_state_pause()
        


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
