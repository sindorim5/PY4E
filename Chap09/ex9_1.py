count = 0
dictionary = dict()
fhand = open('words.txt')
for line in fhand:
	words = line.split()
	for word in words:
		count += 1
		if word in dictionary:
			continue
		dictionary[word] = count

print(dictionary)
