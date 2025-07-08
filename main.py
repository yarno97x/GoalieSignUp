from parser import htmlparser, match
from interactions import Session
from notify import notify

# 1 -> Selenium Log In
s = Session()
s.connect()
page = s.get_html()

# 2 -> Parse HTML and get games
games = htmlparser(page)
print(games)

# 3 -> Get Games \ if empty: refresh and #2
# 4 -> Compare with preferences \ if no matches: refresh and #2
# 5 -> For each match, click and get arena \ if no match: refresh and #2
games = []
signed_up = []
for game in games :
    s.click_on_game(game.link)
    
    # 6 ->  Sign up for match
    html = s.sign_up() 
    if match(html) :
        s.interested.click()
        signed_up.append(game)

    s.go_back() # Implement this

# 7 ->  Send notification
if len(signed_up) > 0 :
    notify(signed_up)
