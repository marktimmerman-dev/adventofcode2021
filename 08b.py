import numpy as np

def pipo(x):
  digits, output = x.split('|')
  return [digits.split(), output.split()]


data = [ pipo(x) for x in open('input.txt').read().splitlines() ]

def overlap(a, b):
  aa = set([ x for x in a ])
  bb = set([ x for x in b ])
  return len(set.intersection(aa, bb))

def fully_overlap(a, b):
  return overlap(a,b) == len(b)
  

def decode(digits, output):
  one = [ d for d in digits if len(d) == 2 ][0]
  four = [ d for d in digits if len(d) == 4 ][0]
  seven = [ d for d in digits if len(d) == 3 ][0]
  eight = [ d for d in digits if len(d) == 7 ][0]
  five_segments = [ d for d in digits if len(d) == 5 ]
  six_segments = [ d for d in digits if len(d) == 6 ]
  three = [ d for d in five_segments if fully_overlap(d, seven) ][0]
  five_segments.remove(three)
  two = [ d for d in five_segments if overlap(d, four) == 2][0]
  five = [ d for d in five_segments if overlap(d, four) == 3][0]
  nine = [ d for d in six_segments if fully_overlap(d, four) ][0]
  six_segments.remove(nine)
  six = [ d for d in six_segments if fully_overlap(d, five) ][0]
  six_segments.remove(six)
  zero = six_segments[0]
  
  decoded = [ sorted(x) for x in [zero, one, two, three, four, five, six, seven, eight, nine] ]
  o = int("".join([str(decoded.index(sorted(x))) for x in output]))
  return o

d = [ decode(digits, output) for digits, output in data ]
print(sum(d))
