from datetime import date
from datetime import time
import datetime


def toFiveCharLine_( text ):
    fiveCharline = ''
    for i in range(0, len(text)):
        if (i%5 != 0):
            if text[i] == ' ':
                fiveCharline = fiveCharline + "\n"
            else: 
                fiveCharline = fiveCharline + text[i]
        else:
           fiveCharline = fiveCharline + text[i] + "\n"
    
    return fiveCharline

def toFiveCharLine( text ):
    fiveCharline = ''
    splitList = str(text).split(' ')
    for word in splitList:
        newWord = ''
        for i in range(0, len(word)):
            if (i%5 != 0 or i==0):
                newWord = newWord + word[i]
            else:
                newWord = newWord + word[i] + "\n"
        fiveCharline = fiveCharline + newWord + "\n"
    return fiveCharline



def isFiveLetters ( text ) : 
    isGood = True
    checkList = str(text).split('\n')

    for line in checkList:
        if len(line) > 5 :
            isGood = False
    return isGood

'''param message is a Wordle score of the format 
   'Wordle 231 6/6\n ⬛🟩🟨⬛⬛\n 🟩🟩⬛🟨⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩⬛⬛\n 🟩🟩🟩🟩🟩'
'''
def recordScore(message):
    today = date.today()
    user =  message.author.nick
    score = message.content.split(" ")[2][0]

    file1 = open(today.strftime("%d-%m-%Y")+'.txt', 'a' )
    #file1 = open(today.strftime("%d-%m-%Y") +'.txt', 'a' )
    file1.write(user+score+"\n")
    file1.close()

def getWinners():
    today = date.today()
    file1 = open(today.strftime("%d-%m-%Y") +'.txt', 'r' )
    
    scoresString = str(file1.read())
    scores = scoresString.split("\n")
  
    players = {}
    topScore = 10
    for s in scores:
        try:
            players.update({s[:-1]: int(s[-1])})
            if( int(s[-1]) < topScore):
                topScore = int(s[-1])
        except:
            nothing = true
    

    winners = ''
    for p in players.items():
        print(p+ " "+ p[0])
        if p[1] == topScore:
            winners = winners +"\n`"+ p[0] + "`"
    file1.close()

    return ("Today's winners are "+ winners +"\nwith a score of "+str(topScore))



