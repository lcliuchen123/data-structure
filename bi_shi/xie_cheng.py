
# 一、单选
# 1.最大似然估计和最小二乘法一般都假定满足正态分布，这个假定下最大似然估计与最小二乘等价。
# 2.cnn中卷积向下取整，池化向上取整。（N-K+2*P)/stride +1
# 3.卡特兰数：1，1，2，5，14，42，132
# f(0)=f(1) = 1, f(n) = f(0)f(n-1)+f(1)f(n-2)+....f(n-1)f(0)
# 4.GSP:关联规则+时间/空间维度
# 5、当数据有一个 0 均值向量时，PCA 有与 SVD 一样的投射 https://blog.csdn.net/wangjian1204/article/details/50642732

# 二、编程
# 一、求ks值
# 输入n个样本，每个样本的分数和标签。
# 没有读懂题，无法写代码。主要是没有理解输入的是什么东西。


def get_ks(line):
    line.sort(key= lambda x: x[0])
    print("line: ", line)
    pos = []
    neg = []
    for item in line:
        if item[1] == 1:
            pos.append(item)
        else:
            neg.append(item)

    pos_neg = []
    for item in line:
        count = 0
        for p in pos:
            if p[0] <= item[0]:
                count += 1
        p0 = count / len(pos)
        count = 0
        for n in neg:
            if n[0] <= item[0]:
                count += 1
        n0 = count / len(neg)
        pos_neg.append(abs(p0-n0))

    result  = max(pos_neg)

    return result


n = int(input())
score_list = []
for i in range(n):
    line = input()
    if line:
        line = [float(x) for x in line.split(',')]
        line = (line[0],line[1])
        print(line)
        score_list.append(line)

print(score_list)

result = get_ks(score_list)
print(result)

# 2、编辑距离
# AC 86
# dp[0][0]表示空白，dp[0][1]表示空白到第一个字符
# dp[1][0]表示空白到另一个字符串的第一个字符
# dp[i][j]:str1[:i]转换为str2[:j]的编辑距离
# 可以进行优化，只保留前一行。

# 编辑距离
def LevenshteinDis(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    dp = [[i + j for j in range(length2 + 1)] for i in range(length1 + 1)]

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + d)

    return dp[length1][length2]


# try:
#     _str1 = input()
# except:
#     _str1 = None
#
# try:
#     _str2 = input()
# except:
#     _str2 = None
#
# res = LevenshteinDis(_str1, _str2)
#
# print(str(res) + "\n")