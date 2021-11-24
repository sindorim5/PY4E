# Finding Numbers in a Haystack

import re
fname = "regex_sum_1412956.txt"
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	quit()
numlist = list()
for line in fhand:
	line = line.rstrip()
	num = re.findall('([0-9]+)', line)
	if len(num) > 0:
		for value in num:
			numlist.append(int(value))
print(sum(numlist))
