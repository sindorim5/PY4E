largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        fnum = float(snum)
    except:
        print("Invalid input")
        continue
    if largest == None:
    	largest = fnum
    if smallest == None:
    	smallest = fnum
    if fnum > largest:
    	largest = fnum
    if fnum < smallest:
    	smallest = fnum

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
