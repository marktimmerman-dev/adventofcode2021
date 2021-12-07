import numpy as np

data = open('input.txt').read().split('\n\n')

draw = [ int(d) for d in data[0].split(',') ]

def pipo(s):
  return list(map(int, s.split()))
  

cards = [ np.array(list(map(pipo, d.splitlines()))) for d in data[1:] ]


def bingo(d):
  global cards
  to_be_removed = []
  
  for i in range(len(cards)):
    c = cards[i]
    c[c == d] = -1
    
    for row in c:
      if np.sum(row) == -5:
        to_be_removed.append(i)
        continue

    for column in c.T:
      if np.sum(column) == -5:
        to_be_removed.append(i)
        continue

  cards = np.delete(cards, to_be_removed, axis=0)
  
  return len(cards) < 1

for d in draw:
  c = cards[0]
  b = bingo(d)
  if b:
    c[c == -1] = 0
    print(d * sum(c.flatten()))
    break
