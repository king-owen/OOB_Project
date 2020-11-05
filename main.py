from models.maze import Maze 
from controllers.game_start import GameStart

if __name__ == "__main__":

  game = GameStart("maze.txt")
  game.run()