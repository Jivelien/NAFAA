import json
import threading
from time import time, sleep

STATE_STOP = 0
STATE_RUNNING = 1
STATE_PAUSE = 0

class TrainingDaemon:
    def __init__(self):
        self._delay = 1
        self.timer = None

        self.state = STATE_STOP
        self.program_list = self._read_json_db('programDb.json')
        self.exercise_list = self._read_json_db('exerciseDb.json')

        self.current_program = 'Etirement'
        self.current_step = 0
        self.current_time = 0
        self.exercice_side = 0

        self.start()


    def _read_json_db(self, pathname):
        with open(pathname, 'r') as myfile:
            data=myfile.read()
        return json.loads(data)

    def run(self):
        while True:
            program = self.program_list.get(self.current_program)
            step = program[self.current_step]
            exercice_name = step.get('exercise')
            time_step = step.get('time')
            exercise = self.exercise_list.get(exercice_name)
            exercise_pic = exercise.get('pic')
            exercise_both_side = exercise.get('both_side')

            print(f"{time()} - {'RUNNING' if self.state else 'NOT RUNNING'} -[{self.exercice_side}] {self.current_time}/{time_step} -{exercice_name} - {exercise_pic}")
            if self.state :
                self.current_time +=1
                if self.current_time >= time_step:
                    self.current_time = 0
                    if exercise_both_side and self.exercice_side == 0:
                        self.exercice_side = 1
                    else:
                        self.current_step += 1
                    if self.current_step >= len(program):
                        #self.state = STATE_STOP
                        self.current_step = 0
                        self.exercice_side = 0
            sleep(self._delay)

    def start(self):
        self.timer = threading.Thread(target = self.run, daemon = True) 
        self.timer.start()
