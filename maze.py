import csv, random

class Maze:
        def __init__(self,filename):
            with open(filename, 'r') as inputfile:
                content = list(csv.reader(inputfile))
            self.content = content

        def check(self, line, column):
            if self.content[line][column] == " ":
                return True
            elif self.content[line][column] == "x":
                return False

        def display(self):
            for i in self.content:
                print(i)

        def find_random_spot(self):
            found = True
            while found:
                line = random.choice(self.content)
                spot = random.randrange(0,len(line))

                if line[spot] == " ":
                    found = False
                    x = self.content.index(line)
                    y = spot

            location = (x,y)
            print(location)
                
        def is_item(self):
                pass


maze1 = Maze("7X7 Maze.txt")

maze1.display()

print(maze1.check(1, 1))

print(maze1.check(1, 4))

maze1.find_random_spot()
