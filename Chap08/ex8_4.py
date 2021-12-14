fhand = open("romeo.txt")
list = []
for line in fhand:
	words = line.split()
	for word in words:
		if word in list:
			continue
		list.append(word)
print(sorted(list))
