def sum(list):
	summ = 0
	for element in list:
		summ += element
	return summ
def multiply(list):
	product = 1
	for element in list:
		product *=element
	return product
print sum([1,2,3,4])
print multiply([1,2,3,4])