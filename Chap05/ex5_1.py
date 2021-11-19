cnt = 0
total = 0.0
while True:
	svalue = input("Enter a number: ")
	if svalue == 'done':
		break
	try:
		fvalue = float(svalue)
	except:
		print("Invalid input")
		continue
	cnt += 1
	total += fvalue

if cnt == 0:
	print("No Numbers Entered")
else:
	print(total, cnt, total/cnt)
