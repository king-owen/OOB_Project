import pytest
from models.player import Player

@pytest.fixture
def test_player():
    return Player()

def test_bag(test_player):
    #checks to see if Player class has the attribute 'backpack'
    assert hasattr(test_player,'backpack')

def test_pickup(test_player):
    #checks to see if Player class has the method appendItem
    assert hasattr(test_player,'appendItem')
