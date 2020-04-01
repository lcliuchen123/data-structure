
# 升序数组转化为二叉排序树
class Node:
    def __init__(self,val):
        self.val=val
        self.left=[]
        self.right=[]


def solve(_list):
    if _list==[]:
        return
    ind=int((len(_list)-1)/2)
    node=Node(_list[ind])
    if ind!=0:
        node.left=solve(_list[0:ind])
        node.right=solve(_list[ind+1:])
    elif ind==0 and len(_list)==2:
        node.right=solve([_list[1]])
    return node


def preorder(root):
    if root==[]:
        return
    preorder(root.left)
    print(root.val)
    preorder(root.right)


_list=[1,2,3,4,5,6,7]
root=solve(_list)
preorder(root)

#
def count_number(number_list):
    i = 0
    length = len(number_list)
    while i < length:
        temp = number_list[i] - 1
        if temp < 0:
            i+=1
            continue
        elif number_list[temp] > 0:
            i += 1
            number_list[temp] = -1
        else:
            number_list[i] = 0
            i+=1
    return number_list


print(count_number([6,2,1,3,2,4]))