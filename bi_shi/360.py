
# import sys
# import numpy as np
#
#
# line = sys.stdin.readline().strip()
# line = line.split()
# n = int(line[0])
# m = int(line[1])
# array = np.zeros((n, m))
# row_max = []
# col_max = []
# for i in range(n):
#     line = sys.stdin.readline().strip()
#     line = line.split()
#     int_line = [int(x) for x in line]
#     row_max.append(max(int_line))
#     for j in range(m):
#         array[i][j] = int_line[j]
#
# for j in range(m):
#     col_max.append(max(array[:,j]))
#
# result = (sum(row_max)+sum(col_max)+n*m)*2
# print(int(result))


# 在一个古老的国度，这个国家的人并不懂得进位，
# 但是对取模情有独钟，因此诞生了一个经典的问题，
# 给出两个在m进制下含有n位的数字，你可以分别将这两个数各位上的数字重新排列，
# 然后将两个数按位对应相加并分别对m取模，
# 这样显然可以得到一个新的m进制下的n位数(可能存在前导0)，
# 但是这个结果是不唯一的，问题来了，按照这样的操作，
# 能够得到的最大的m进制下的数字是多少呢。

import sys
import numpy as np

line = sys.stdin.readline().strip()
line = line.split()
n = int(line[0])
m = int(line[1])
array = np.zeros((2,n))
for i in range(2):
    line = sys.stdin.readline().strip()
    line = line.split()
    int_line = [int(x) for x in line]
    for j in range(n):
        array[i,j] = int_line[j]
col_list =[]
for  k in range(n):
    col_max = sum(array[:,k])
    col_mod = int(col_max) % m
    col_list.append(col_mod)
col_list.sort()
print(col_list)