from views.maze_view import MazeView

class GameMove:

    def __init__(self, maze):
        self.maze = maze

    def move(self):
        see_maze = MazeView(self.maze)

        running = True

        while running == True:

            see_maze.display_maze()

            direction = input("Enter a direction: ")

            if direction == "w":
                if self.maze.can_move_to(self.maze.location[0]-1,self.maze.location[1]) == True:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                    self.maze.location = (self.maze.location[0]-1,) + self.maze.location[1:]
                    print("Successful Move")
                else:
                    print("Unsuccessful Move")

            elif direction == "a":
                if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]-1) == True:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                    self.maze.location = (self.maze.location[0], self.maze.location[1]-1,)
                    print("Successful Move")
                else:
                    print("Unsuccessful Move")
                    
            elif direction == "s":
                if self.maze.can_move_to(self.maze.location[0]+1,self.maze.location[1]) == True:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                    self.maze.location = (self.maze.location[0]+1,) + self.maze.location[1:]
                    print("Successful Move")
                else:
                    print("Unsuccessful Move")

            elif direction == "d":
                if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]+1) == True:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                    self.maze.location = (self.maze.location[0], self.maze.location[1]+1,)
                    print("Successful Move")
                else:
                    print("Unsuccessful Move")
            else:
                print("Invalid Direction")
            
            if self.maze.can_move_to(self.maze.location[0], self.maze.location[1]) == True:
                if self.maze.is_exit(self.maze.location[0], self.maze.location[1]) == False:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = "P"
                        
            if self.maze.is_exit(self.maze.location[0],self.maze.location[1]) == True:
                print("Exit Reached")
                running = False

            if running == True:
                print(self.maze.location)