n=input()
q=n
a=0
m=n
while q!=0:
	q=n/10
	r=n%10
	n=q
	a=a+r*r*r
if a==m:
	print("armstrong no")
else:
	print("not a armstrong no")
