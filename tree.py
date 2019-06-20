

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(data, index=0):
    if len(data) == 0:
        return None
    root = None
    if index < len(data):
        root = TreeNode(data[index])
        root.left = create_tree(data, 2*index+1)
        root.right = create_tree(data, 2*index+2)

    return root

def cengci_search(root):
    if root is None:
        return None
    pre_list = []
    final_result = []
    pre_list.append(root)
    while len(pre_list)> 0:
        curr_val = []
        curr_list = []
        for i in pre_list:
            curr_val.append(i.val)
            if i.left:
                curr_list.append(i.left)
            if i.right:
                curr_list.append(i.right)
        pre_list = curr_list
        final_result.append(curr_val)
    return final_result

def xian_search(root):
    if root==None:
        return
    while root:
        print(root.val)
        xian_search(root.left)
        xian_search(root.right)

data=[9,20,None,15,8,30,31]
root=create_tree(data)
# xian_search(root)
print(cengci_search(root))


# 字典树
import collections
class DTreeNode:
    def __init__(self):
        self.isStr = False
        self.node = collections.defaultdict(DTreeNode)
        self.count =1

class Trie:
    def __init__(self):
        self.root = DTreeNode()

    def insert(self,word):
        curr =self.root
        word = word.lower()
        for ch in word:
            if ch in curr.node:
                curr.node[ch].count+=1
            curr = curr.node[ch]
        curr.isStr = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.node:
                return False
            curr = curr.node[ch]

        return curr.isStr

    def start_with(self,prefix):
        # 返回以prefix为前缀的单词个数
        curr = self.root
        for ch in prefix:
            if ch not in curr.node:
                return 0
            curr = curr.node[ch]
        return curr.count

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.start_with("app"))