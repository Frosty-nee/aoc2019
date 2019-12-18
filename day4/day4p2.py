#! python

with open('day4/input') as f:
	minimum, maximum = map(int, f.readline().split('-'))

def list_num(number):
	return list(map(int, str(number)))

def check_double(number):
	number = list_num(number)
	repeats = {}
	repeated = 0
	last = None
	for digit in range(len(number)):
		if number[digit] == last:
			repeated += 1
			last = number[digit]
		elif number[digit] != last:
			repeats[last] = repeated
			repeated = 0
			last = number[digit]
		if digit == len(number)-1:
			repeats[last] = repeated


	if 1 in repeats.values(): 
		return True
	else: 
		return False

def check_increasing(number):
	number = list_num(number)
	for digit in range(len(number)):
		if digit > 0:
			if number[digit] < number[digit-1]:
				return False
	return True

passwords = 0
for number in range(minimum, maximum):
	if check_double(number) and check_increasing(number):
		passwords += 1

print(passwords)