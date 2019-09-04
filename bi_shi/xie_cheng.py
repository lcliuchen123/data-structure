
# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
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

# ******************************结束写代码******************************


try:
    _str1 = input()
except:
    _str1 = None

try:
    _str2 = input()
except:
    _str2 = None

res = LevenshteinDis(_str1, _str2)

print(str(res) + "\n")