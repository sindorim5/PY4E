import re
count = 0
fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	quit()
regex = input("Enter a regular expression: ")
for line in fhand:
	line = line.rstrip()
	matched = re.findall(regex, line)
	if len(matched) > 0:
		count += 1

print(fname, "had", count, "lines that matched", regex)
