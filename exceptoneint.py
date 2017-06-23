n=input()
l=[]
flag=0
for i in range(n):
	l.append(input())
for i in range(n):
	if(l.count(l[i])==1):
		print(l[i])
