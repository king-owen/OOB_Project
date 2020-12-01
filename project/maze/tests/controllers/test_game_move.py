import pytest
from project.maze.controllers.game_move import GameMove

@pytest.fixture()
def test_maze():
    return GameMove('Maze','Maze',0,0)

def test_maze_controller(test_maze):
    assert hasattr(test_maze, 'maze')
    assert hasattr(test_maze, 'name')
    assert hasattr(test_maze, 'start_time')
    assert hasattr(test_maze, 'end_time')
    assert hasattr(test_maze, 'timer')
    assert hasattr(test_maze,'move')




