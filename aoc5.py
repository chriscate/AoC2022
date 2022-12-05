import re

with open('aoc5in_1.txt') as f:
    aocin1 = f.readlines()
with open('aoc5in_2.txt') as f:
    aocin2 = f.readlines()

# parse input 1 (stacks)
a1 = []
for x in aocin1:
    i = 0
    sub = []
    while i < len(x):
        sub.append(x[i:i+4])
        i += 4
    a1.append(sub)

a1_2 = []
for x in a1:
    a1_2.append([y.replace(',','').replace('\n','').replace('[','').replace(']','').strip() for y in x])

stack_ids = a1_2.pop()
vals = list(map(list, zip(*a1_2)))

final_vals = []
for x in vals:
    final_vals.append([y for y in x if y != ''])
fv_reverse = [list(reversed(x)) for x in final_vals]

a1_final = dict(zip(stack_ids, fv_reverse))

# parse input 2 (move instructions)
a2 = [re.findall(r'\d+', x) for x in aocin2]

# PART 1
# arrange the stacks
for x in a2:
    for y in range(int(x[0])):
        a1_final[x[2]].append(a1_final[x[1]].pop())

''.join([x[-1] for x in a1_final.values()])

# PART 2
fv_reverse = [list(reversed(x)) for x in final_vals]
a1_final2 = dict(zip(stack_ids, fv_reverse))
# arrange the stacks
for x in a2:
    a1_final2[x[2]] = a1_final2[x[2]] + a1_final2[x[1]][-int(x[0]):]
    del(a1_final2[x[1]][-int(x[0]):])

''.join([x[-1] for x in a1_final2.values()])
