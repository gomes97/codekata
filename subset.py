a1=[1,2,4]
a2=[1,2,4,7]
c=0

for i in range(len(a2)):
	if(a1[0]==a2[i]):
		for j in range(len(a1)):
			if(a1[j]==a2[i]):
				i=i+1
				c=c+1
if(c==len(a1)):
	print("subset")
else:
	print("not a subset")
