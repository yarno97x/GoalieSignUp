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

params = {
    "MaxTime" : "9:00PM",
    "MaxDuration" : 45,
    "Calibres" : [Calibre.BPLUS, Calibre.A, Calibre.AA]
}

# Date heure duration calibre
def check(game):
    pass

def checkdate(string):
    pass

def checkheure(string):
    time = params["MaxTime"]


def converttime(time) :
    heure = time[:-2]
    tab = heure.split(":")
    minutes = int(tab[0]) * 60 + int(tab[1])

    if "PM" in time :
        return minutes + 12 * 60
    return minutes

def checkduration(string):
    pass

def checkcalibre(calibre):
    return calibre != Calibre.B

# Tout le reste
def checkRest(game):
    pass