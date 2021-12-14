import copy

p, r = open('input.txt').read().split('\n\n')

polymer = p.splitlines()[0]

rules = dict([ s.split(' -> ') for s in r.splitlines() ])

pair_count = dict([ (x, 0) for x in rules.keys() ])

pairs = [ "".join(x) for x in list(zip(polymer, polymer[1:])) ]
for pr in pairs:
  pair_count[pr] += 1


def apply_step():
  global pair_count
  new_pair_count = copy.deepcopy(pair_count)
  for pair in pair_count:
    c = rules[pair]
    new_pair_1 = pair[0] + c
    new_pair_2 = c + pair[1]
    n = pair_count[pair]
    new_pair_count[pair] -= n
    new_pair_count[new_pair_1] += n
    new_pair_count[new_pair_2] += n
  pair_count = copy.deepcopy(new_pair_count)

for step in range(40):
  apply_step()
  left = [ (a[0],b) for a,b in list(pair_count.items())]
  cnt = dict()
  cnt[polymer[-1]] = 1
  for a,b in left:
    if a not in cnt:
      cnt[a] = 0
    cnt[a] += b
  wortel = sorted(list(cnt.values()))

print(wortel[-1] - wortel[0])
  
