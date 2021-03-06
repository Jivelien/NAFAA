from exercise import Exercise
import json


class Program:
    def __init__(self,  program_definition, rest_time = 5):
        self.exercise_list = self._read_json_db('exerciseDb.json')
        self.rest_time = rest_time
        self.steps = []

        for step in program_definition:

            exercise_name = step.get('exercise')
            exercise_definititon = self.exercise_list.get(exercise_name)
            time_step = step.get('time')

            is_both_side = exercise_definititon.get('both_side')

            self.steps.append(self.Step('Rest', self.exercise_list.get('Rest'), self.rest_time ))
            self.steps.append(self.Step(exercise_name, exercise_definititon, time_step))
            if is_both_side:
                self.steps.append(self.Step('Rest', self.exercise_list.get('Rest'), self.rest_time ))
                self.steps.append(self.Step(exercise_name, exercise_definititon, time_step))
            

    class Step:
        def __init__(self, exercise_name, exercise_definition, time):
            self.exercise = Exercise(name = exercise_name,
                                    picture_path = exercise_definition.get('pic'),
                                    is_both_side = exercise_definition.get('both_side')
                                    )
            self.time = time

    def _read_json_db(self, pathname):
        with open(pathname, 'r') as myfile:
            data = myfile.read()
        return json.loads(data)

    def get_full_time(self):
        return sum([step.time for step in self.steps])

    def get_time_at_id(self,id):
        return sum([step.time for step in self.steps[:id]])