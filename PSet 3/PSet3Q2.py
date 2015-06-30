def isWordGuessed(secretWord, lettersGuessed):
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True