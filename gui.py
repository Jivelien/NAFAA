from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys
from trainingDaemon import TrainingDaemon
import threading
from time import sleep

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.daemon = TrainingDaemon(debug=True)
        self.initUI()
        self.daemon.state=1
        self._thread = threading.Thread(target=self.update_interface, daemon=True)
        self._thread.start()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.lbl = QLabel(self)

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Sid')
        self.show()

    def update_interface(self):
        while True:
            p = self.daemon.current_exercise.get('pic')
            if p is None: 
                p='.jpg'
            pp = QPixmap()
            pp.load(p)
            pp = pp.scaledToHeight(100)
            self.lbl.setPixmap(pp)
            sleep(.1)

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()