from enum import Enum

class GameType(Enum):
    BALLGAME = "Ball Game"
    FIVEVFIVE = "5v5"
    THREEVTHREE = "3v3"

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    EITHER = "Either"

class Calibre(Enum):
    C = "C"
    B = "B"
    BPLUS = "B+"
    A = "A"
    AA ="AA"

# Date heure duration calibre
def check(game):
    pass

# Tout le reste
def checkRest(game):
    pass