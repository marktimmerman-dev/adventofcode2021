data = [ [a, int(b) ] for a, b in (x.split() for x in open('input.txt').read().splitlines() )]

position = 0
depth = 0

for direction, steps in data:
  if direction == 'forward':
    position = position + steps
  if direction == 'down':
    depth = depth + steps
  if direction == 'up':
    depth = depth - steps
    
print(position*depth)
