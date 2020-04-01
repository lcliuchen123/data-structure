#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2020/3/31 17:37
@Author  : Chen Liu
@FileName: floor.py
@Software: PyCharm
"""


# 跳台阶
def floor(n):
    if n == 0:
        return
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]
