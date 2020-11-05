from models.maze import Maze
from models.player import Player
from .game_move import GameMove

class GameStart:

    def __init__(self, maze):
        self.maze = Maze(maze)
        self.running = True

    def run(self):

        self.maze.display()

        moving = GameMove(self.maze)

        while self.running == True:
            moving.move()

            # direction = input("Enter a direction: ")

            # if direction == "w":
            #     if self.maze.can_move_to(self.maze.location[0]-1,self.maze.location[1]) == True:
            #         self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
            #         self.maze.location = (self.maze.location[0]-1,) + self.maze.location[1:]
            #         print("Successful Move")
            #     else:
            #         print("Unsuccessful Move")

            # elif direction == "a":
            #     if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]-1) == True:
            #         self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
            #         self.maze.location = (self.maze.location[0], self.maze.location[1]-1,)
            #         print("Successful Move")
            #     else:
            #         print("Unsuccessful Move")
                
            # elif direction == "s":
            #     if self.maze.can_move_to(self.maze.location[0]+1,self.maze.location[1]) == True:
            #         self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
            #         self.maze.location = (self.maze.location[0]+1,) + self.maze.location[1:]
            #         print("Successful Move")
            #     else:
            #         print("Unsuccessful Move")

            # elif direction == "d":
            #     if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]+1) == True:
            #         self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
            #         self.maze.location = (self.maze.location[0], self.maze.location[1]+1,)
            #         print("Successful Move")
            #     else:
            #         print("Unsuccessful Move")
            # else:
            #     print("Invalid Direction")
            
            # if self.maze.can_move_to(self.maze.location[0], self.maze.location[1]) == True:
            #     if self.maze.is_exit(self.maze.location[0], self.maze.location[1]) == False:
            #         self.maze.content[self.maze.location[0]][self.maze.location[1]] = "P"

                    
            # if self.maze.is_exit(self.maze.location[0],self.maze.location[1]) == True:
            #     print("Exit Reached")
            #     running = False

            # if running == True:
            #     self.maze.display()
            #     print(self.maze.location)
        
