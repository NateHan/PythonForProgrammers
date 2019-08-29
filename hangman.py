
lives = 5

word = "Apple"

blank = " _ "

def runGame():
	blanks = []
	guessedLetters = []
	global lives
	for idx in range(len(word)):
		blanks.append(blank)
	while lives > 0 and blank in list(blanks):
		inputLetter = input("Word: {} - Lives = {} , Guessed letters: {} \n Guess a letter: ".format(blanks, lives, guessedLetters))
		if letterIsInWord(inputLetter.lower(), word.lower()):
			print("Correct!")
		else: 
			print("Wrong!")
			lives -= 1
		guessedLetters.append(inputLetter)
		genWordsAndBlanks(blanks, guessedLetters)
	else:
		if lives > 0: print("You win!")
		else: print("You died! The word was: {}".format(word))

def letterIsInWord(letter, word):
	if letter in list(word):
		return True
	else: 
		return False
		
def genWordsAndBlanks(blanks, guessedLetters):
	for idx in range(len(word)):
		if word[idx].lower() in guessedLetters:
			blanks[idx] = word[idx]
	return ''.join(blanks)
		

runGame()