def Semordnilap(filename):
	output = []
	for element in open(filename,'r').read().split():
		for element2 in open(filename,'r').read().split():
			if element == element2[::-1]:
				output.append(element)
	return output
print Semordnilap('check_pal.txt')