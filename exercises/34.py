def char_freq_table():
	filename = raw_input("Enter the filename\n")
	dictt={}
	for element in open(filename,'r').read():
		dictt[element]=dictt.get(element,0)+1
	return dictt
print char_freq_table()