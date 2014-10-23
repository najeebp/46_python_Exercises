def hapax(filename):
	dictt = {}
	for element in open(filename,'r').read().split():
		dictt[element] = dictt.get(element,0)+1
	for element in dictt:
		if dictt[element] == 1:
			print element
hapax('check_pal.txt')