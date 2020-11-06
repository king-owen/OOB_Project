import pytest
from maze import Maze

def test_content(Maze):
    assert hasattr(Maze,'content')

def test_player(Maze):
    assert hasattr(Maze,'player')

def test_location(Maze):
    assert hasattr(Maze,'location')
    assert type(Maze.location) == list

def test_can_move_to(Maze):
    assert hasattr(Maze,'can_move_to')

    #would need fixture for this one

def test_display(Maze):
    assert hasattr(Maze,'display')
    assert None

def test_find_random_spot(Maze):
    assert hasattr(Maze,'find_random_spot')

def test_lose(Maze):
        if self.content[line][column] == "E":
            if len(Maze.player.backpack) == 4:
                assert True

