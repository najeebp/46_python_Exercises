def enumeratee(filename):
	output = []
	fwrite = open('enumerate.txt','w')
	for each,q in enumerate(open(filename,'r').readlines()):
		fwrite.write('%d %s' % (each+1,q))
enumeratee('check_pal.txt')