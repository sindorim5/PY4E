fname = input("Enter the file name: ")
try:
	fhand = open(fname, 'r')
except:
	print("File cannot be opened:", fname)
	quit()

count = 0
total = 0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence:"):
		start_index = line.find(" ")
		num = float(line[start_index+1:])
		total += num
		count += 1

print("Average spam confidence:", total/count)
