import copy

edges = [ e.split('-') for e in open('input.txt').read().splitlines() ]

reverse = [ [a,b] for b,a in edges ]
edges = edges + reverse

start = [ e for e in edges if e[0] == 'start' ]

paths = []

def find_path(edge, path):
  a, b = edge
  path.append(b)
  next = [ e for e in edges if e[0] == edge[1] ]
  if b == 'end':
    paths.append(path)
    return
  if len(next) == 0:
    return
  for n in next:
    if n[1][0] < 'a' or n[1] not in path:
      find_path(n, copy.deepcopy(path))

for e in start:
  find_path(e, [e[0]])

print(len(paths))
