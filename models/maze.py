
import csv, random
from .player import Player

class Maze:

    def __init__(self,filename):
        with open(filename, 'r') as inputfile:
            content = list(csv.reader(inputfile))
        self.content = content
        self.player = Player()
        self.location = [(x, y.index("P")) for x, y in enumerate(self.content) if "P" in y][0]

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
                    self.content[x][y] = "key"
                    i += 1

    def can_move_to(self, line, column):
        if self.content[line][column] != "X":
            if self.is_item(line, column) == True:
                return True
            else:
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
        if self.content[line][column] == "key":
            self.player.appendItem("key")
            print("Picked up Item")
            print(self.player.backpack)

            self.content[line][column] = " "
            return True
        else:
            return False

    def is_exit(self, line, column):
        if self.content[line][column] == "E":
            if len(self.player.backpack) == 4:
                print("You win")
            else:
                print("You lose")
            return True
        else:
            return False
    


# def main(maze):
#     running = True

#     maze.display()

#     while running == True:
#         direction = input("Enter a direction: ")

#         if direction == "w":
#            if maze.can_move_to(maze.location[0]-1,maze.location[1]) == True:
#                maze.content[maze.location[0]][maze.location[1]] = " "
#                maze.location = (maze.location[0]-1,) + maze.location[1:]
#                print("Successful Move")
#            else:
#                print("Unsuccessful Move")

#         elif direction == "a":
#             if maze.can_move_to(maze.location[0],maze.location[1]-1) == True:
#                 maze.content[maze.location[0]][maze.location[1]] = " "
#                 maze.location = (maze.location[0], maze.location[1]-1,)
#                 print("Successful Move")
#             else:
#                 print("Unsuccessful Move")
                
#         elif direction == "s":
#             if maze.can_move_to(maze.location[0]+1,maze.location[1]) == True:
#                 maze.content[maze.location[0]][maze.location[1]] = " "
#                 maze.location = (maze.location[0]+1,) + maze.location[1:]
#                 print("Successful Move")
#             else:
#                 print("Unsuccessful Move")

#         elif direction == "d":
#             if maze.can_move_to(maze.location[0],maze.location[1]+1) == True:
#                 maze.content[maze.location[0]][maze.location[1]] = " "
#                 maze.location = (maze.location[0], maze.location[1]+1,)
#                 print("Successful Move")
#             else:
#                 print("Unsuccessful Move")
#         else:
#             print("Invalid Direction")
        
#         if maze.can_move_to(maze.location[0], maze.location[1]) == True:
#             if maze.is_exit(maze.location[0], maze.location[1]) == False:
#                 maze.content[maze.location[0]][maze.location[1]] = "P"

                
#         if maze.is_exit(maze.location[0],maze.location[1]) == True:
#             print("Exit Reached")
#             running = False

#         if running == True:
#             maze.display()
#             print(maze.location)
        
