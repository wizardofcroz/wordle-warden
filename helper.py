from datetime import date
from datetime import time
import datetime
import textwrap
import csv
import glob
import os

from numpy import average

def to_five_char_line(text):
    return textwrap.wrap(text, width=5)


def is_five_letters(text):
    return all(len(line) <= 5 for line in str(text).splitlines())


def record_score(message):
    user = message.author.nick
    score = message.content.split(" ")[2][0]
    with open(f'./data/{date.today().strftime("%d-%m-%Y")}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writeline([user, score])
    return score


def get_winners():
    with open(f'./data/{date.today().strftime("%d-%m-%Y")}.csv', 'r') as file:
        reader = csv.reader(file)
        scores = [(x[0], x[1]) for x in reader]  # List of tuples in form (name, score)
        topScore = max([x[1] for x in scores])  # Get maximum score value from list of scores
        winners = set([x[0] for x in scores if x[1] == topScore])  # List of names with score == topScore
        return """Today's winners are {0}\n with a score of: {1}""".format("\n".join(winners), str(topScore))

def get_leaderboard():
    def get_average_by_player(events,player):
        return average([event[2] for event in events if event[1] == player]) # get the average of all their scores ever
    
    files = glob.glob('./data/*.csv')
    data = dict()  # {username: [{date:score}]}
    events = []
    for file in files:
        with open(file,'r') as fh:
            reader = csv.reader(fh)
            for row in reader:
                # Appends a tuple to list in form: (filename,username,score)
                events.append(str(os.path.basename(fh.name),str(row[0]),int(row[1])))
    players = [] # need empty definition to not have undefined error below
    players = [event[1] for event in events if event[1] not in players] # Get list of all players
    average_scores = sorted({player:get_average_by_player(events,player) for [player] in players}.items, key=lambda item: item[1]) # Get a sorted dict of players and scores
    return """Leaderboard:\n{0}""".format('\n'.join([f'{i} : {average_scores[i]}'] for i in average_scores))
