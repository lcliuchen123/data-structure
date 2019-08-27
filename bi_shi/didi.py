
# 一、选择
# 用户粘性是指用户对APP的依赖度、忠诚度和使用率。
# 生产者剩余指卖者得到的量减去其最低所能接受的量。
# 方差分析
# 假设检验
# 二、简答
# 特征重要性排序，特征分析
# 过拟合解决办法
# 参数估计与假设检验的区别
# 方差分析公式
# 三、编程
# 1、sql题 AC100%
# 2、一元一次方程的根，AC了20%，暂时不知道原因在哪

import sys

line = sys.stdin.readline()
line = line.strip().split()
if line:
    print(line[0][:-1])
    k = float(line[0][:-1])
    if k != 0:
        b = int(line[2])
        if line[1] == '-':
            x = b // k
        else:
            x = b // k

        print("x=%.1f" % x)