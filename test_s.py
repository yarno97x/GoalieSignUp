import pytest
from game import Game
from preferences import Calibre, GameType, Gender

@pytest.fixture
def game() :
    c = Game("Roger", "July 7", "9:00PM", "45 min", Calibre.A, "url")
    c.setAll("loc", "$50", "add", GameType.BALLGAME, Gender.EITHER)
    return c

def test_check_game(game) :
    pass

