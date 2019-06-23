

# 哈夫曼树可以用来编码，出现频率越高的字符路径越短
class Node:
    # 创建节点类
    def __init__(self,weight,ch = "",left = None,right = None, code =""):
        self.ch = ch
        self.weight = weight
        self.left = left
        self.right = right
        self.code = code

class HFman_tree:
    def __init__(self,str="",root=None,node_list=[],char_dic={}):
        # 初始化哈夫曼树
        self.str = str    # 要编码或压缩的字符串
        self.root = root  # 根节点
        self.char_dic = char_dic  #str中的每个字符及其出现的频率
        self.node_list = node_list #保存节点的列表

    def get_char_dic(self):
        # 统计每个字符及其对应的频率
        if not self.str:
            print("str is null")

        for ch in self.str:
            self.char_dic[ch] = self.char_dic.get(ch,0)+1

    def generate_node(self):
        # 初始化节点列表，将每个字符加入列表
        for k,v in self.char_dic.items():
            new_node = Node(v, k)
            self.node_list.append(new_node)

    # 排序算法影响最终的编码结果，快排不稳定，冒泡稳定，编码不一样
    # def quick_sort(self, l , start , end):
    #     if start >= end:
    #         return
    #     i = start
    #     j = end
    #     tmp = l[start]
    #     while i < j:
    #         while i< j and l[j].weight >= tmp.weight:
    #             j -= 1
    #
    #         if i < j:
    #             l[i] = l[j]
    #             i += 1
    #
    #         while i<j and l[i].weight <= tmp.weight:
    #             i += 1
    #
    #         if i<j:
    #             l[j] = l[i]
    #             j -= 1
    #
    #     l[i] = tmp
    #     self.quick_sort(l, 0 , i-1)
    #     self.quick_sort(l, j+1, end)

    def quick_sort(self, l):
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i].weight > l[j].weight:
                    l[i], l[j] = l[j], l[i]


    def sort_node_list(self):
        length = len(self.node_list)
        if length == 0:
            print("the node_list is null")

        # self.quick_sort(self.node_list, 0, length-1)
        self.quick_sort(self.node_list)

    def create_parent(self):
        # 合并最小的两个节点，然后删除，并对左右子节点进行编码，
        # 生成新的节点，加入列表，然后重新排序
        while len(self.node_list) >1:
            # print("len: ",len(self.node_list))
            left = self.node_list[0]
            # print("left: ", left.ch)
            right = self.node_list[1]
            # print("right: ", right.ch)

            self.node_list.remove(left)
            self.node_list.remove(right)

            left.code = '0'
            right.code = '1'
            self.set_code(left)
            self.set_code(right)
            parent = Node(weight=left.weight+right.weight, left=left, right=right)
            self.node_list.insert(0,parent)
            # for i in range(len(self.node_list)):
            #     print(self.node_list[i].ch+" before sorting: ", self.node_list[i].weight)
            self.sort_node_list()
            # for i in range(len(self.node_list)):
            #     print( self.node_list[i].ch+" after sorting: ", self.node_list[i].weight)

    def set_code(self, root):
        # 为左右节点编码
        if root.left:
            root.left.code =root.code+ '0'
            self.set_code(root.left)

        if root.right:
            root.right.code =root.code+ '1'
            self.set_code(root.right)

    def  output_node(self,root):
        # 先序遍历
        if not root:
            return

        print(root.ch + ": ",root.weight)
        self.output_node(root.left)
        self.output_node(root.right)

    def output(self):
        self.output_node(self.root)

    def create_tree(self, str):
        self.str = str
        print("str: ", str)
        # 1.统计字符串中的字符以及字符出现的次数
        self.get_char_dic()
        # print(self.char_dic.items())
        # 2.生成节点
        self.generate_node()
        # print(len(self.node_list))
        # 3.按照节点排序
        self.sort_node_list()
        # print(len(self.node_list))
        # for i in range(len(self.node_list)):
        #     print("ch:: ", self.node_list[i].ch)
        # 4.找出最小的两个结点，合并后加入加入节点列表
        self.create_parent()
        # 5.重复第4步，把最后一个结点赋值给根节点
        # 最后一个节点就是合并后最大的节点
        self.root = self.node_list[0]

    def search(self, root,ch):
        if not root:
            return None

        if ch == root.ch:
            # print("find ch, and the code is %s" % root.code)
            return root.code

        if self.search(root.left,ch):
            return self.search(root.left,ch)
        if self.search(root.right,ch):
            return self.search(root.right, ch)

    def  encode_huffman(self, str):
        encode = ""
        if not str:
            print("str is null")
        for ch in str:
            code = self.search(self.root,ch)
            # print("ch: ",ch)
            # print("code: ", code)
            encode += code

        return encode

    def match_substr(self, root, code):
        if not root:
            return None
        if code == root.code:
            flag = True
            return root.ch, flag
        if self.match_substr(root.left, code):
            return self.match_substr(root.left, code)
        if self.match_substr(root.right, code):
            return self.match_substr(root.right, code)

    def decode(self, huffman_code):
        start = 0
        end = 1
        result = ""
        while end <= len(huffman_code):
            sub_code = huffman_code[start:end]
            ch, flag = self.match_substr(self.root,sub_code)

            if ch:
                print(sub_code)
                print("ch: ", ch)
                result += ch
                start = end

            end += 1

        return result


if __name__ == "__main__":
    h = HFman_tree()
    str = "1123545"
    h.create_tree(str)
    h.output()
    print(h.search(h.root,'1'))
    code = h.encode_huffman(str)
    print("encode: ", code)
    print(h.match_substr(h.root,'10'))
    print("decode: ", h.decode(code))