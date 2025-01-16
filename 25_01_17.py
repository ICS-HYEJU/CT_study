import itertools
N = int(input())
S = [list(map(int,input().split()))for _ in range(N)]
c = [i for i in range(N)]
teams = list(itertools.combinations(c, N//2))

scores = []
result = []
for t in teams:
    score = 0
    in_team=list(itertools.combinations(t,2))
    for i in in_team:
        score += S[i[0]][i[1]]+S[i[1]][i[0]]
    scores.append(score)

for i in range(len(scores)//2):
    result.append(abs(scores[i]-scores[len(scores)-i-1]))
print(min(result))


# for i in range(N):
#     for j in range(N):
#         ij = S[i][j] + S[j][i]
