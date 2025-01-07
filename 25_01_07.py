# Using itertools.ver
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

# Not Using itertools.ver
def find_del_value(del_value):
    for i in range(len(dwarf)):
        for j in range(len(dwarf)):
            if i == j:
                continue
            if (dwarf[i]+dwarf[j]) == del_value:
                del_one = dwarf[i]
                del_two = dwarf[j]
                return del_one, del_two

if __name__=='__main__':
    dwarf = [int(input()) for _ in range(9)]
    all_sum = sum(dwarf)
    del_value = all_sum - 100
    value_,value__= find_del_value(del_value)
    dwarf.remove(value_)
    dwarf.remove(value__)
    dwarf.sort()
    print(*dwarf, sep='\n')