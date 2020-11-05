import pygame
import pygame.locals

class GameMove:
    """Allows a player to move
    """

    def __init__(self, maze):
        """Takes a nested list and creates an instance of the GameMove class

        :param maze: A nested list of letters
        :type maze: nested list
        """
        self.maze = maze

    def move(self):
        """Allows for movement in pygame
        """
        pygame.init()

        running = True

        while running:
        """Loops through movement taking an input of wasd to move
        """

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
        """Checks what key is pressed
        """
                if event.type == pygame.KEYDOWN:
        """Checks if a key is pressed down
        """
                    if (keys[pygame.locals.K_w]):
        """Checks if w has been pressed
        """

                        if self.maze.can_move_to(self.maze.location[0]-1,self.maze.location[1]) == True:
        """Checks if the player can move to the spot and moves them if possible
        """
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0]-1,) + self.maze.location[1:]
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")


                    elif (keys[pygame.locals.K_a]):
        """Checks if a has been pressed
        """
                        if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]-1) == True:
        """Checks if the player can move to the spot and moves them if possible
        """
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0], self.maze.location[1]-1,)
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")
                            

                    elif (keys[pygame.locals.K_s]):
        """Checks if s has been pressed
        """
                        if self.maze.can_move_to(self.maze.location[0]+1,self.maze.location[1]) == True:
        """Checks if the player can move to the spot and moves them if possible
        """
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0]+1,) + self.maze.location[1:]
                        #     print("Successful Move")
                        # else:
                        #     print("Unsuccessful Move")


                    elif (keys[pygame.locals.K_d]):
        """Checks if d has been pressed
        """
                        if self.maze.can_move_to(self.maze.location[0],self.maze.location[1]+1) == True:
        """Checks if the player can move to the spot and moves them if possible
        """
                            self.maze.content[self.maze.location[0]][self.maze.location[1]] = " "
                            self.maze.location = (self.maze.location[0], self.maze.location[1]+1,)
                    #         print("Successful Move")
                    #     else:
                    #         print("Unsuccessful Move")
                    # else:
                    #     print("Invalid Direction")


            if self.maze.can_move_to(self.maze.location[0], self.maze.location[1]) == True:
        """Checks if the player can move to the spot
        """
                if self.maze.is_exit(self.maze.location[0], self.maze.location[1]) == False:
        """If the spot being moved to is not the exit, replaces the spot with the player
        """
                    self.maze.content[self.maze.location[0]][self.maze.location[1]] = "P"
                else:
        """If the spot is the exit then says exit is reached and quits
        """
                    running = False
                    print("Exit Reached")
                    pygame.quit()
                    quit()


            for event in pygame.event.get():
        """Checks if the x button is hit and if so exits the game
        """
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            running = False
            