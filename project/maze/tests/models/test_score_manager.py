import pytest
from .models.score_manager import ScoreManager
from .models.score import Score

@pytest.fixture
def high():
    return Score("Albert", 0, '10:43:29.392756')


@pytest.fixture
def low():
    return Score("Barry", 999, '10:44:38.491000')

@pytest.fixture
def manager():
    return ScoreManager()

def test_manager_len(manager, high):
    manager.add_score(high)
    assert len(manager) == 1

def test_manager_scores_property():
    assert type(ScoreManager.scores) == property


def test_manager_remove_score(manager,low):
    manager.add_score(low)
    manager.remove_score(low)
    assert len(manager) == 0





def test_manager_serialize(manager, high, low):
    manager.add_score(high)
    manager.add_score(low)

    assert manager.serialize() == {'scores': [
        {"name": "Albert", "score": 0, "date": '10:43:29.392756'},
        {"name": "Barry", "score": 999, "date": '10:44:38.491000' },
    ]}


