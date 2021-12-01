data = [ int(d) for d in open('input.txt').read().splitlines()]
threemeasurements = [ a + b + c for a,b,c in zip(data, data[1:], data[2:])]
s = sum([a < b for a,b in zip(threemeasurements, threemeasurements[1:])])
print(s)
