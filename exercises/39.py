import random
def guess_number():
	count = 0
	name = raw_input('Hello! What is your nam??\n')
	print 'Well, %s , I am thinking of a number between 1 and 20' %(name)
	inputt = int(input('Take a guess'))
	correct = random.randint(1,20)
	while correct != inputt:
		count += 1
		if inputt > correct:
			print 'Your guess is high'
		elif  inputt < correct:
			print ' your guess is low'
		inputt = int(input('Take a guess'))
	print 'Good job , %s! You guessed my number in a %d guesses' % (name,count) 
#guess_number()