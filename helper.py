from datetime import date


def toFiveCharLine_(text):
    fiveCharline = ''
    for i in range(0, len(text)):
        if (i % 5 != 0):
            if text[i] == ' ':
                fiveCharline = fiveCharline + "\n"
            else:
                fiveCharline = fiveCharline + text[i]
        else:
            fiveCharline = fiveCharline + text[i] + "\n"

    return fiveCharline


def toFiveCharLine(text):
    fiveCharline = ''
    splitList = str(text).split(' ')
    for word in splitList:
        newWord = ''
        for i in range(0, len(word)):
            if (i % 5 != 0 or i == 0):
                newWord = newWord + word[i]
            else:
                newWord = newWord + word[i] + "\n"
        fiveCharline = fiveCharline + newWord + "\n"
    return fiveCharline


def isFiveLetters(text):
    return all(len(line) <= 5 for line in str(text).splitlines())


'''param message is a Wordle score of the format
   'Wordle 231 6/6\n ⬛🟩🟨⬛⬛\n 🟩🟩⬛🟨⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩🟩🟩'
'''


def recordScore(message):
    today = date.today()
    user = message.author.nick
    score = message.content.split(" ")[2][0]

    with open(today.strftime("%d-%m-%Y") + '.txt', 'a') as file:
        file.write(user + score + "\n")


def getWinners():
    today = date.today()
    with open(today.strftime("%d-%m-%Y") + '.txt', 'r') as file:
        scores = file.readlines()

        players = {}
        topScore = 10
        for s in scores:
            try:
                players.update({s[:-1]: int(s[-1])})
                if (int(s[-1]) < topScore):
                    topScore = int(s[-1])
            except:
                nothing = True

        winners = ''
        for p in players.items():
            if p[1] == topScore:
                winners = winners + "\n`" + p[0] + "`"

    return ("Today's winners are " + winners + "\nwith a score of " + str(topScore))
