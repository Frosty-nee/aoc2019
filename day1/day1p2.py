#! python
from math import floor as floor

input_mass = []
with open("day1/input") as f:
	for line in f:
		input_mass.append(int(line))
		
total_fuel = 0

def calculate_fuel(mass):
	fuel_need = floor(mass/3)-2
	if fuel_need > 0:
		return(fuel_need + calculate_fuel(fuel_need))
	else: return(0)

for mass in input_mass:
	total_fuel += calculate_fuel(mass)

print(total_fuel)