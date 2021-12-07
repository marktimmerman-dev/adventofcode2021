fish = [ int(x) for x in open('input.txt').read().split(',') ]



for day in range(80):
  l = len(fish)
  for i in range(l):
    fish[i] = fish[i] - 1
    if fish[i] < 0:
      fish[i] = 6
      fish.append(8)
#  print('After',day+1,'days:',fish, 'totaal', len(fish))  
print(len(fish))    
