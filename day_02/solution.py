import itertools

f = [x for x in open("input.txt").read().splitlines()]
p1, p2 = 0,0
for line in f:
    numbers = [int(x) for x in line.split("\t")]
    p1 += max(numbers) - min(numbers)
    for a,b in itertools.combinations(numbers, 2):
        a,b = max(a,b), min(a,b)
        if a % b == 0:
            p2 += a // b
            break
print(p1)
print(p2)