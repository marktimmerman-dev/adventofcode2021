import numpy as np
import networkx as nx

def pipo(x):
  return [ int(d) for d in x ]

smallcave = np.array([ pipo(x) for x in open('input.txt').read().splitlines() ])

maxy, maxx = smallcave.shape

cave = np.zeros((maxy*5, maxx*5), dtype=np.uint8)

for cy in range(5):
  for cx in range(5):
    c = smallcave + cy + cx
    c[c>9] -= 9
    cave[maxy*cy:maxy*(cy+1), maxx*cx:maxx*(cx+1)] = c

maxy, maxx = cave.shape

g = nx.DiGraph()

g.add_nodes_from(range(cave.size))

def node(x,y):
  return y*maxx+x

for y in range(maxy):
  for x in range(maxx):
    n = node(x,y)
    if x < maxx-1:
      n2 = node(x+1,y)
      g.add_edge(n, n2, weight=cave[x+1,y] )
      g.add_edge(n2, n, weight=cave[x,y] )
    if y < maxy-1:
      n2 = node(x,y+1)
      g.add_edge(n, n2, weight=cave[x,y+1] )
      g.add_edge(n2, n, weight=cave[x,y] )


print(nx.shortest_path_length(g, source=0, target=cave.size-1, weight='weight'))
