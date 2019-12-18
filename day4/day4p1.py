#! python

with open('day4/input') as f:
	minimum, maximum = map(int, f.readline().split('-'))

def check_double(number):
	number = list(map(int,str(number)))
	for digit in range(len(number)):
		if digit > 0:
			if number[digit] == number[digit-1]:
				return True
	return False

def check_increasing(number):
	number = list(map(int,str(number)))
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