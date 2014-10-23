def max(a,b):
        if a>b:
                return a
        else:
                return b

def max_list(z):
	print reduce(max,z)
max_list([4,5,6,1,2])
