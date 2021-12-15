import numpy as np
import networkx as nx

def pipo(x):
  return [ int(d) for d in x ]

cave = np.array([ pipo(x) for x in open('input.txt').read().splitlines() ])

maxy, maxx = cave.shape

print(maxx,maxy,cave.size)

g = nx.Graph()

g.add_nodes_from(range(cave.size))

def node(x,y):
  return y*maxx+x

for y in range(maxy):
  for x in range(maxx):
    n = node(x,y)
    if x < maxx-1:
      n2 = node(x+1,y)
      g.add_edge(n, n2, weight=cave[x+1,y] )
    if y < maxy-1:
      n2 = node(x,y+1)
      g.add_edge(n, n2, weight=cave[x,y+1] )


print(nx.shortest_path_length(g, source=0, target=cave.size-1, weight='weight'))
