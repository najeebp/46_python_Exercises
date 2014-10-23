import string
def pangram(stringg):
	alphebet = set(string.ascii_lowercase)
	check = set(stringg.replace(" ", "").lower())
	if alphebet == check:
		print 'it is pangram'
	else:
		print 'it is not pangram'
pangram('The quick brown fox jumps over the lazy dog')