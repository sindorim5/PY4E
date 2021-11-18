hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
	f_hours = float(hours)
	f_rate = float(rate)
except:
	print("Error, please enter numeric input")
	quit()
if f_hours > 40 :
	pay = 40 * f_rate + (f_hours - 40) * f_rate * 1.5
else :
	pay = f_hours * f_rate
print("Pay:", pay)
