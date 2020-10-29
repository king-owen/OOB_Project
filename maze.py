import csv, random

class Maze:
        def __init__(self,filename):
            with open(filename, 'r') as inputfile:
                content = list(csv.reader(inputfile))
            self.content = content

        def check(self, line, column):
            if self.content[line][column] == " ":
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
                spot = random.choice(line)
                if spot == " ":
                    found = False
            location = (line, spot)
            print(location)

maze1 = Maze("7X7 Maze.txt")

maze1.display()

print(maze1.check(1, 1))

print(maze1.check(1, 4))

maze1.find_random_spot()