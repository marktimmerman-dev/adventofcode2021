import numpy as np

data = open('input.txt').read().split('\n\n')

draw = [ int(d) for d in data[0].split(',') ]

def pipo(s):
  return list(map(int, s.split()))
  

cards = [ np.array(list(map(pipo, d.splitlines()))) for d in data[1:] ]


def bingo(d):
  for c in cards:
    c[c == d] = -1
    
    for row in c:
      if np.sum(row) == -5:
        return True,c

    for column in c.T:
      if np.sum(column) == -5:
        return True,c

  return False, None

for d in draw:
  b, c = bingo(d)
  if b:
    c[c == -1] = 0
    print(d * sum(c.flatten()))
    break
