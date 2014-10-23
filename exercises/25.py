import re
def make_ing_form(string):
	strr = ''
	check = re.search(r'(\w[aeiou]\w$)',string)
	if string.endswith('ie'):
		strr = string[:len(string)-2] + 'ying'
	elif string.endswith('e'):
		strr = string[:len(string)-1] + 'ing'
	elif check:
		strr = string + string[-1] + 'ing'
	else:
		strr = string + 'ing'
	return strr
print make_ing_form('lie')