alpha = 'abcdefghijklmnopqrstuvwxyz'
freq_dict = dict()
freq_list = list()
fname = input("Enter the file name: ")
try:
	fhand = open(fname, 'r')
	text = fhand.read()
except:
	print("File cannot be opened:", fname)
	quit()
for char in text.lower():
	if char in alpha:
		freq_dict[char] = freq_dict.get(char, 0) + 1

for key, val in freq_dict.items():
	freq_list.append((val, key))

freq_list = sorted(freq_list, reverse=True)

for val, key in freq_list:
	print(key, val)
