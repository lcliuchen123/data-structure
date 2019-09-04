
# 判断一个树是不是二叉搜索树
class TreeNode():
    def __init__(self,x):
        self.val =x
        self.left =None
        self.right = None


# 生成树，根节点怎么选择？？？？？？？？root=None不能去掉
def build_tree(data,index=0):
    if len(data) == 0:
        return None
    root =None      #定义一个空的根节点???????????
    if index < len(data):
        root = TreeNode(data[index])
        root.left = build_tree(data,2*index+1)
        root.right = build_tree(data,2*index+2)

    return root


# 中序遍历
def print_tree(root):
    if root is None:
        return

    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


# 获取中序遍历结果
def get_mid_result(root,result):
    if root is None:
        return
    if root.left:
        get_mid_result(root.left,result)

    result.append(root.val)

    if root.right:
        get_mid_result(root.right,result)


if __name__ == "__main__":
    data = [10,5,15,3,7,13,18]
    root = build_tree(data)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    # print_tree(root)
    # result = []
    # get_mid_result(root,result)
    # print("result: ",result)
    # flag = True
    # for i in range(len(result)-1):
    #     if  result[i] > result[i+1]:
    #         flag = False
    #         break
    #
    # print(flag)