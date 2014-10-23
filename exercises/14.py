def length_list(list):
	length_list = []
	for element in list:
		length_list.append(len(element))
	return [(x,y) for x in list for y in length_list if list.index(x)==length_list.index(y)] 
print length_list(['spark','leela','python'])