import json
import threading
from program import Program
from time import time, sleep

STATE_STOP = 0
STATE_RUNNING = 1
STATE_PAUSE = 2


class TrainingDaemon:
    def __init__(self, delay=1, debug = False):
        self._delay = delay
        self._thread = None
        self._debug = debug

        self.state = STATE_STOP
        self.program_list = self._read_json_db('programDb.json')
        self.exercise_list = self._read_json_db('exerciseDb.json')

        self.current_program = None
        self.current_exercise = None
        self.current_step = 0
        self.current_time = 0
        self.exercice_side = 0

        self.start()

    def set_program(self, program_name):
        program_definition = self.program_list.get(program_name)
        self.current_program = Program(program_definition)
        self.current_step = 0
        self.current_time = 0
        self.exercice_side = 0
        self.state = STATE_STOP
        self.set_exercice()

    def set_exercice(self):
        self.current_exercise = self.current_program.steps[self.current_step]

    def set_state_stop(self):
        self.current_step = 0
        self.current_time = 0
        self.exercice_side = 0
        self.state = STATE_STOP

    def set_state_pause(self):
        self.state = STATE_PAUSE

    def set_state_running(self):
        if self.current_program is not None:
            self.state = STATE_RUNNING
        else:
            self.state = STATE_STOP

    def _read_json_db(self, pathname):
        with open(pathname, 'r') as myfile:
            data = myfile.read()
        return json.loads(data)

    def run(self):
        while True:
            if self.current_program is None:
                sleep(self._delay)
                if self._debug:
                    print(f"{time()} - No programm")
                continue
            if self._debug:
                print(
                    f"{time()} - {'RUNNING' if self.state else 'NOT RUNNING'} -[{self.current_exercise.exercice.name}] {self.current_time}/{self.current_exercise.time} -{self.current_exercise.exercice.name} - {self.current_exercise.exercice.picture_path}")
            if self.state == STATE_RUNNING:
                self.current_time += self._delay
                if self.current_time >= self.current_exercise.time:
                    self.current_time = 0
                    if self.current_exercise.exercise.is_both_side and self.exercice_side == 0:
                        self.exercice_side = 1
                    else:
                        self.current_step += 1
                        self.set_exercice()
                    if self.current_step >= len(self.current_program.steps):
                        self.set_state_stop()

            sleep(self._delay)

    def start(self):
        self._thread = threading.Thread(target=self.run, daemon=True)
        self._thread.start()
