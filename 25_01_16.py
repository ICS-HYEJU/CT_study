N = int(input())
TP = [list(map(int,input().split()))for _ in range(N)]
dp = [0]*(N+1)

for i in range(N-1, -1, -1):
    if i+TP[i][0]>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[i+TP[i][0]]+TP[i][1])
print(dp[0])

















# consult = [0]*N
# pay = 0
# result =[]
#
# for j in range(N):
#     if 1 in consult[j:j+T_P[j][0]]:
#         continue
#     if j+T_P[j][0] > N:
#         continue
#     consult[j:j+T_P[j][0]] = [1] * T_P[j][0]
#     pay += T_P[j][1]
#
# print(pay)