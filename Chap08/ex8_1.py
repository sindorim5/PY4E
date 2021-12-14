def chop(list):
	del list[0]
	del list[-1]

def middle(list):
	new_list = list[1:]
	del new_list[-1]
	return new_list

usr_list = [0, 1, 2, 3, 4]
usr_list2 = [0, 1, 2, 3, 4]
chop_list = chop(usr_list)
middle_list = middle(usr_list2)
print(chop_list)
print(middle_list)
