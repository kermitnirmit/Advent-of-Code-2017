f = [x for x in open("input.txt").read().splitlines()]
p1, p2 = 0,0
for line in f:
    a = line.split()
    if len(set(a)) == len(a):
        p1 += 1
    counters = set()
    for word in a:
        counters.add("".join(sorted(word)))
    if len(counters) == len(a):
        p2 += 1
print(p1)
print(p2)