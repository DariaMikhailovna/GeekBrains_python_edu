from random import randint


class Hamster:
    def __init__(self, hid, coords):
        self.id = hid
        self.health = randint(1, 4)
        self.position = coords

    def on_shot(self):
        self.health -= 1
        return self.health == 0
