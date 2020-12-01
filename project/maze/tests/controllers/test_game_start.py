import pytest
from project.maze.controllers.game_start import GameStart

@pytest.fixture()
def test_maze():
    return GameStart('maze.txt','Maze')

def test_maze_controller(test_maze):
    assert hasattr(test_maze, 'maze')
    assert hasattr(test_maze, 'name')
    assert hasattr(test_maze, 'run')





