def find_starting_index(l):
    i = 0
    maxv = l[0]
    for index, elem in enumerate(l):
        if elem > maxv:
            i = index
            maxv = elem
    return i

def solve(p1=True):
    f = [int(x) for x in open("input.txt").read().splitlines()[0].split("\t")] if p1 else [0, 1, 14, 14, 13, 12, 11, 9, 9, 8, 7, 6, 5, 3, 2, 4]
    check = tuple(f)
    seen = set()
    c = 0
    while True:
        q = find_starting_index(f)
        dist = f[q]
        f[q] = 0
        q += 1
        q %= len(f)
        while dist > 0:
            f[q] += 1
            dist -= 1
            q += 1
            q %= len(f)
        c += 1
        if p1:
            if tuple(f) in seen:
                break
            seen.add(tuple(f))
        else:
            if tuple(f) == check:
                break
    return c

print(solve())
print(solve(False))