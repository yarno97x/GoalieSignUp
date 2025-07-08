from bs4 import BeautifulSoup

from GoalieSignUp.data import mock_game
from data import mock
from game import Game

def htmlparser(string):
    soup = BeautifulSoup(string, 'html.parser')
    gameslist = soup.find('div', class_='games-list')

    if not gameslist : # Returns empty list if it can't find gameslist
        return []

    gamerow = gameslist.find_all('a', class_='game-row')
    liste = []
    for game in gamerow:
        title = game.find('div', class_='title').text
        fulldate = game.find('span', class_='date').text
        date, _, time = fulldate.split(', ')
        duration = game.find('span', class_='length').text
        calibre = game.find('span', class_='calibre').text
        liste.append(Game(title=title, date=date, time=time, duration=duration, calibre=calibre))
    return liste

def parameters(Game, string):
    soup = BeautifulSoup(string, 'html.parser')
    location = soup.find('div', class_='title').text
    pay = soup.find('div', class_='fee').text
    gamedetails = soup.find('div', class_='details')
    infolist = gamedetails.find_all('div', class_='info')
    gametype = infolist[0].text
    gender = infolist[2].text
    Game.setAll(location, pay, location, gametype, gender)


if __name__ == "__main__" :
    roger = htmlparser(mock)
    parameters(roger[0], mock_game)
    print(roger[0])