from player import Player
from hamsters import Hamster
from random import randint

hamsters_count = 4


class Game:
    map = """****\n****\n****\n****"""
    directions = {"w": "s", "s": "w", "a": "d", "d": "a"}
    happy_message = "WOW!!!! You won!!!"

    def __init__(self):
        self.game_on = True
        self.hamsters = {}
        for i in range(hamsters_count):
            self.hamsters[i + 1] = Hamster(i + 1, self.get_clear_position())
        self.player = Player(self.get_clear_position())  # фикс баги с наезжающим на хомяков игроком

    def get_clear_position(self):
        map = self.get_full_map()
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        while True:
            coords = [randint(0, map_width - 1), randint(0, map_height - 1)]
            if map.split("\n")[coords[1]][coords[0]] == "*":
                return coords

    def add_point(self, position, name, s):
        li = s.split('\n')
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self):
        s = self.get_full_map()
        s = self.add_point(self.player.position, "x", s)
        print(s)

    def get_full_map(self):
        s = self.map
        for h in self.hamsters.values():
            s = self.add_point(h.position, str(h.id), s)
        return s

    def move_player(self, destination):
        """"destination = w,a,s,d"""
        if destination == "s":
            if self.player.position[1] == len(self.map.split("\n")) - 1:
                return False
            self.player.position[1] += 1
        if destination == "w":
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        if destination == "a":
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        if destination == "d":
            if self.player.position[0] == len(self.map.split("\n")[0]) - 1:
                return False
            self.player.position[0] += 1
        self.on_move(destination)

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]

    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == "*":
            self.player.was_hit(int(hamster))
            if self.player.health <= 0:
                self.game_on = False
                print("GAME OVER!!! AZAZA")
                return False
            print("Player's health: ", self.player.health)
            killed = self.hamsters[int(hamster)].on_shot()
            if not killed:
                print("wasn't killed")
                self.move_player(self.directions[direction])
            else:
                print(int(hamster), 'was killed')
                del self.hamsters[int(hamster)]  # фикс баги с концом игры

    def start(self):
        print(game.render_map())
        while self.game_on:
            if len(self.hamsters) == 0:
                print(self.happy_message)
                return False
            command = input("Insert command: ")
            if command in ["a", "s", "d", "w"]:
                self.move_player(command)
                self.render_map()
            if command == "e":
                self.player.wait()
            if command == "q":
                self.game_on = False


game = Game()
game.start()
