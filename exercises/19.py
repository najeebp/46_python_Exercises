def bottles():
	for i in range(99,0,-1):
		 print "%d bottles of beer on the wall, %d bottles of beer.\nTake one down, pass it around, %d bottles of beer on the wall." % (i, i, i - 1)
bottles()