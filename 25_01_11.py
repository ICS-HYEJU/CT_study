# Input
# 1. first line = N, M (=<50)
# 2. second line = the numbers in N lines
# Output
# size of square
# Problem
# 꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형

import sys


def find_size(N,M,square):
    for r in range(N-s+1):
        for c in range(M-s+1):
            if (square[r][0][c] == square[r][0][c+s-1] == square[r+s-1][0][c] == square[r+s-1][0][c+s-1]):
                return True
    return False


if __name__=='__main__':
    N, M = map(int, input().split())
    square = []
    for _ in range(N):
        square.append(list(sys.stdin.readline().split()))
    side = min(N,M)
    for s in range(side,0,-1):
        if find_size(N,M,square):
            print(s**2)
            break


