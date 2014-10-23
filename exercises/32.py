def pal_recog(filename):
	for each_line in open(filename,'r').read().split():
		if each_line == each_line[::-1]:
			print  each_line
pal_recog('check_pal.txt')