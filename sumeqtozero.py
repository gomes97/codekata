n=input("enter n")
a=[]
flag=0
for i in range(n):
	a.append(input())
for i in range(n):
	for j in range(n):
		if(a[i]+a[j]==0):
			print("the sum is zero")
			flag=1;
if (flag==0):
	print("the sum is not equal to zero")
