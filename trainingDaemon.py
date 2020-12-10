import json
import threading
from program import Program
from time import time, sleep

STATE_STOP = 0
STATE_RUNNING = 1
STATE_PAUSE = 0


class TrainingDaemon:
    def __init__(self, delay=1, debug = False, autostart = False):
        self._delay = delay
        self._thread = None
        self._debug = debug

        self.state = STATE_STOP
        self.program_list = self._read_json_db('programDb.json')
        self.exercise_list = self._read_json_db('exerciseDb.json')

        self.current_program = None
        self.current_step = None
        self.current_step_id = 0
        self.current_time = 0
        self.exercise_side = 0

        if autostart:self.start() 

    def set_program(self, program_name):
        program_definition = self.program_list.get(program_name)
        self.current_program = Program(program_definition) if program_definition is not None else None
        self.current_step_id = 0
        self.current_time = 0
        self.exercise_side = 0
        self.state = STATE_STOP
        if self.current_program is not None:
            self.set_exercise()
        else:
            self.current_step = None

    def set_exercise(self):
        self.current_step = self.current_program.steps[self.current_step_id]

    def set_state_stop(self):
        self.current_step_id = 0
        self.current_time = 0
        self.exercise_side = 0
        self.current_program = None
        self.current_step = None
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
                    f"{time()} - State: {self.state} -[{self.current_step.exercise.name}] {self.current_time}/{self.current_step.time} -{self.current_step.exercise.name} - {self.current_step.exercise.picture_path}")
            if self.state == STATE_RUNNING:
                self.current_time += self._delay
                if self.current_time >= self.current_step.time:
                    self.current_time = 0
                    if self.current_step.exercise.is_both_side and self.exercise_side == 0:
                        self.exercise_side = 1
                    else:
                        self.current_step_id += 1
                    if self.current_step_id >= len(self.current_program.steps):
                        self.set_state_stop()
                    else:
                        self.set_exercise()

            sleep(self._delay)

    def start(self):
        self._thread = threading.Thread(target=self.run, daemon=True)
        self._thread.start()
