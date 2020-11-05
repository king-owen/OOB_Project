from models.maze import Maze
from models.player import Player
from .game_move import GameMove
from views.maze_view import MazeView

class GameStart:
    """Creates an instance of the the game to be run
    """

    def __init__(self, maze):
        """instantiates the game and applies a Maze instance as an attribute.

        :param maze: An instance of the Maze class
        :type maze: class
        """
        self.maze = Maze(maze)

    def run(self):
        """Starts the actual game by creating a view of the maze attribute tied to a variable
        and then running the display_maze method to show the view.
        """

        start = MazeView(self.maze)

        start.display_maze()