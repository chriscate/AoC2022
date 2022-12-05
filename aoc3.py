with open('aoc_in.txt') as f:
    aoc_in = f.readlines()

in2 = [[x[:len(x)//2], x[len(x)//2:]] for x in aoc_in]

# ord() - 96 for lowercase
# ord() - 38 for uppercase

def convert_to_score(x):
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96

result1 = []
for x in in2:
    for y in x[0]:
        if y in x[1]:
            result1.append(convert_to_score(y))
            break

print(sum(result1))

result2 = []
i = 0
while i < len(aoc_in):
    for x in aoc_in[i]:
        if x in aoc_in[i+1] and x in aoc_in[i+2]:
            result2.append(convert_to_score(x))
            break
        else: pass
    i += 3

print(sum(result2))
