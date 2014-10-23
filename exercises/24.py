def make_3sg_form(string):
	strr = ''
	if string.endswith('y'):
		strr =string[:len(string)-1]+'ies'
	elif string.endswith('o') or string.endswith('s') or string.endswith('x') or string.endswith('z'):
		strr = string[:len(string)-1]+'es'
	elif string.endswith('ch') or string.endswith('sh'):
		strr = 	 string[:len(string)-2]+'es'
	else:
		strr = string + 's'
	return strr
print make_3sg_form('try')