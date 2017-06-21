no=input("")
c=2
for i in range(2,no):
	if no%i!=0:
		c=c+1
	else:
		break
if c==no:
	print("prime")
else:
	print("not a prime")
