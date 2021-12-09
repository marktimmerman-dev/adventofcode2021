import numpy as np

def str2intlist(s):
  return [ int(c) for c in s ]

data = np.array([ str2intlist(s) for s in open('input.txt').read().splitlines() ])

rows, cols = data.shape

risk_level_of_low_points = []

for r in range(rows):
  for c in range(cols):
    if r > 0 and data[r, c] >= data[r-1, c]:
      continue;
    if r < rows-1 and data[r, c] >= data[r+1, c]:
      continue;
    if c > 0 and data[r, c] >= data[r, c-1]:
      continue;
    if c < cols-1 and data[r, c] >= data[r, c+1]:
      continue;
    risk_level_of_low_points.append(data[r,c]+1)

print(sum(risk_level_of_low_points))
