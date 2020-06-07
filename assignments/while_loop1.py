n=1
while n<=100:
	print(n , end=", ")
	n=n+1
print()
#omitting mode3
n=1
while n<=100:
	if n%3==0:
		n=n+1
	else:
		print(n)
		n=n+1
#omitting mode 5
n=1
while n<=100:
	if n%5==0:
		n=n+1
		print()
	else:
		print(n,end=",")
		n=n+1
#omitting both mode 3 & 5
n=1
while n<=100:
	if (n%3 and n%5)==0:
		n=n+1

	else:
		print(n,end=",")
		n=n+1
	print()
#another method for the problem above using or function
n = 1
while n <= 100:
	if (n % 3 or n % 5) == 0:
		n = n + 1
		print()
	else:
		print(n, end=",")
		n = n + 1