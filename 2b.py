data = [ [a, int(b) ] for a, b in (x.split() for x in open('input.txt').read().splitlines() )]

position = 0
depth = 0
aim = 0

for direction, steps in data:
  if direction == 'forward':
    position = position + steps
    depth = depth + steps * aim
  if direction == 'down':
    aim = aim + steps
  if direction == 'up':
    aim = aim - steps
    
print(position*depth)
