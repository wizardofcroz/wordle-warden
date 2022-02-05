from pickle import TRUE

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
        