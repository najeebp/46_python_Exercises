import os
def speak_ICAO(string):
	d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot','g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima','m':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo','s':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey','x':'x-ray', 'y':'yankee', 'z':'zulu'}
	out=''
	for each in string:
		out += d[each]
		out += ' '
	print out
	a = out.replace(' ','_')
	print a
	# cmd = 'echo'+out
	os.system('say'+a)
speak_ICAO('abc')
