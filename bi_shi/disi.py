
# 费马四平方数猜想指出，任意自然数都可以分解成不超过四个完全平方数的和。
# 例如：144 = 122 ，14 = 12 + 22 +32。

def get_n(n):
    mn = n // 2
    count = 0
    num = []
    for i in range(1,mn):
        num.append(i*i)
    for j in num[::-1]:
        if n % j == 0:
            count += n // j
            return count

    for i in range(mn,0,-1):
        if n % (i*i) == 0:
            count += (n // (i*i))
            break
        if n - i*i > 0:
            count += 1
            n = n - i*i
    return count

# n = int(input())
# count = get_n(n)
# print(count)


# 正解
s = [4] * 100        #先初始每个数是最多由4个平方数组成
print(len(s))
for i in range(100):
    if i*i <100:
        s[i*i] = 1


for i in range(100):  #二个平方数由两个一个平方数组成，三个平方数由一个平方数和一个由两个平数数组成
    if s[i]==1:
        for j in range(1,100):
            if i + j >= 100:
                break
            print("i: ", i)
            if s[i+j]>s[j]+1:
                s[i+j]=s[j]+1
            print("j：",s[i+j])

print(s)
