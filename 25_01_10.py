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
                # if sum of index == even, same start color
                if (r+c) % 2 == 0:
                    # start 'W', even_index == 'W'
                    if board[r][c] != 'B':
                        is_B +=1
                    else:
                        # start 'B', even_index == 'B'
                        is_W +=1
                # sum of index == odd, not same start color
                else:
                    if board[r][c] != 'W':
                        is_B += 1
                    else:
                        is_W += 1
        count.append(min(is_W,is_B))
print(min(count))

# N, M = map(int, input().split())
# original = []
# count = []
#
# for _ in range(N):
#     original.append(input())
#
# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))
#
# print(min(count))