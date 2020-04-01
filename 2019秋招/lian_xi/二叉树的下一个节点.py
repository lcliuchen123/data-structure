# -*- coding:utf-8 -*-

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  #父节点


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        #如果该结点有右子树，那么下一个节点是右子树最左端的节点
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        #如果该结点没有右子树，则找第一个当前节点的父节点为左节点的节点
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        #如果找不到对应的节点，返回空值
        return None