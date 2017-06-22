s=raw_input()
s1=s[::-1]
li=[]
h=[]
for i in range(len(s1)):
	li.append(s1[i])
for i in range(len(li)):
	if li[i]=='a' or li[i]=='e' or li[i]=='i' or li[i]=='o' or li[i]=='u':
		li[i]=' '

h=''.join(li).split()
print(''.join(h))
