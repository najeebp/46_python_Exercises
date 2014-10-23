def vowel_check(string):
	vowels='aeiou'
	for element in string:
		if element in vowels:
			print True
		else:
			print  False
vowel_check('sparkies')