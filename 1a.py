data = [ int(d) for d in open('input.txt').read().splitlines()]
s = sum([a < b for a,b in zip(data, data[1:])])
print(s)
