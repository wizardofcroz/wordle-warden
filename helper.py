from datetime import date
import csv
import textwrap

'''param message is a Wordle score of the format
   'Wordle 231 6/6\n ⬛🟩🟨⬛⬛\n 🟩🟩⬛🟨⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩🟩🟩'
'''


def to_five_char_line(text):
    return textwrap.wrap(text, width=5)


def is_five_letters(text):
    return all(len(line) <= 5 for line in str(text).splitlines())


def record_score(message):
    user = message.author.nick
    score = message.content.split(" ")[2][0]
    with open(f'{date.today().strftime("%d-%m-%Y")}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writeline([user, score])
    return score


def get_winners():
    with open(f'{date.today().strftime("%d-%m-%Y")}.csv', 'r') as file:
        reader = csv.reader(file)
        scores = [(x[0], x[1]) for x in reader]  # List of tuples in form (name, score)
        topScore = max(x[1] for x in scores)  # Get maximum score value from list of scores
        winners = set([x[0] for x in scores if x[1] == topScore])  # List of names with score == topScore
        return """Today's winners are {0}\n with a score of: {1}""".format("\n".join(winners), str(topScore))
