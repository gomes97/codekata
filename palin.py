n=input()
q=n
m=n
a=0
while q!=0:
	q=n/10
	r=n%10
	n=q
	a=a*10+r
if a==m:
	print("palindrome")
else:
	print("not a palindome")
	
