fhand = open("mbox-short.txt")
count = 0
for line in fhand:
	words = line.split()
	if len(words) < 3 : continue # 최소 words = [0, 1, 2]
	if words[0] != 'From' : continue
	count += 1
	print (words[1])
print("There were", count, "lines in the file with From as the first word")

