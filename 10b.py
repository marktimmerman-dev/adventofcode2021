lines = open('input.txt').read().splitlines()

closing = { '[': ']', '{': '}', '(': ')', '<': '>' }

points = { ')': 1, ']': 2, '}': 3, '>': 4 }

def find_illegal_character(line):
  stack = []
  for c in line:
    if c in '[({<':
      stack.append(c)
    else:
      o = stack.pop()
      if closing[o] != c:
        return c
  return ''
  
def autocomplete(line):
  stack = []
  for c in line:
    if c in '[({<':
      stack.append(c)
    else:
      stack.pop()
  completed = ""
  while(len(stack)):
    completed += closing[stack.pop()]
  return completed  
incomplete = [ line for line in lines if find_illegal_character(line) == '' ]

completed = [ autocomplete(line) for line in incomplete ]

def score(s):
  p = [ points[c] for c in s ]
  t = 0
  for i in p:
    t = t * 5 + i
  return t
  

p = [ score(c) for c in completed ]
middle = len(p)//2
print(sorted(p)[middle])
