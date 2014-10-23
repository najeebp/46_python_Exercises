def translate(listt):
	dictt= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	return map(lambda x:dictt[x],listt)
print translate(['and','new'])
