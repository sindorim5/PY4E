cnt = 0
total = 0.0
max_num = 0
min_num = 0
while True:
	svalue = input("Enter a number: ")
	if svalue == 'done':
		break
	try:
		fvalue = float(svalue)
	except:
		print("Invalid input")
		continue
	if cnt == 0:
		max_num = fvalue
		min_num = fvalue
	if fvalue > max_num:
		max_num = fvalue
	if fvalue < min_num:
		min_num = fvalue
	cnt += 1
	total += fvalue

if cnt == 0:
	print("No Numbers Entered")
else:
	print(total, cnt, max_num, min_num)
