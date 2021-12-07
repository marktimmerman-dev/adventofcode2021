import numpy as np

def pipo(x):
  return list(map(int, x.split(',')))

f = [ list(map(pipo, a.split(' -> '))) for a in open('input.txt').read().splitlines() ]

m = np.max(np.array(f))

diagram = np.zeros((m+1, m+1), dtype=np.uint8)

for begin, end in f:
  bc = begin[0]
  br = begin[1]
  ec = end[0]
  er = end[1]
  vc = 0
  if ec > bc:
    vc = 1
  if ec < bc:
    vc = -1
  vr = 0
  if er > br:
    vr = 1
  if er < br:
    vr = -1
  n = abs((ec - bc) * vc)
  if vc == 0:
    n = abs((er - br) * vr)
    
  for i in range(n+1):
    diagram[br+i*vr][bc+i*vc] = diagram[br+i*vr][bc+i*vc] + 1

print(np.count_nonzero(diagram.flatten() >= 2))
