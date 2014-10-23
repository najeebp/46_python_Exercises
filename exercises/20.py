def translate(string):
	out = []
	dictt = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	string_list = string.split()
	for element in string_list:
		out.append(dictt[element])
	return ' '.join(out)
print translate('merry christmas and happy new year')

