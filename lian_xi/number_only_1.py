
# 出现的1的个数
def NumberOf1Between1AndN_Solution(n):
    # write code here
    count = 0
    for i in range(1, n + 1):
        s = str(i)
        # print("i: ",i)
        if '1' in s:
            print(s)
            count += 1
    return count

count = NumberOf1Between1AndN_Solution(55)
print(count)

# K点游戏 招商银行
import sys
line = sys.stdin.readline().strip()
n,k,w = [int(x) for x in line.split()]
dp = [0] * (k+w)

for i in range(k,n+1):
    dp[i] = 1

s = min(w,n-k+1)
for j in range(k-1,-1,-1):
    dp[j] = s/w
    s += dp[j] - dp[j+w]

print(round(dp[0],5))