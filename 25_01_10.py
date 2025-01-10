N,M = map(int,input().split())
board = []
count = []
for _ in range(N):
    board.append(input())

# make 8x8 size from NxM board
for n in range(N-7):
    for m in range(M-7):
        is_W = 0
        is_B = 0
        # Check 8x8 board (W,B)
        for r in range(n, n+8):
            for c in range(m, m+8):
                if (r+c) % 2 == 0:
                    if board[r][c] != 'B':
                        is_B +=1
                    else:
                        is_W +=1
                else:
                    if board[r][c] != 'W':
                        is_B += 1
                    else:
                        is_W += 1
        count.append(min(is_W,is_B))
print(min(count))