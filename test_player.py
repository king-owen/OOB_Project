import pytest
from player import Player
#
# @pytest.fixture



def test_bag(Player):
    #checks to see if Player class has the attribute 'backpack'
    assert hasattr(Player,'backpack')

def test_pickup(Player):
    #checks to see if Player class has the method appendItem
    assert hasattr(Player,'appendItem')
