#! python
from math import floor as floor

input_mass = []
with open("day1/input") as f:
	for line in f:
		input_mass.append(int(line))

total_fuel = 0
for mass in input_mass:
	total_fuel += floor(mass/3)-2

print(total_fuel)