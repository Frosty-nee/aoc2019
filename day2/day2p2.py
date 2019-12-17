#! python

import os
import sys

with open('day2/input') as f:
	initial_intcode = list(map(int, (f.readline().split(','))))
	intcode=initial_intcode.copy()

def add(input1, input2):
	return input1+input2

def mult(input1, input2):
	return input1*input2


for noun in range(100):
	for verb in range(100):
		position=0
		intcode = initial_intcode.copy()
		intcode[1], intcode[2] = noun, verb

		while True:
			opcode=intcode[position]
			input1=intcode[intcode[position+1]]
			input2=intcode[intcode[position+2]]
			output=intcode[position+3]

			if opcode == 99 and intcode[0] == 19690720:
				print('noun: {noun}, verb: {verb}')
				print(100*noun+verb)
				sys.exit()
			if opcode == 1:
				intcode[output] = add(input1, input2)
			if opcode == 2:
				intcode[output] = mult(input1, input2)
			if opcode == 99:
				break	
			position +=4


