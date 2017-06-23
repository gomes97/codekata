import sys
l=[]
for i in range(3):
	l.append(input().split())
print(l)
for i in range(len(l)):
  for j in range(3):
    sys.stdout.write(l[i][j])
