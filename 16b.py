import numpy as np

def hex2bin(s):
  return "".join([ ('000'+format(int(c,16),'b'))[-4:] for c in s ])

hexdata = open('input.txt').read().splitlines()

def parse(data):
  i = 0

  packet_version = int(data[i:i+3],2)
  i += 3

  packet_type = int(data[i:i+3],2)
  i += 3

  if packet_type == 4:  # litteral value
    litteral = ""
    while True:
      not_the_last_group = int(data[i:i+1],2)
      i += 1
      litteral += data[i:i+4]
      i += 4
      if not not_the_last_group:
        break;
    return i, int(litteral, 2)

  else:
    length_type = int(data[i:i+1],2)
    i += 1
    
    r = []

    if length_type == 0:
      total_length = int(data[i:i+15],2)
      i += 15

      j = 0
      while j < total_length:
        k, val = parse(data[i:])
        i += k
        j += k
        r.append(val)

    else:
      nsubpackets = int(data[i:i+11],2)
      i += 11

      for j in range(nsubpackets):
        k, val = parse(data[i:])
        i += k
        r.append(val)

    if packet_type == 1:
      return i, np.prod(r)
    if packet_type == 2:
      return i, min(r)
    if packet_type == 3:
      return i, max(r)
    if packet_type == 5:
      return i, int(r[0] > r[1])
    if packet_type == 6:
      return i, int(r[0] < r[1])
    if packet_type == 7:
      return i, int(r[0] == r[1])
    return i, sum(r)

for h in hexdata:
  data = hex2bin(h)
  l, val = parse(data)
  print(val)
