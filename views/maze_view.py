from controllers.game_move import GameMove
import pygame
import pygame.locals

class MazeView:

    def __init__(self, maze):
        self.maze = maze

    def display_maze(self):

        pygame.init()

        clock = pygame.time.Clock()

        running = True

        while running:
            clock.tick(60)

            # for i in self.maze.content:
            #     print(i)

            window = pygame.display.set_mode(((len(self.maze.content[0])*50), (len(self.maze.content*50))))
            window.set_colorkey((255, 255, 255))
            window.fill((211, 211, 211))


            # rectangle_surface = pygame.Surface((5, 5))
            # rect_shape = pygame.draw.rect(rectangle_surface, (0, 0, 0), (0, 0, 0, 0))
            # rectangle_surface.set_colorkey((255, 255, 255))
            # window.blit(rectangle_surface.convert(), (0, 0))

            for idx, value in enumerate(self.maze.content):
                for jdx, jvalue in enumerate(value):
                    if jvalue == "X":
                        rectangle_surface = pygame.Surface((50, 50))
                        rect_shape = pygame.draw.rect(rectangle_surface, (0, 0, 0), (0, 0, (jdx * 50),  (idx * 50)))
                        rectangle_surface.set_colorkey((255, 255, 255))
                        window.blit(rectangle_surface.convert(), ((jdx * 50), (idx * 50)))
                
                    if jvalue == "P":
                        rectangle_surface = pygame.Surface((50, 50))
                        rect_shape = pygame.draw.rect(rectangle_surface, (0, 0, 255), (0, 0, (jdx * 50),  (idx * 50)))
                        rectangle_surface.set_colorkey((255, 255, 0))
                        window.blit(rectangle_surface.convert(), ((jdx * 50), (idx * 50)))
                
                    if jvalue == "E":
                        rectangle_surface = pygame.Surface((50, 50))
                        rect_shape = pygame.draw.rect(rectangle_surface, (0, 255, 0), (0, 0, (jdx * 50),  (idx * 50)))
                        rectangle_surface.set_colorkey((255, 0, 255))
                        window.blit(rectangle_surface.convert(), ((jdx * 50), (idx * 50)))
                
                    if jvalue == "key":
                        rectangle_surface = pygame.Surface((50, 50))
                        rect_shape = pygame.draw.rect(rectangle_surface, (255, 0, 0), (0, 0, (jdx * 50),  (idx * 50)))
                        rectangle_surface.set_colorkey((0, 255, 255))
                        window.blit(rectangle_surface.convert(), ((jdx * 50), (idx * 50)))

            pygame.display.update()

            moving = GameMove(self.maze)
            moving.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()