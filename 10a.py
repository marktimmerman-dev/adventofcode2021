lines = open('input.txt').read().splitlines()

closing = { '[': ']', '{': '}', '(': ')', '<': '>' }

points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

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
  
illegal = [ find_illegal_character(line) for line in lines if find_illegal_character(line) != '' ]
print(illegal)

p = [ points[i] for i in illegal ]
print(sum(p))
