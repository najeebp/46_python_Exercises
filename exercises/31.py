def map(f,listt):
	output = []
	for element in listt:
		output.append((f(element)))
	return output
def filter(f,listt):
	output=[]
	for element in listt:
		if f(element)==True:
			output.append(element)
	return output
def reduce(f,listt):
	output=[]
	for element in listt:
		if f(element)==True:
			output.append(element)
	return output

print filter(lambda x:len(x)>3 , ['spark','a'])
print map(len,['asian','nippon'])