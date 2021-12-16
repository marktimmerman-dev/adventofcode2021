def hex2bin(s):
  return "".join([ ('000'+format(int(c,16),'b'))[-4:] for c in s ])

hexdata = open('input.txt').read().splitlines()

packet_versions = []

def parse(data):
  i = 0

  packet_version = int(data[i:i+3],2)
  i += 3
  packet_versions.append(packet_version)

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


    return i, sum(r)

for h in hexdata:
  data = hex2bin(h)
  packet_versions = []
  parse(data)
  print(sum(packet_versions))
