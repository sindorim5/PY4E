score = input("Enter Score: ")
try:
	f_score = float(score)
except:
	print("Bad score")
	quit()
if f_score < 0:
	print("Bad score")
elif f_score < 0.6:
	print("F")
elif f_score < 0.7:
	print("D")
elif f_score < 0.8:
	print("C")
elif f_score < 0.9:
	print("B")
elif f_score <= 1.0:
	print("A")
else:
	print("Bad score")
