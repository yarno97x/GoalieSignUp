class Game :
    def __init__(self, title, date, time, duration, calibre):
        self.title = title
        self.date = date
        self.time = time
        self.duration = duration
        self.calibre = calibre

    def __repr__(self):
        return f"{self.title}, {self.date}, {self.time}, {self.duration}, {self.calibre}"