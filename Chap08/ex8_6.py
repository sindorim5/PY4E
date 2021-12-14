numlist = []
while True:
	svalue = input("Enter a number: ")
	if svalue == 'done':
		break
	try:
		fvalue = float(svalue)
	except:
		print("Invalid input")
		continue
	numlist.append(fvalue)
print("Maximum:", max(numlist))
print("Minimum:", min(numlist))
