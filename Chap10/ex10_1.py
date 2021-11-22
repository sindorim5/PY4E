dictionary = dict()
dict_list = list()
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
		if words[1] not in dictionary:
			dictionary[words[1]] = 1
		else:
			dictionary[words[1]] += 1

for key, val in dictionary.items():
	dict_list.append((val, key))

dict_list = sorted(dict_list, reverse=True)

for val, key in dict_list[:1]:
	print(key, val)
