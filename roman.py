rom=["I","II","III","IV","V","VI","VII","VIII","IX","X"]
val=[1,2,3,4,5,6,7,8,9,10]
x=raw_input("enter a roman letter")
y=len(rom)
for i in range(y):
	if(rom[i]==x):
		print(val[i])
