# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解法一：
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global res #全局变量
        res = []
        self.mid_search(pRoot)
        if k <= 0 or k > len(res):
            return None
        else:
            return res[k - 1]

    # 二叉树的中序遍历
    def mid_search(self, pRoot):
        if not pRoot:
            return None

        self.mid_search(pRoot.left)
        res.append(pRoot)
        self.mid_search(pRoot.right)


# 解法二：中序遍历，不用全局变量

# 返回对应节点TreeNode
class Solution1:
    # 返回对应节点TreeNode
    index = 0

    def KthNode(self, pRoot, k):
        # write code here

        if pRoot is not None:
            node = self.KthNode(pRoot.left, k)
            if node:
                return node

            self.index += 1
            if k == self.index:
                return pRoot

            node = self.KthNode(pRoot.right, k)
            if node:
                return node
        else:
            return None


