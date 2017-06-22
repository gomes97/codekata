s=raw_input()
s1=raw_input()
l=len(s)
l1=len(s1)
if(l==l1):
	for i in range(l):
		for j in range(i+1,l):
			if(s[i]==s[j]):
				if(s1[i]==s1[j]):
					print("isomarpic")
				else:
					print("not a isomorpic")
else:
	print("not a isomorpic")
