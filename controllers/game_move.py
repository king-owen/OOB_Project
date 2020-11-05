# from views.maze_view import MazeView
import pygame
import pygame.locals

class GameMove:

    def __init__(self, maze):
        self.maze = maze

    def move(self):
        pygame.init()

        # see_maze = MazeView(self.maze)

        running = True

        while running:

            # see_maze.display_maze()

            # direction = input("Enter a direction: ")

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # if (direction == "w") or 
                    if (keys[pygame.locals.K_w]):
                        if self.maze.can_move_to(self.maze.location[0]-1,self.maze.location[1]) == True:
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0]-1,) + self.maze.location[1:]
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")

                    # elif (direction == "a") or 
                    elif (keys[pygame.locals.K_a]):
                        if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]-1) == True:
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0], self.maze.location[1]-1,)
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")
                            
                    # elif (direction == "s") or 
                    elif (keys[pygame.locals.K_s]):
                        if self.maze.can_move_to(self.maze.location[0]+1,self.maze.location[1]) == True:
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0]+1,) + self.maze.location[1:]
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")

                    # elif (direction == "d") or 
                    elif (keys[pygame.locals.K_d]):
                        if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]+1) == True:
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0], self.maze.location[1]+1,)
                    #         print("Successful Move")
                    #     else:
                    #         print("Unsuccessful Move")
                    # else:
                    #     print("Invalid Direction")

            if self.maze.can_move_to(self.maze.location[0], self.maze.location[1]) == True:
                if self.maze.is_exit(self.maze.location[0], self.maze.location[1]) == False:
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = "P"
                else:
                    running = False
                    print("Exit Reached")
                    pygame.quit()
                    quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            running = False
            
            # if running == True:
            #     print(self.maze.location)