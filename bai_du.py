#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2020/3/30 16:34
@Author  : Chen Liu
@FileName: bai_du.py
@Software: PyCharm
"""


# 判断链表是否有环，如果有返回交点，
def is_exisit(root):
    if not root:
        return None

    searched_list = []
    while root:
        searched_list.append(root)
        root = root.next
        if root in searched_list:
            return root

    return None


# 解法二：快慢指针
# 思路：如果存在环，快指针和慢指针一定会相遇，如果不存在，则快指针走到头
def is_exisit2(root):
    if not root:
        return
    flag = False
    slow = root
    fast = root
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            flag = True

    # 当慢节点第一次到达环入口节点时，快节点也肯定在入口节点
    if flag:
        slow = root
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    return None


# 数组，正整数和负整数，连续子数组
def max_sum(nums_list):
    """没有考虑全是负数的情况"""
    if not nums_list:
        return None

    # 初始化和为第一个元素
    result = 0
    max_sum = -float('inf')
    for num in nums_list:
        # 如果和小于0，则将该和更新为当前元素
        if result < 0:
            result = num
        # 如果和大于0，则加上当前值
        else:
            result += num
        # 更新最大值
        max_sum = max(max_sum, result)

    return max_sum


if __name__ == "__main__":
    nums_list = [-1, -2, -4, -1, -6, -7]
    print(max_sum(nums_list))
