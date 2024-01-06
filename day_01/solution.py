f = open("input.txt").read().splitlines()[0]

print(sum(int(a) if a == b else 0 for a,b in zip(f, f[1:] + f[0])))
print(sum(int(a) if a == f[(i+len(f) // 2) % len(f)] else 0 for i,a in enumerate(f)))