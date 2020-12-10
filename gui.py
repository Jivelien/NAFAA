from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer
import sys
from trainingDaemon import  TrainingDaemon

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('gui.ui', self)
        self.daemon = TrainingDaemon(delay=1, debug=True , autostart=True)
        self._init_ui()
        self.mainloop = QBasicTimer()
        self.mainloop.start(100, self)

    def _init_ui(self):
        self.load_program_combo()
        self.start_button.clicked.connect(self.start_button_act)
        self.stop_button.clicked.connect(self.stop_button_act)

    def timerEvent(self, e):
        self.start_stop_button_bhv()
        self.exercise_picture_bhv()
        self.step_progress_bhv()

        if self.daemon.current_program is not None:
            full_time = self.daemon.current_program.get_full_time()
            elapsed_time = self.daemon.current_program.get_time_at_id(self.daemon.current_step_id) + self.daemon.current_time
            self.full_progress_label.setText(f"{elapsed_time}/{full_time}")
            full_percent = int((elapsed_time/full_time)*100)
        else:
            self.full_progress_label.setText('')
            full_percent = 0
        self.full_progressbar.setValue(full_percent)

    def step_progress_bhv(self):
        if self.daemon.current_step is not None:
            step_percent = int((self.daemon.current_time / self.daemon.current_step.time) * 100)
            self.step_progress_label.setText(f'{self.daemon.current_time} / {self.daemon.current_step.time}')
        else:
            step_percent = 0
            self.step_progress_label.setText('')
        self.step_progressbar.setValue(step_percent)

    def start_stop_button_bhv(self):
        if self.daemon.state in (1,2):
            self.stop_button.setDisabled(False)
        else:
            self.stop_button.setDisabled(True)
        if self.daemon.state == 1:
            self.start_button.setText('PAUSE')
        else:
            self.start_button.setText('START')

    def exercise_picture_bhv(self):
        if self.daemon.current_step is not None and self.daemon.current_step.exercise.picture_path is not None:
                exercice_picture = QPixmap(self.daemon.current_step.exercise.picture_path)
                exercice_picture = exercice_picture.scaled(self.picture_label.size(),aspectRatioMode=2)
                self.picture_label.setPixmap(exercice_picture)
        else:
            self.picture_label.setPixmap(QPixmap())

    def start_button_act(self):
        if self.daemon.state != 1:
            self.daemon.set_state_running()
        else:
            self.daemon.set_state_pause()
        
    def stop_button_act(self):
        self.daemon.set_state_stop()
        self.program_combo.setCurrentIndex(0)

    def load_program_combo(self):
        self.program_combo.addItem(None)
        for key in self.daemon.program_list.keys():
            self.program_combo.addItem(key)
        self.program_combo.activated[str].connect(self.select_program)

    def select_program(self, selected_program):
        self.daemon.set_program(selected_program)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()