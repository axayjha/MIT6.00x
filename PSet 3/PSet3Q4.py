def getAvailableLetters(lettersGuessed):
    import string
    lettersLeft = string.ascii_lowercase
    for letter in lettersGuessed:
        lettersLeft = lettersLeft.replace(letter,'')
    return lettersLeft