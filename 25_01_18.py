N = int(input())
nums = list(map(int,input().split()))
opers = list(map(int,input().split()))

max = -1e9
min = 1e9
result = nums[0]
def dfs_operate(depth, nums, opers):
    global max,min,result

    if depth == len(nums):
        if result > max:
            max = result
        if result < min:
            min = result
        return

    for i in range(4):
        if opers[i] > 0:
            if i == 0:
                result += nums[depth]
            elif i == 1:
                result -= nums[depth]
            elif i == 2:
                result *= nums[depth]
            elif i == 3:
                if result < 0:
                    result = (-result//nums[depth])*-1
                else:
                    result //= nums[depth]

            opers[i] -= 1
            dfs_operate(depth+1,nums,opers)
            result = nums[0]
            opers[i] += 1


dfs_operate(1,nums,opers)
print(max)
print(min)

