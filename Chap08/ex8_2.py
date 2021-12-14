fhand = open('mbox-short.txt')
for line in fhand:
	words = line.split()
	if len(words) < 3 : continue # 최소 words = [0, 1, 2]
	if words[0] != 'From' : continue
	print (words[2])
