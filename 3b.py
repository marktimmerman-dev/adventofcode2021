import numpy as np

l = [ list(map(int, list(s))) for s in (open('input.txt').read().splitlines()) ]

data = np.array(l)

for i in range(len(data[0])):
  col = data[:,i]
  most_common = int(np.count_nonzero(col) >= (len(col) / 2))
  d = [ x == most_common for x in col ]
  rem = []
  for r in range(len(d)):
    if not d[r]:
      rem.append(r)
  data = np.delete(data, rem, axis=0)
  if len(data) == 1:
    break
  
oxygen_bits = [ str(x) for x in data[0] ]
oxygen_rate = int("".join(oxygen_bits),2)

data = np.array(l)

for i in range(len(data[0])):
  col = data[:,i]
  least_common = int(np.count_nonzero(col) < (len(col) / 2))
  d = [ x == least_common for x in col ]
  rem = []
  for r in range(len(d)):
    if not d[r]:
      rem.append(r)
  data = np.delete(data, rem, axis=0)
  if len(data) == 1:
    break
  
co2_bits = [ str(x) for x in data[0] ]
co2_rate = int("".join(co2_bits),2)

print(oxygen_rate * co2_rate)

