import numpy as np

def strtointlist(s):
  return [ int(c) for c in s ]

data = np.array([ strtointlist(s) for s in open('input.txt').read().splitlines() ])

def find_neighbours(f):
  n = []
  r,c = f
  maxr, maxc = data.shape
  maxr -= 1
  maxc -= 1
  if r > 0:
    if c > 0:
      n.append([r-1, c-1])
    n.append([r-1, c])
    if c < maxc:
      n.append([r-1, c+1])
  if c > 0:
    n.append([r, c-1])
  if c < maxc:
    n.append([r, c+1])
  if r < maxr:
    if c > 0:
      n.append([r+1, c-1])
    n.append([r+1, c])
    if c < maxc:
      n.append([r+1, c+1])
  return n

ones = np.ones(data.shape, dtype=np.uint8)

nflash = 0

for step in range(1000):
  data = data + ones
  
  fw = np.where(data > 9)
  flash = list(zip(fw[0], fw[1]))

  while(len(flash)):
    nflash += 1
    f = flash.pop()
    neighbours = find_neighbours(f)
    for nr,nc in neighbours:
      data[nr,nc] = data[nr,nc] + 1
      if data[nr,nc] == 10:
        flash.append((nr,nc))

  fw = np.where(data > 9)
  flash = list(zip(fw[0], fw[1]))
  for fr, fc in flash:
    data[fr, fc] = 0
  
  if np.count_nonzero(data) == 0:
    print(step+1)
    break  

