
import csv, random
from player import Player
class Maze:

    def __init__(self,filename):
        with open(filename, 'r') as inputfile:
            content = list(csv.reader(inputfile))
        self.content = content
        self.player = Player()
        self.location = [(x, y.index("P")) for x, y in enumerate(self.content) if "P" in y]

        i = 0
        while i < 4:
            found = True

            while found:
                line = random.choice(self.content)
                spot = random.randrange(0,len(line))

                if line[spot] == " ":
                    found = False
                    x = self.content.index(line)
                    y = spot
                    self.content[x][y] = "i"
                    i += 1

    def can_move_to(self, line, column):
        if self.content[line][column] != "X":
            return True
        else:
            return False

    def display(self):
        for i in self.content:
            print(i)

    def find_random_spot(self):
        found = True
        while found:
            line = random.choice(self.content)
            spot = random.randrange(0,len(line))

            if line[spot] != "X":
                found = False
                x = self.content.index(line)
                y = spot

        location = (x,y)
        return(location)

    def is_item(self, line, column):
        if self.content[line][column] == "i":
            return True
        else:
            return False

    def is_exit(self, line, column):
        if self.content[line][column] == "E":
            winner = 'winner'
            return True
        else:
            return False




maze1 = Maze("7X7 Maze.txt")

maze1.display()

print(maze1.location)

print(maze1.can_move_to(0, 1))

print(maze1.can_move_to(5, 1))

print(maze1.find_random_spot())

print(maze1.is_exit(1,5))

print(maze1.is_exit(1,4))

print(maze1.is_item(5, 3))

print(maze1.is_item(5, 4))

