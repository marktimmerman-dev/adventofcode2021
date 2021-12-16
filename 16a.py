def hex2bin(s):
  return "".join([ ('000'+format(int(c,16),'b'))[-4:] for c in s ])


hexdata = open('input.txt').read().splitlines()

packet_versions = []

def parse(data):
  i = 0

  packet_version = int(data[i:i+3],2)
  i += 3
  print('packet_version', packet_version)
  packet_versions.append(packet_version)

  packet_type = int(data[i:i+3],2)
  i += 3
  print('packet_type', packet_type)

  if packet_type == 4:  # litteral value
    litteral = ""
    while True:
      not_the_last_group = int(data[i:i+1],2)
      i += 1
      litteral += data[i:i+4]
      i += 4
      if not not_the_last_group:
        break;
    print('litteral', litteral, int(litteral, 2))
    return i, int(litteral, 2)

  else:
    length_type = int(data[i:i+1],2)
    i += 1
    
    r = []

    if length_type == 0:
      total_length = int(data[i:i+15],2)
      i += 15

      print('operator packet with length in bits',total_length)

      j = 0
      
      while j < total_length:
        k, val = parse(data[i:])
        i += k
        j += k
        r.append(val)
        
      if j != total_length:
        print('!!!!!!!!!!!!! hier is wat geks aan de hand')
        
      

    else:
      nsubpackets = int(data[i:i+11],2)
      i += 11

      print('operator packet with number of subpackets',nsubpackets)

      for j in range(nsubpackets):
        k, val = parse(data[i:])
        i += k
        r.append(val)


    return i, sum(r)

for h in hexdata:
  print('-------------------',h,'------------')
  data = hex2bin(h)

  print(data)

  packet_versions = []


  print(parse(data))
  print(packet_versions)
  print(sum(packet_versions))
