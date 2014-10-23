def palindrome(string):
	check1 = ''
	for char in string.lower():
		if char ==' ':
			pass
		else:
			check1 +=char
	if check1 == check1[::-1]:
		print True
	
palindrome('Rise to vote sir')