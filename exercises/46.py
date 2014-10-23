import urllib
def alternade(string):
	q = []
	first = string[ : :2]
	second = string[1: :2]
	f = urllib.urlopen(' http://www.puzzlers.org/pub/wordlists/unixdict.txt')
	for each_word in f:
		if each_word.rstrip() == first:
			first1 = each_word
		elif each_word.rstrip() == second:
			second1 = each_word
	print string + ": makes" + ' "'+first1 + '"' + ' and '+ '"' + second1 + '"'	
alternade("board")
