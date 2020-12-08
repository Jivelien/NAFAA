class Exercise:
    def __init__(self, name = '', picture_path = None, is_both_side = False):
        self.name = name
        self.picture_path = picture_path
        self.is_both_side = False if is_both_side == None else is_both_side