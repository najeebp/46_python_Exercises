def generate_n_chars(n,c):
	output = ' '
	for element in range(n):
		output += c
	return output
print generate_n_chars(5,'x')
