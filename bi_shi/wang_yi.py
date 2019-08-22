
# 网易笔试第一题 最大公约数
def get_max(a,b):
    if a < b:
        a, b = b, a
    while a %b !=0:
        tmp = a%b
        a = b
        b = tmp

    return b

# 第二题：按位或
def is_True(a,b,num_list):
    if not num_list:
        return "NO"
    if a == 1:
        num_list.append(b)
    else:
        num = b
        for i in num_list:
            num = num | i
        if num == b:
            return "YES"
        else:
            return "NO"

# 第三题：最大最小值 最大子序列里面的最小值

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     num_list = []
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         ans = is_True(values[0],values[1],num_list)
#         print(ans)


import sys
if __name__ == "__main__":
    # 读取第一行的n
    # first_line = sys.stdin.readline().strip().split()
    # length = int(first_line[0])
    # n = int(first_line[1])
    # second_line = sys.stdin.readline().strip().split()
    # values = list(map(int, second_line))
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     value = int(line)
    #     count = 0
    #     print("value: ",value)
    #     for j in range(len(values)):
    #         if values[j] >= value:
    #             values[j] = values[j] - 1
    #             count += 1
    #     print(count)

    print(get_max(6,4))