import itertools

dwarf = [int(input()) for _ in range(9)]

comb = list(itertools.combinations(dwarf, 7))
for i in list(comb):
    sum = 0
    a = []
    for j in i:
        sum += j
        a.append(j)
    if sum == 100:
        a.sort()
        print(*a, sep='\n')
        break