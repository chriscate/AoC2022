with open('aoc_in.txt') as f:
    aoc_in = f.readlines()

a = [[x.split(',')[0].split('-'), x.split(',')[1].split('-')] for x in aoc_in]

result1 = 0
for x in a:
    min1 = int(x[0][0])
    max1 = int(x[0][1])
    min2 = int(x[1][0])
    max2 = int(x[1][1])
    if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1):
        result1 += 1

print(result1)

result2 = 0
for x in a:
    min1 = int(x[0][0])
    max1 = int(x[0][1])
    min2 = int(x[1][0])
    max2 = int(x[1][1])
    if set(range(min1, max1+1)).intersection(set(range(min2, max2+1))):
        result2 += 1

print(result2)
