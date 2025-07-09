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

def test_convert_time_simple_format() :
    assert converttime("9:00PM") == (9 + 12) * 60
    assert converttime("6:00AM") == 6 * 60
    assert converttime("11:00PM") == (11 + 12) * 60

def test_convert_time_twelve_pm() :
    assert converttime("12:21PM") == 12 * 60 + 21

def test_convert_time_twelve_am() :
    assert converttime("12:36AM") == 36

def test_check_heure_simple_format() :
    assert not checkheure("9:00PM", "7:00PM")
    assert checkheure("11:00AM", "2:00PM")

def test_check_heure_twelve_am() :
    assert checkheure("12:00AM", "11:00AM")
    assert checkheure("12:00AM", "11:00PM")

def test_check_heure_twelve_pm() :
    assert not checkheure("12:00PM", "11:00AM")
    assert checkheure("12:00PM", "11:00PM")
