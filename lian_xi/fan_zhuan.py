

# temp[-1:-length:-1] 逆序
# 自己的解法，一直在纠结空格的位置。思考后放置在反转字符串后的末尾
# s = '' s+=str不改变str的值
# 思路：从后往前遍历，遇见空格就对先加入的单词进行反转。
# 最后一个单词后面没有空格，需要单独考虑、

def ReverseSentence(s):
    temp = ''
    start = 0
    end = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            #start表示一个单词的起始位置，end表示结束位置，包含了空格
            # temp[-1:-length:-1]表示length-1个元素，不包括空格
            end = len(s) - i
            length = end - start
            temp =  temp[:start] + temp[-1:-length:-1] + ' '
            start = end
        else:
            temp += s[i]

        # 反转最后一个单词
        if i == 0:
            length = len(s) - start + 1
            temp = temp[0:start]  + temp[-1:-length:-1]

    return temp


# 别人的解法
# def ReverseSentence2( s):
#         # write code here
#         l=s.split(' ')
#         return ' '.join(l[::-1])

s = "Iabbb am a student"
result = ReverseSentence(s)
print(result)

# for i in result:
#     print(i)
print(len(result))