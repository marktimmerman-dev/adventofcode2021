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
  if bc > ec:
    tmp = bc
    bc = ec
    ec = tmp
  if br > er:
    tmp = br
    br = er
    er = tmp
  
  if br == er:
    for i in range(bc,ec+1):
      diagram[br][i] = diagram[br][i] + 1
  if bc == ec and br != er:
    for i in range(br,er+1):
      diagram[i][bc] = diagram[i][bc] + 1

print(np.count_nonzero(diagram.flatten() >= 2))
