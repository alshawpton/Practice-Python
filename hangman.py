# you have to download sowpods.txt found at
# https://www.practicepython.org/solution/2016/10/15/30-pick-word-solutions.html

# function to generate random word from sowpods
def picksWord():
        import csv, random
        word_file = open('sowpods.txt','r')
        allWords = word_file.readlines()
        for i in range(len(allWords)):
                word = allWords[i]
                word = word.strip('\n')
                allWords[i] = word
        word = random.choice(allWords)
        return(word)


answer = list(picksWord())
answerKey = []
guessList = []
misses = 0
drawings = {1:' | ',2:' | \n 0 ',3:' | \n 0 \n | \n',4:' | \n 0 \n-|-\n',\
5:' | \n 0 \n-|-\n | \n', 6:' | \n 0 \n-|-\n | \n ^ '}

# creates the '_ _ _' answerkey output
for i in answer:
        answerKey += '_'

print(' '.join(answerKey),'\n')

print('Welcome to Hangman\n')


# keeps the game going until player wins or gets 6 wrong
while answerKey != answer and misses < 6:
	guess = input('Guess a Letter\n').upper()

# having a hard time figuring out how to take "enter key" and numbers without it messing up
#	if guess == '' or isinstance(int(guess),int) == True:
#		print('Please guess one letter')
#		continue

# doesn't accept multi letter answers
	if len(guess) > 1 or len(guess)<1:
		print('Please guess one letter')
		continue

# doesn't count letters already guessed
	if guess in guessList:
		print('Already guessed that letter')
		continue

# checks answer
	if guess in answer:
		for i in range(len(answer)):
			if guess == answer[i]:
				answerKey[i] = guess
	else:
		misses += 1
		if misses == 6:
			break
		print('Incorrect. You have %s lives left. Guess Again.' % (6 - misses))
		print(drawings[misses])

# prints current answer board
	print(' '.join(answerKey))
	guessList += guess

# prints result of the game
if answerKey == answer:
	print('You Win!')
elif misses == 6:
	print('\nYou dead\n')
	print(drawings[misses])
	print('The word was %s.' % (''.join(answer)))
