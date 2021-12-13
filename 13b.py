import re
import numpy as np

prog = re.compile(r"fold along ([xy])=([0-9]+)")

dots_lines, fold_lines = open('input.txt').read().split('\n\n')

dots = [ list(map(int, d.split(','))) for d in dots_lines.splitlines() ]

fold_instructions = [ prog.match(d).groups() for d in fold_lines.splitlines() ]

maxx = max([ x for x,y in dots ])
maxy = max([ y for x,y in dots ])
if maxy % 2:
  maxy += 1

paper = np.zeros((maxy+1, maxx+1), dtype=np.uint8)

for x,y in dots:
  paper[y, x] = 1

for axis, l in fold_instructions:
  line = int(l)
  if axis == 'y':
    bottomhalf = paper[line+1:,]
    upperhalf = paper[:line,]
    bottomhalf = np.flipud(bottomhalf)
    paper = np.bitwise_or(upperhalf, bottomhalf)

  if axis == 'x':
    right = paper[:,line+1:]
    left = paper[:,:line]
    right = np.fliplr(right)
    paper = np.bitwise_or(left, right)
  
print(paper)

