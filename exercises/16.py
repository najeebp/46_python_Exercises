def filter_long_words(list,n):
	return [x for x in list if len(x) > n ]
print filter_long_words(['python','asi','spark support'],3)