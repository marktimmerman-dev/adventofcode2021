import numpy as np

def pipo(x):
  digits, output = x.split('|')
  return [digits.split(), output.split()]


data = [ pipo(x) for x in open('input.txt').read().splitlines() ]

def flatten(t):
    return [item for sublist in t for item in sublist]

outputlens = np.array([ len(x) for x in flatten([ output for digits, output in data ]) ])
print(np.count_nonzero(outputlens <=4)+np.count_nonzero(outputlens == 7))

