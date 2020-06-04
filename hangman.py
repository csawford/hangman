# Set variables
turns = 6
winner = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
gameAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

# Load or generate random word
word = 'coronation street'


# Function to convert a string to a list of chars
def split(word):
    return list(word)


# Function to display the puzzle word
def displayWord():
    print("\n\n")
    for x in puzzleWord:
        if x in gameAlphabet:
            print('-', end='')
        else:
            print(x, end='')
    print("\n\n")


# Function to check the players guess
def checkGuess(guess):
    global turns
    global winner
    # if players guess is a word (more than one letter) check to see if matches puzzleWord
    if len(guess) > 1:
        if split(guess) == puzzleWord:
            winner = True
            return
        else:
            print('Sorry, that is not the correct word.')
            turns -= 1
            return
    if guess not in alphabet:
        print('Please enter a valid letter.')
        return

    if guess not in gameAlphabet:
        print('You have already guessed that letter, Try again.')
        return

    if guess in puzzleWord:
        print('correct guess')
        gameAlphabet.remove(guess)
        return
    elif guess not in puzzleWord:
        print('That letter is not in the word!')
        gameAlphabet.remove(guess)
        turns -= 1
        return


puzzleWord = split(word)
while (turns > 0 and winner == False):
    displayWord()
    print('You have ', turns, ' guesses left.')
    # input letter guess
    lguess = input('Choose a letter or guess the answer: ')

    checkGuess(lguess)

if winner == True:
    print('Congratulations, you completed the puzzle!')
else:
    print('You have run out of turns!')
