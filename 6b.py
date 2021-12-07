import numpy as np

data = [ int(x) for x in open('input.txt').read().split(',') ]

days = 256

age_histogram = np.array([ data.count(i) for i in range(8+1) ])

for d in range(days):
  age_histogram = np.roll(age_histogram, -1)
  age_histogram[6] += age_histogram[-1]  

print(sum(age_histogram))
