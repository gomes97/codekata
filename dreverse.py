n=input()
q=n
a=0
while q!=0:
	q=n/10
	r=n%10
	n=q
	a=a*10+r
print(a)
