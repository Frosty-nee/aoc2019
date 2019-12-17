#! python

with open('day3/input') as f:
	wires = list(f.readlines())
for wire in range(len(wires)):
	wires[wire] = wires[wire].split(',')
	wires[wire][-1] = wires[wire][-1][:4]

def trace_wire(wire):
	path = [(0,0)]
	for movement in wire:
		direction = movement[0]
		distance = int(movement[1:])
		moved = 0
		if direction == 'R':
			while moved < distance:
				moved += 1
				x,y = path[-1]
				x+=1
				path.append((x,y))
		elif direction == 'L':
			while moved < distance:
				moved += 1
				x,y = path[-1]
				x-=1
				path.append((x,y))
		elif direction == 'U':
			while moved < distance:
				moved += 1
				x,y = path[-1]
				y+=1
				path.append((x,y))
		elif direction == 'D':
			while moved < distance:
				moved += 1
				x,y = path[-1]
				y-=1
				path.append((x,y))
			
	return path

def man_dist(tu):
	return abs(tu[0]) + abs(tu[1])
		
path1 = trace_wire(wires[0])
path2 = trace_wire(wires[1])

intersections = set(path1) & set(path2)

closest = (0,0)
for intersect in intersections:
	distance = man_dist(intersect)
	if distance > 0 and distance < man_dist(closest):
		closest = intersect
		continue
	if closest == (0,0):
		closest = intersect
		continue
print(man_dist(closest))
