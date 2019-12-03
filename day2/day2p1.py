#! python

with open('day2/input') as f:
	intcode = list(map(int, (f.readline().split(','))))
	intcode[1] = 12
	intcode[2] = 2


position=0
while True:
	opcode = intcode[position]
	input1 = intcode[intcode[position+1]]
	input2 = intcode[intcode[position+2]]
	output = intcode[position+3]

	if opcode == 1:
		intcode[output] = input1+input2
	elif opcode == 2:
		intcode[output] = input1*input2
	elif opcode == 99:
		print(intcode[0])
		break
	position += 4