class Game :
    def __init__(self, title, date, time, duration, calibre):
        self.title = title
        self.date = date
        self.time = time
        self.duration = duration
        self.calibre = calibre

    def __repr__(self) :
        return f"'{self.title}, {self.date}, {self.time}, {self.duration}, {self.calibre}'"
    
    def set_arena(self, arena) :
        self.arena = arena

    def to_html(self) :
        string = "<div style='border: 1px solid white; padding-left: 10px; margin-bottom: 5px;'>"
        string += f"<h3 style='margin-bottom: 0px'>{self.title}</h3>"
        string += f"<b>{self.arena if self.arena else "No Specified Location"}</b>"
        string += f"<p>{self.date}, {self.time}</p> "
        string += f"<p>{self.duration}, {self.calibre}</p></div>"
        return string

    def setAll(self, location, pay, address, gametype, gender) :
        self.location = location
        self.pay = pay
        self.address = address
        self.gametype = gametype
        self.gender = gender