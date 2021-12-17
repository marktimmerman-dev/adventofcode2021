import re

prog = re.compile(r"^target area: x=([-]?\d+)\.\.([-]?\d+), y=([-]?\d+)\.\.([-]?\d+)$")

data = open('input.txt').read()

minx, maxx, miny, maxy = [ int(x) for x in prog.match(data).groups() ]

def trajectory(vx, vy):
  t = [(0,0)]
  
  x, y = t[0]
  
  while True:
    x += vx
    y += vy
    if vx != 0:
      vx -= vx // abs(vx)
    vy -= 1
    t.append((x,y))
  
    if x > maxx or y < miny:
      break
  
  return t

def hit(t):
  for x, y in t:
    if x >= minx and x <= maxx and y >= miny and y <= maxy:
      return True
  return False  


def traj(vy):
  for vx in range(maxx):
    t = trajectory(vx, vy)
    if hit(t):
      return max([y for x,y in t])
  return -1000  


highest = [traj(vy) for vy in range(maxx) ]
print(max(highest))

