import numpy as np

crab = [ int(x) for x in open('input.txt').read().split(',') ]

def abssub(a, b):
  m = abs(a - b)
  cost = m * (m+1) // 2 # https://oeis.org/A000217
  return cost


def calculate_cost(i):
  moves = [ abssub(c, i) for c in crab ]
  cost = sum(moves)
  return cost

m = max(crab)
costs = [ calculate_cost(i) for i in range(m+1)]

print(costs[np.argmin(costs)])


  
