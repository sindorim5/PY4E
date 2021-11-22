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
	if len(words) < 6 or words[0] != 'From':
		continue
	end = words[5].find(":")
	hour = words[5][:end]
	if hour not in dictionary:
		dictionary[hour] = 1
	else:
		dictionary[hour] += 1

for key, val in dictionary.items():
	dict_list.append((key, val))

dict_list.sort()

for key, val in dict_list:
	print(key, val)
