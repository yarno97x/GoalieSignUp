import pytest
from game import Game
from preferences import *

@pytest.fixture
def game() :
    c = Game("Roger", "July 7", "9:00PM", "45 min", Calibre.A, "url")
    c.setAll("loc", "$50", "add", GameType.BALLGAME, Gender.EITHER)
    return c

def test_check_calibre() :
    assert checkcalibre(Calibre.AA)
    assert checkcalibre(Calibre.A)
    assert checkcalibre(Calibre.BPLUS)
    assert not checkcalibre(Calibre.B)

def test_check_date() :
    pass

def test_convert_time() :
    assert converttime("9:00PM") == (9+12)*60
    assert converttime("6:00AM") == 6*60
    assert converttime("11:00PM") == (11+12)*60

def test_check_heure() :
    assert not checkheure("9:00PM", "7:00PM")
    assert checkheure("11:00AM", "2:00PM")
