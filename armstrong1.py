n1=input()
n2=input()
q=n1
a=0
for n in range(n1,n2):
	a=0
	m=n
	q=n
	while q!=0:
		q=n/10
		r=n%10
		n=q
		a=a+r*r*r
	if a==m:
		print(a)
