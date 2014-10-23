def filter_long_words(listt,n):
	return filter(lambda x:len(x) > n,listt)
print filter_long_words(['spark support','asian','info'],4)