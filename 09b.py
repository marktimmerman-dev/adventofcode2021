import numpy as np

def str2intlist(s):
  return [ int(c) for c in s ]

data = np.array([ str2intlist(s) for s in open('input.txt').read().splitlines() ])

rows, cols = data.shape

low_points = []

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
    low_points.append((r,c))

def remove_duplicates(x):
  return list(dict.fromkeys(x))

b = []

n = np.zeros((rows,cols), dtype=np.uint8)

def find_basin(p):
  b.append(p)
  r,c = p
  n[r,c]=1
  if r > 0 and (r-1,c) not in b and data[r-1,c] != 9:
    find_basin((r-1, c))
  if r < rows - 1 and (r+1,c) not in b and data[r+1,c] != 9:
    find_basin((r+1, c))
  if c > 0 and (r,c-1) not in b and data[r,c-1] != 9:
    find_basin((r, c-1))
  if c < cols-1 and (r,c+1) not in b and data[r,c+1] != 9:
    find_basin((r, c+1))

def find_basin_size(p):
  find_basin(p)
  return len(b)


basin_sizes = []

for lp in low_points:
  n = np.zeros((rows,cols), dtype=np.uint8)
  b = []
  bs = find_basin_size(lp)
  basin_sizes.append(bs)
  
print(np.prod(sorted(basin_sizes, reverse=True)[:3]))
