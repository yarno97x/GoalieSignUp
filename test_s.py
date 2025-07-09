import pytest
from game import Game
from preferences import Calibre, GameType, Gender
from preferences import check, checkcalibre
from params import params

@pytest.fixture
def game() :
    c = Game("Roger", "July 7", "9:00PM", "45 min", Calibre.A, "url")
    c.setAll("loc", "$50", "add", GameType.BALLGAME, Gender.EITHER)
    return c

def test_check_calibre(game) :
    assert checkcalibre(Calibre.AA)
    assert checkcalibre(Calibre.A)
    assert checkcalibre(Calibre.BPLUS)
    assert not checkcalibre(Calibre.B)



