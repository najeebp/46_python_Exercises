def avg_length(filename):
	count = 0
	total_char_count = 0
	for word in open(filename,'r').read().split():
		total_char_count += len(word)
		count += 1
	print total_char_count,count
	return total_char_count/count
print avg_length('check_pal.txt')
