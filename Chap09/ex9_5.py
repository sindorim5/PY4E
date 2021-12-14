dictionary = dict()
fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	quit()
for line in fhand:
	words = line.split()
	if len(words) < 3 or words[0] != 'From':
		continue
	else:
		start = words[1].find("@")
		addr = words[1][start+1:]
		if addr not in dictionary:
			dictionary[addr] = 1
		else:
			dictionary[addr] += 1

print(dictionary)
