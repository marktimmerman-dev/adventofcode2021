import numpy as np

l = [ list(map(int, list(s))) for s in (open('input.txt').read().splitlines()) ]

data = np.array(l)

t = np.transpose(data)

g = [ str(int(x > ( len(t[0]) // 2))) for x in np.count_nonzero(t, axis=1) ]

gamma_rate = int("".join(g),2)

e = [ str(int(not(x > ( len(t[0]) // 2)))) for x in np.count_nonzero(t, axis=1) ]

epsilon_rate = int("".join(e),2)

print(gamma_rate * epsilon_rate)
