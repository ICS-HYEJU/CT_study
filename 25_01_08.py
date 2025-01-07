lines = int(input())
tri_nums = [int(input()) for _ in range(lines)]

def make_triangle(v):
    T_n =[]
    for n in range(1,v+1):
        T_i = n*(n+1)/2
        if T_i > v:
            break
        T_n.append(T_i)
    return T_n
def find_three_tri(T_n, v):
    for i in range(len(T_n)):
        for j in range(len(T_n)):
            for k in range(len(T_n)):
                sum = T_n[i] + T_n[j] + T_n[k]
                if sum == v:
                    return True

for v in tri_nums:
    T_n = make_triangle(v)
    bool = find_three_tri(T_n,v)
    if bool == True:
        print(1)
    else:
        print(0)