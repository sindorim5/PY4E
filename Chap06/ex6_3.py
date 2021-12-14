def count(word, letter):
	num = 0
	for char in word:
		if char == letter:
			num += 1
	print(num)

word = input("Enter the word: ")
letter = input("Enter the letter: ")
count(word, letter)
