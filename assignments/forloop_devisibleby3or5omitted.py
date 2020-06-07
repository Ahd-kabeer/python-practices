j=1
x=1
for i in range (100):
	if (x%3==0 or x%5==0):
		x=x+1
	else:
		print(x, end=",")
		x=x+1
