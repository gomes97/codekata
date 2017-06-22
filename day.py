def workingday(day):
	if day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or  day=="Friday":
		return "true"
	else:
		return "false"
print(workingday(raw_input("enter day")))
