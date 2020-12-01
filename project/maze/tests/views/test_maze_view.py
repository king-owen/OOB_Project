import pytest
from project.maze.views.maze_view import MazeView

@pytest.fixture()
def test_maze():
    return MazeView('Maze','Maze')

def test_maze_view(test_maze):
    assert hasattr(test_maze, 'maze')
    assert hasattr(test_maze, 'name')
    assert hasattr(test_maze, 'start_time')
    assert hasattr(test_maze, 'timer')





