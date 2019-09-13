
# 1，
def get_min(s):
    index = s.index('0')
    count = 0
    for i in range(index,len(s)):
        if s[i] == ')':
            count += 1

        if s[i] == '(':
            break
    return count

def get_min2(s):
    ind = s.index('0')
    count = 0
    for i in range(ind):
        if s[i] == '(':
            count += 1

        if s[i] == ')':
            count -= 1

    return count

s = '(()((0)()))'
print(get_min2(s))


# 2.0-1指派
def get_max_score(boxes):
    # count = len(boxes)
    # d = {}
    # while count >0:
    #     for i in boxes:
    #         if i

    from collections import Counter
    d = Counter(boxes)
    score = 0
    for k,v in d.items():
        score += v*v
    return score

# boxes = [1 ,4, 2, 2, 3, 3, 2, 4, 1]
# print(get_max_score(boxes))


# 0-1指派，动态规划
def main():
    w = int(input())    #背包大小
    n = int(input())    #物品个数
    listWV = [[0,0]]
    listTemp = []
    for i in range(n):
        listTemp = list(map(int, input().split()))  #借助临时list每次新增物品对应的list加入到listWV中
        listWV.append(listTemp) #依次输入每个物品的重量与价值

    # 建立价值数组，初始值均为0，目的是为了在value[0][j]与value[i][0]的情况为0，毕竟不放入物品或者背包容量为0的情况下，背包中的价值肯定为0，
    value = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, w+1):
            if j < listWV[i][0]:    #若物品不能放到背包中
                value[i][j] = value[i-1][j] #价值与之前相同
            else:   #物品可以放到背包中，最大价值在两者之中取
                value[i][j] = max(value[i-1][j], value[i-1][j-listWV[i][0]]+listWV[i][1])
    print(value)
    print(value[n][w])


# ans[i][j][k]表示i个物品，在容量在j,k的情况下的最大用户数
def  get_max_users(d,m,u):
    n = len(u)
    ans =[[[0 for i in range(d+1)] for j in range(m+1)] for k in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(1,d+1):
                if u[i][-1] > k or u[i][-2] > j:
                    ans[i][j][k] = ans[i-1][j][k]
                else:
                    ans[i][j][k] = max(ans[i-1][j][k], ans[i-1][j-u[i][-2]][k-u[i][0]]+u[i][-1])

    return ans[n][d][m]

if __name__ == '__main__':
    main()