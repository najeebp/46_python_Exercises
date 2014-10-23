import re
def correct(strings):
	a = re.sub(r'\s+',' ',strings)
	b = re.sub(r'\.','. ',a)
	print b
correct('thiis    iss cool.indeed')
