from unicodedata import name

from numpy import average


class WorldleEvent:
    def __init__(self,date:str,score:int):
        self.date = date
        self.score = score
class Player:
    def __init__(self,name:str):
        self.name = name
        self.scores = []
        self.average_score = 0
    def add_score(self,worldle_event:WorldleEvent):
        self.scores.append(worldle_event)
        self.average_score = average(self.scores)
#class Leaderboard:
#    def __init__(self):


class Row:
    def __init__(self, name: str, date: str, score: int):
        self.name = name
        self.date = date
        self.score = score
class Table:
    def __init__(self,rows: list(Row)):
        self.rows = rows