n=input("enter n ")
k=input("enter k")
l=[]
l1=[]
for i  in range(n):
	l.append(input())
for i in range(k+1,n):
	l1.append(l[i])
for i in range(k+1):
	l1.append(l[i])
print(l1)
