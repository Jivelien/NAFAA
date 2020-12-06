STATE_STOP = 0
STATE_RUNNING = 1
STATE_PAUSE = 2

class TrainingDaemon:
    
    def __init__(self):
        self.state = STATE_STOP

