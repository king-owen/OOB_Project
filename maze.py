import csv

class Maze:
        def __init__(self,filename):
            with open(filename, 'r') as inputfile:
                content = list(csv.reader(inputfile))
            self.content = content

        def check(self, line, column):
            pass

        def display(self):
            print(self.content)

        def find_random_spot(self):
            pass

maze1 = Maze("7X7 Maze.txt")

maze1.display()
