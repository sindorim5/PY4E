import re
fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	quit()
numlist = list()
for line in fhand:
	line = line.rstrip()
	num = re.findall('^New Revision: ([0-9.]+)', line)
	if len(num) > 0:
		for value in num:
			value = float(value)
		numlist.append(value)
print(sum(numlist)/len(numlist))

