import random

answer = str(random.randint(1000,9999))
answerList = list(answer)
#print(answerList)


guess = input('Guess a 4-digit number:\n')
guessList = list(guess)
#print(guessList)

if int(guess) < 1000 or int(guess) > 9999:
	print('Not a 4-digit number. cmon dude')
else:
	while int(guess) != int(answer):
		guessList = list(guess)
		cows = 0
		bulls = 0
		for i in range(4):
			if guessList[i] == answerList[i]:
				cows += 1
			elif guessList[i] in answerList:
				bulls += 1
		print(str(cows) + ' cows,' + str(bulls) + ' bulls')
		guess = input('Guess Again\n')

if int(guess) == int(answer):
	print('Correct. You did it. No way. Yeah you')
