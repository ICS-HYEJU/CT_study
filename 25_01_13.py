# input
M = int(input())
changes =[list(map(int, input().split())) for _ in range(M)]
cups = [1, 2, 3]
def change_cups(changes,cups):
    for c in changes:
        c_x = cups.index(c[0])
        c_y = cups.index(c[1])
        tmp = cups[c_x]
        cups[c_x] = c[1]
        cups[c_y] = tmp
    return cups[0]

if change_cups:
    print(change_cups(changes,cups))
else:
    print(-1)