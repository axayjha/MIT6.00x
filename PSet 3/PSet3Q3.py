def getGuessedWord(secretWord, lettersGuessed):
    
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result = result + letter
        else:
            result = result + '_'
    return result