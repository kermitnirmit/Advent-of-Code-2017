from utils import *
f = [x for x in open("input.txt").read().splitlines()[0].split(",")]
p = (0,0)
max_d = 0
for line in f:
    p = add_tuples(p, d_map_hex[line])
    if absolute_value_sum(p) > max_d:
        max_d = absolute_value_sum(p)
print(int(absolute_value_sum(p)))
print(int(max_d))