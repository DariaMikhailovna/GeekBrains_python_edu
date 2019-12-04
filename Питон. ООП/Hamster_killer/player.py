from random import choice


class Player:
    max_health = 10

    def __init__(self, coords):
        self.health = self.max_health
        self.position = coords

    def was_hit(self, hid):
        self.health -= choice(range(hid + 1))

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("Players health:", self.health)
