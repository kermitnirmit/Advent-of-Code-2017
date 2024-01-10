f = [int(x) for x in open("input.txt").read().splitlines()]
old_f = f.copy()
p1, p2 = 0,0
i = 0
while i < len(f):
    jump = f[i]
    f[i] += 1
    i += jump
    p1 +=1
i = 0
print(p1)
f = old_f
while i < len(f):
    jump = f[i]
    if jump >= 3:
        f[i] -= 1
    else:
        f[i] += 1
    i += jump
    p2 += 1

print(p2)