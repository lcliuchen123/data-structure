

# 二叉树的层次遍历
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def create_tree(data,index=0):
    if len(data)==0:
        return None
    root=None
    if index<len(data):
        root=TreeNode(data[index])
        root.left=create_tree(data,2*index+1)
        root.right=create_tree(data,2*index+2)
    return root

def  cengci_search(root):
    if root==None:
        return None
    pre_list=[]  #存放每层的结点值
    pnode_list=[]#存放每层的结点
    pnode_list.append(root)
    while len(pnode_list)>0:
        current_val=[] #存放当前节点值
        current_node_list=[] #存放当前节点值
        for node in pnode_list:
            current_val.append(node.val)
            if node.left and node.left.val is not None:
                current_node_list.append(node.left)
            if node.right and node.right.val is not None:
                current_node_list.append(node.right)
        pre_list.append(current_val)
        pnode_list=current_node_list

    return pre_list

data=[9,20,None,15,8,30,31]
root=create_tree(data)
print(cengci_search(root))

#快速排序

def sort_nums(nums,start,end):
    if start>=end:
        return None
    i=start
    j=end
    tmp=nums[i]
    while i<j:
        while i<j and nums[j]>=tmp:
            j-=1
        if i<j:
            nums[i]=nums[j]
            i=i+1

        while i<j and nums[i]<=tmp:
            i+=1
        if i<j:
            nums[j]=nums[i]
            j-=1
    print(nums)
    nums[i]=tmp

    sort_nums(nums,start,i-1)
    sort_nums(nums,i+1,end)

    return nums

nums=[3,4,2,5,9]
# print(sort_nums(nums,0,4))

# 堆排序
def adjust_heap(nums,start,end):
    tmp=nums[start]
    i=2*start+1
    while i<end:
        if i+1<end and nums[i]<nums[i+1]:
            i+=1
        if nums[i]>tmp:
            nums[start]=nums[i]
            start=i
        else:
            break
        i=2*i+1
    nums[start]=tmp


def heap_sort(nums):
    if nums==None:
        return
 # 构建大顶堆:每个节点的元素值大于其左右节点的值
    i=len(nums)//2-1
    while i>=0:
        adjust_heap(nums,i,len(nums))
        i-=1
#         将栈顶元素与末尾元素交换
    for i in range(1,len(nums)):
        tmp=nums[0]
        nums[0]=nums[-i]
        nums[-i]=tmp
        adjust_heap(nums,0,len(nums)-i)

nums=[3,2,6,5,9,0]
heap_sort(nums)
print(nums)

# 字典树
import collections

class TreeNode:
    def __init__(self):
        self.isStr=False
        self.count=1
        self.node=collections.defaultdict(TreeNode)
class Trie:
    def __init__(self):
        self.root=TreeNode()

    def insert(self,word):
        curr=self.root
        word=word.lower()
        for ch in word:
            if ch in curr.node:
                curr.node[ch].count+=1
            curr=curr.node[ch]
        curr.isStr=True

    def search(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.node:
                return False
            curr=curr.node[ch]
        return curr.isStr

    def start_with(self,prefix):
        curr=self.root
        for ch in prefix:
            if ch not in curr.node:
                return 0
            curr=curr.node[ch]
        return curr.count

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.start_with("app"))