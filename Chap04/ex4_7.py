def computegrade(score):
	if score < 0:
		grade = "Bad score"
	elif score < 0.6:
		grade = "F"
	elif score < 0.7:
		grade = "D"
	elif score < 0.8:
		grade = "C"
	elif score < 0.9:
		grade = "B"
	elif score <= 1.0:
		grade = "A"
	else:
		grade = "Bad score"
	return grade

score = input("Enter Score: ")
try:
	f_score = float(score)
except:
	print("Bad score")
	quit()
result = computegrade(f_score)
print(result)
