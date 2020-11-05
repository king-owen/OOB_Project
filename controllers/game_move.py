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
            
        if maze.can_move_to(maze.location[0], maze.location[1]) == True:
            if maze.is_exit(maze.location[0], maze.location[1]) == False:
                maze.content[maze.location[0]][maze.location[1]] = "P"
            else:
                running = False
                print("Exit Reached")

            if running == True:
                print(self.maze.location)
