def translate(string):
	sample = []
	vowels = 'aeiou'
	for element in string.split():
		re=''
		for elementt in element:
			if elementt not in vowels:
				re += elementt+'o'+elementt
			else:
				re +=elementt
		sample.append(re)
		
	return ' '.join(sample)
print translate('this is fun')
