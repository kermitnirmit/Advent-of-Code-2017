from utils import *
import networkx
f = [x for x in open("input.txt").read().splitlines()]

adj_list = {}
for line in f:
    nums = ints(line)
    adj_list[nums[0]] = nums[1:]

g = networkx.from_dict_of_lists(adj_list)
c = 0
for x in networkx.connected_components(g):
    c += 1
    if 0 in x:
        print(len(x))
print(c)

