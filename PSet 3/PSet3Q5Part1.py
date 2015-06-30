def hangman(secretWord):
   
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-----------"

    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessesLeft = 8
    while guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print "-----------"
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
            if isWordGuessed(secretWord, lettersGuessed) == True:
             print "Congratulations, you won!"
             break
        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft = guessesLeft - 1
            lettersGuessed.append(letter)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."
