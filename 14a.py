from collections import Counter

p, r = open('input.txt').read().split('\n\n')

polymer = p.splitlines()[0]

rules = dict()


def pipo(s):
  g = s.split()
  rules[g[0]] = g[2]

[ pipo(s) for s in r.splitlines() ]

def apply_step(h):
  pairs = [ "".join(x) for x in list(zip(h, h[1:])) ]
  new_polymer = []
  for w in pairs:
    new_polymer += w[0]+rules[w]
  new_polymer += w[1]
  return "".join(new_polymer)

for step in range(10):
  polymer = apply_step(polymer)
  element_histogram = [ b for a,b in Counter(polymer).most_common() ] 

print(element_histogram[0] - element_histogram[-1])
