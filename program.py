from exercise import Exercise
import json


class Program:
    def __init__(self,  program_definition):
        self.exercise_list = self._read_json_db('exerciseDb.json')
        self.steps = []

        for step in program_definition:
            exercise_name = step.get('exercise')
            exercise_definititon = self.exercise_list.get(exercise_name)
            time_step = step.get('time')

            self.steps.append(self.Step(exercise_name, exercise_definititon, time_step))


    class Step:
        def __init__(self, exercice_name, exercice_definition, time):
            self.exercice = Exercise(name = exercice_name,
                                    picture_path = exercice_definition.get('pic'),
                                    is_both_side = exercice_definition.get('both_side')
                                    )
            self.time = time

    def _read_json_db(self, pathname):
        with open(pathname, 'r') as myfile:
            data = myfile.read()
        return json.loads(data)