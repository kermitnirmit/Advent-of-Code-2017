from utils import *
from parse import parse
f = [x for x in open("input.txt").read().splitlines()]

regs = defaultdict(int)
max_ever = 0
for line in f:
    reg, act, amt, oreg, op, oamt = parse("{} {} {:d} if {} {} {:d}", line)
    if eval(f"{regs[oreg]} {op} {oamt}"):
        if act == "inc":
            regs[reg] += amt
            if regs[reg] > max_ever:
                max_ever = regs[reg]
        else:
            regs[reg] -= amt
            if regs[reg] > max_ever:
                max_ever = regs[reg]

print(max(regs.values()))
print(max_ever)