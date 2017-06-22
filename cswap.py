s=raw_input()
l=len(s)
li=[]
for i in range(0,l,2):
	li.append(s[i+1])
	li.append(s[i])
s1=''.join(li)
print(s1)
