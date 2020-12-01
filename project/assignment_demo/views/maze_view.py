from controllers.game_move import GameMove
import pygame
import pygame.locals
import sprites
import datetime
class Wall(pygame.sprite.Sprite):
    """ This is the wall sprite """
    def __init__(self):
        image = pygame.image.load('Sprites/wall.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()


class Play(pygame.sprite.Sprite):
    """ This is the wall sprite """
    def __init__(self):
        image = pygame.image.load('Sprites/player.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()

class Key(pygame.sprite.Sprite):
    """ This is the item sprite """
    def __init__(self):
        image = pygame.image.load('Sprites/key.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()

class Exit(pygame.sprite.Sprite):
    """ This is the wall sprite """
    def __init__(self):
        image = pygame.image.load('Sprites/door.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()

def create_text_surface(text):
    arial = pygame.font.SysFont('arial', 24)
    text_surface = arial.render(text, True, (0, 0, 0))

    return text_surface

class MazeView:
    """Creates a view of the maze in pygame
    """

    def __init__(self, maze, name):
        """Creates an instance of the maze view

        :param maze: An attribute of the maze class that is the nested lists for the maze
        :type maze: nested lists
        """
        self.maze = maze
        self.name = name
        start_time = datetime.datetime.now()
        self.start_time = (60 * start_time.minute) + start_time.second
        self.timer = 0

    def display_maze(self):
        """Starts pygame display, activates movement, and displays maze
        """

        pygame.init()

        clock = pygame.time.Clock()

        running = True

        while running:
            player = Play()
            key = Key()
            exit = Exit()
            wall = Wall()
        # """A loop that updates the maze with new information after moving and loops movement
        # """
            clock.tick(60)

            window = pygame.display.set_mode(((len(self.maze.content[0])*50), (len(self.maze.content*50) + 50)))
            window.set_colorkey((255, 255, 255))
            window.fill((211, 211, 211))

            for idx, value in enumerate(self.maze.content):
        # """loops through the outer list of the nested lists for the maze

        # :param valueinenumerate: an inner list
        # :type valueinenumerate: list
        # """
                for jdx, jvalue in enumerate(value):
        # """loops through the inner list of the nested lists for the maze

        # :param valueinenumerate: an inner list
        # :type valueinenumerate: list
        # :param jvalueinenumerate: One of the folowing strings "key, X,  , E"
        # :type jvalueinenumerate: string
        # """
                for jdx, jvalue in enumerate(value):
        # """loops through the inner list of the nested lists for the maze

        # :param valueinenumerate: an inner list
        # :type valueinenumerate: list
        # :param jvalueinenumerate: One of the folowing strings "key, X,  , E"
        # :type jvalueinenumerate: string
        # """
                    if jvalue == "X":
        # """Checks if a spot is an X and creates a black square to represent a wall for it in pygame
        # """
        #                 rectangle_surface = pygame.Surface((50, 50))
        #                 rect_shape = pygame.draw.rect(rectangle_surface, (0, 0, 0), (0, 0, (jdx * 50),  (idx * 50)))
        #                 rectangle_surface.set_colorkey((255, 255, 255))
                        window.blit(wall.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "P":
        # """Checks if a spot is the player or P and creates a blue square to represent it in pygame
        # """

        #                 rectangle_surface = pygame.Surface((50, 50))
        #                 rect_shape = pygame.draw.rect(rectangle_surface, (0, 0, 255), (0, 0, (jdx * 50),  (idx * 50)))
        #                 rectangle_surface.set_colorkey((255, 255, 0))

                        window.blit(player.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "E":
        # """Checks if a spot is the exit or E and creates a green square to represent it in pygame
        # """
        #                 rectangle_surface = pygame.Surface((50, 50))
        #                 rect_shape = pygame.draw.rect(rectangle_surface, (0, 255, 0), (0, 0, (jdx * 50),  (idx * 50)))
        #                 rectangle_surface.set_colorkey((255, 0, 255))
                        window.blit(exit.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "key":
        # """Checks if a spot is a key and creates a red square to represent it in pygame
        # """
        #                 rectangle_surface = pygame.Surface((50, 50))
        #                 rect_shape = pygame.draw.rect(rectangle_surface, (255, 0, 0), (0, 0, (jdx * 50),  (idx * 50)))
        #                 rectangle_surface.set_colorkey((0, 255, 255))
                        window.blit(key.image, ((jdx * 50), (idx * 50)))


            self.timer = 100 - (pygame.time.get_ticks() // 600)
            show_fps = create_text_surface(str(self.timer))
            timer = create_text_surface("Timer:")
            backpack = create_text_surface("Backpack:")
            window.blit(timer, (5, (len(self.maze.content*50) + 13)))
            window.blit(show_fps, (62, (len(self.maze.content*50) + 13)))

            window.blit(backpack, (100, (len(self.maze.content*50) + 13)))
            if len(self.maze.player.backpack) == 1:

                    rectangle_surface = pygame.Surface((24, 24))
                    rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                    rectangle_surface.set_colorkey((0, 255, 255))
                    window.blit(rectangle_surface.convert(), ((200, (len(self.maze.content*50) + 13))))

            if len(self.maze.player.backpack) == 2:

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((200, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((230, (len(self.maze.content*50) + 13))))

            if len(self.maze.player.backpack) == 3:

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((200, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((230, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((260, (len(self.maze.content*50) + 13))))

            if len(self.maze.player.backpack) == 4:

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((200, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((230, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((260, (len(self.maze.content*50) + 13))))

                rectangle_surface = pygame.Surface((24, 24))
                rect_shape = pygame.draw.rect(rectangle_surface, (250, 0, 0), (0, 0, (jdx * 24),  (idx * 24)))
                rectangle_surface.set_colorkey((0, 255, 255))
                window.blit(rectangle_surface.convert(), ((290, (len(self.maze.content*50) + 13))))

            pygame.display.update()

            moving = GameMove(self.maze, self.start_time, self.name, self.timer)
            moving.move()

        #     for event in pygame.event.get():
        # # """Checks if the X button is clicked in pygame and closes the game if it is
        # # """
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
