def computepay(hours, rate):
	if hours > 40:
		pay = 40 * rate + (hours - 40) * rate * 1.5
	else:
		pay = hours * rate
	return pay

s_hours = input("Enter Hours: ")
s_rate = input("Enter Rate: ")
try:
	f_hours = float(s_hours)
	f_rate = float(s_rate)
except:
	print("Error, please enter numeric input")
	quit()
result = computepay(f_hours, f_rate)
print("Pay:", result)
