
class TreeNode():
    def __init__(self,x):
        self.left =None
        self.right = None
        self.val  = x

class Solution():
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    # 利用先序遍历和中序遍历的列表获取原始二叉树
    def get_tree(self,pre,mid):

        if len(pre) == 0 or len(mid) == 0:
            return None

        root = TreeNode(pre[0])
        for order, mid_element in enumerate(mid):
            if  root.val == mid_element:
                root.left = self.get_tree(pre[1:order+1], mid[:order])
                root.right = self.get_tree(pre[order+1:], mid[order+1:])
                return root

    # 将二叉树转化为双向排序列表:中序遍历，改变每一个节点的指向
    def convert(self,root):
        if not root:
            return
        self.convert(root.left)
        if self.list_head == None:
            self.list_head = root
            self.list_tail = root
        else:
            self.list_tail.right = root
            root.left = self.list_tail
            self.list_tail = root

        self.convert(root.right)
        return self.list_head

    # 逆序或者正序打印
    def get_order(self,root):
        while root.right:
            print(root.val, end=" ")
            root = root.right
        print(root.val)
        while root:
            print(root.val,end=" ")
            root = root.left

if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [4,2,1,3,6,5,7]
    middleorder_seq = [1,2,3,4,5,6,7]
    treeRoot1 = solution.get_tree(preorder_seq,middleorder_seq)
    head = solution.convert(treeRoot1)
    solution.get_order(head)
