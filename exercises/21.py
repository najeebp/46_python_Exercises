def char_freq(string):
	dictt={}
	for element in string:
		dictt[element] = dictt.get(element,0)+1
	return dictt
print char_freq("abbabcbdbabdbdbabababcbcbab")