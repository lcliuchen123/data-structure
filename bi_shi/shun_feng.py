
# 一、单选
# 进程实体；单例模式；数据库并发，连接池；hive sql执行顺序；CRC检验；高响应比优先调度算法；存储器的地址线和数据线。
# python面向对象，回滚rollback，最优二叉树；c++中的assert宏和verify宏。

# 二、问答 sql

# 三、编程
# 每个人可能会一种或者多种语言，可以配备学习机或者通过其他人使
# 每个人能够相互交流，请问最少需要多少个学习机（每个人学习机可以让一个人短暂的掌握一门语言）？
# 超时，AC 9%
import sys
import numpy as np
from itertools import product

line = sys.stdin.readline()
line = line.strip().split()
n = int(line[0])
m = int(line[1])
k = int(line[2])
info_dict = {}
for i in range(k):
    line = sys.stdin.readline()
    line = line.strip().split()
    key = int(line[0])
    value = int(line[1])
    if not info_dict.get(key):
        info_dict[key] = {value}
    else:
        info_dict[key] = info_dict.get(key).add(value)

array = np.zeros((n, n))
print(info_dict.items())
flag = False
for i in range(0, n):
    for j in range(i + 1, n):
        keys = list(info_dict.keys())
        print(i, j)
        if i+1 in keys and  j+1 in keys:
            print("keys")
            x = info_dict[i+1] & info_dict[j+1]
            print("x: ",x)
            if len(x) == 0:
                for y, z in product(info_dict[i+1], info_dict[j+1]):
                    s = {y, z}
                    print("s: ",s)
                    for item in info_dict.values():
                        print("item: ",item)
                        print("jiao_ji: ",(s <= item))
                        if  s <= item:
                            flag = True
                            break
                    if not flag:
                            array[i, j] = 1
                            info_dict[i+1] = info_dict[i+1] | info_dict[j+1]
                            print("1: ",(i,j))
                            print("i+1: ",info_dict[i+1])
                            break
        else:
            print("2: ", (i, j))
            array[i,j] = 1
            info_dict[i + 1] = info_dict.get(i+1,set()) | info_dict.get(j + 1,set())
            print("i+2: ",info_dict[i+1])

res = np.sum(array)
print(array)
print(int(res))

# 3 3 2
# 2 3
# 3 1