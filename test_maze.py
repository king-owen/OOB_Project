import pytest
from models.maze import Maze
from models.player import Player

@pytest.fixture
def test_maze():
    return Maze("maze.txt")

def test_content(test_maze):
    assert hasattr(test_maze,'content')

def test_player(test_maze):
    assert hasattr(test_maze,'player')

def test_location(test_maze):
    assert hasattr(test_maze,'location')
    assert type(test_maze.location) == list

def test_can_move_to(test_maze):
    assert hasattr(test_maze,'can_move_to')

    #would need fixture for this one

def test_display(test_maze):
    assert hasattr(test_maze,'display')
    assert None

def test_find_random_spot(test_maze):
    assert hasattr(test_maze,'find_random_spot')

def test_lose(Maze):
        if self.content[line][column] == "E":
            if len(Maze.player.backpack) == 4:
                assert True

