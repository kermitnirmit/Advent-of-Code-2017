from utils import *
f = [x for x in open("input.txt").read().splitlines()]

adj_list = defaultdict(list)
node_weight = {}
all_values = set()
for line in f:
    if "->" in line:
        left, right = line.split(" -> ")
        weight = ints(left)[0]
        dests = right.split(", ")
        left = words(left)[0]
        node_weight[left] = weight
        adj_list[left] = dests
    else:
        left, right = words(line)[0], ints(line)[0]
        node_weight[left] = right
for k,v in adj_list.items():
    for val in v:
        all_values.add(val)
for k in adj_list.keys():
    if k not in all_values:
        print(k)
        break


final_weights = {}
def find_stack_weight(k):
    towers = adj_list[k]
    ret = []
    for tower in towers:
        if tower in final_weights:
            ret.append(node_weight[tower] + sum(final_weights[tower]))
        else:
            find_stack_weight(tower)
            ret.append(node_weight[tower] + sum(final_weights[tower]))
    final_weights[k] = ret

find_stack_weight('vtzay')

# for k,v in final_weights.items():
#     if len(v) > 0:
#         if any(v) != v[0]:
#             print(k,v)

# print(final_weights['vtzay'])
# for v in adj_list['vtzay']:
#     print(v, node_weight[v], final_weights[v], node_weight[v] + sum(final_weights[v]))
#
# for v in adj_list['qawlwzi']:
#     print(v, node_weight[v], final_weights[v], node_weight[v] + sum(final_weights[v]))

# for v in adj_list['jfrda']:
#     print(v, node_weight[v], final_weights[v], node_weight[v] + sum(final_weights[v]))
# # lnpuarnm is 8 too heavy, subtract 8
print(node_weight['lnpuarm'] - 8)