from models.maze import Maze
from models.player import Player
from .game_move import GameMove
from views.maze_view import MazeView

class GameStart:

    def __init__(self, maze):
        self.maze = Maze(maze)

    def run(self):

        moving = GameMove(self.maze)

        moving.move()