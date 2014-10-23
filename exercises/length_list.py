def length_list(list):
	length_listt = []
	for element in list:
		count = 0
		for each in element:
			count += 1
		length_listt.append(count)
	return zip(list,length_listt)
print length_list(['asian','spark','python'])
