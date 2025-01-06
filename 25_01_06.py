# 분해합

# 오답코드
# - 조건 가장 작은 생성자 출력 불만족
# - 러닝타임 줄이는 것에 초점 맞춰 제한 조건 제대로 파악 x
# N = int(input())
# exist = False
# for i in range(N,0,-1):
#     sum = i
#     for j in range(len(str(i))):
#         sum += int(str(i)[j])
#     if sum == N:
#         print(i)
#         break
# if exist == False:
#     print(0)

# 정답
N = int(input())
exist = False
for i in range(0,N+1):
    sum = i
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if sum == N:
        exist = True
        print(i)
        break
    if exist == False:
        print(0)