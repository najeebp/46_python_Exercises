def overlapping(list1,list2):
	flag = 1
	for element1 in list1:
		if element1 in list2:
				flag = 0
				return True
	if flag ==1:
		return False
print overlapping([1,2,3],[6,8,9])