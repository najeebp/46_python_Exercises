def reverse(string):
	return string[::-1]
print reverse('spark')
def reverse_2(string):
	str=''
	length = len(string)
	for element in string:
		str += string[length-1]
		length -= 1
	return str
print reverse_2('spark')
