fh = open('mbox-short.txt')
for line in fh:
	data = line.rstrip()
	print(data.upper())
