import pytest
from project.maze.models.maze import Maze
from project.maze.models.player import Player
""""""
@pytest.fixture
def test_maze():
    """Fixture for all maze tests takes a text file"""
    return Maze("maze.txt")

def test_content(test_maze):
    """Checks to see if Maze has an attribute content"""
    assert hasattr(test_maze,'content')

def test_player(test_maze):
    """Checks to see if Maze has an attribute Player"""
    assert hasattr(test_maze,'player')

def test_location(test_maze):
    """Checks to see if Maze has an attribute location and that it is a tuple"""
    assert hasattr(test_maze,'location')
    assert type(test_maze.location) == tuple

def test_can_move_to(test_maze):
    """Checks to see if Maze has an attribute can_move_to and that it returns the correct value for an empty space
    and a wall X """
    assert hasattr(test_maze,'can_move_to')
    assert test_maze.can_move_to([(x, y.index(" ")) for x, y in enumerate(test_maze.content) if " " in y][0][0],[(x, y.index(" ")) for x, y in enumerate(test_maze.content) if " " in y][0][1]) == True
    assert test_maze.can_move_to([(x, y.index("X")) for x, y in enumerate(test_maze.content) if "X" in y][0][0],[(x, y.index("X")) for x, y in enumerate(test_maze.content) if "X" in y][0][1]) == False


def test_display(test_maze):
    """Checks to see if Maze has a display attribute"""
    assert hasattr(test_maze,'display')


def test_find_random_spot(test_maze):
    """Checks to see if Maze has a find_random_spot attribute and that it can find an empty random spot and verify"""
    assert hasattr(test_maze,'find_random_spot')
    plot = test_maze.find_random_spot()
    test_maze.can_move_to(plot[0],plot[1]) == True

def test_exit(test_maze):
    """Checks to see if Maze has a is_exit attribute and verfiy if the exit is True """
    assert hasattr(test_maze,"is_exit")
    test_maze.location = [(x, y.index("E")) for x, y in enumerate(test_maze.content) if "E" in y][0]
    assert test_maze.is_exit(test_maze.location[0],test_maze.location[1]) == True





