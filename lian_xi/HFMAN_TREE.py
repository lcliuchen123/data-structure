
class Node:
    def __init__(self,weight,ch="",code="",left=None,right=None):
        self.ch =ch
        self.weight = weight
        self.code = code
        self.left = left
        self.right = right

class Huffman_tree:
    def __init__(self,str="",root=None,char_dict={},node_list=[]):
        self.str = str
        self.root = root
        self.char_dict = char_dict
        self.node_list = node_list

    def get_char_dict(self):
        if not self.str:
            print("str is null in get_char_dict")
        for i in self.str:
            self.char_dict[i] = self.char_dict.get(i,0)+1

    def generate_node(self):
        for k,v in self.char_dict.items():
            self.node_list.append(Node(v,k))

    def sort(self, l):
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i].weight > l[j].weight:
                    l[i], l[j] = l[j], l[i]

    def sort_node_list(self):
        self.sort(self.node_list)

    def set_code(self, root):
        if root.left:
            root.left.code = root.code+'0'
            self.set_code(root.left)

        if root.right:
            root.right.code = root.code+'1'
            self.set_code(root.right)

    def create_parent(self):
        while len(self.node_list)>1:
            left = self.node_list[0]
            right = self.node_list[1]
            self.node_list.remove(left)
            self.node_list.remove(right)
            left.code = '0'
            right.code = '1'

            self.set_code(left)
            self.set_code(right)
            parent = Node(weight=left.weight+right.weight,left=left,right=right)
            self.node_list.insert(0,parent)
            self.sort_node_list()


    def output(self,root):
        if not root:
            return
        print(root.ch+": ",root.weight)
        self.output(root.left)
        self.output(root.right)

    def output_nodes(self):
        self.output(self.root)

    def create_huffman_tree(self,str):
        self.str = str
        self.get_char_dict()
        self.generate_node()
        self.sort_node_list()
        self.create_parent()
        self.root = self.node_list[0]

    def search(self,root,ch):
        if not root:
            return None
        if ch==root.ch:
            return root.code
        if self.search(root.left,ch):
            return self.search(root.left, ch)
        if self.search(root.right,ch):
            return self.search(root.right, ch)

    def encode(self,str):
        if not str:
            return
        encode = ""
        for ch in str:
            code = self.search(self.root,ch)
            print(ch+"::::", code)
            encode += code

        return encode

    def match_huffcode(self,root,substr):
        if not root:
            return
        if root.code == substr:
            return root.ch
        if self.match_huffcode(root.left,substr):
            return self.match_huffcode(root.left,substr)
        if self.match_huffcode(root.right,substr):
            return self.match_huffcode(root.right, substr)

    def decode(self,code_str):
        start = 0
        end = 1
        result =""
        while end<=len(code_str):
            ch = self.match_huffcode(self.root,code_str[start:end])
            if ch:
                result += ch
                start = end

            end += 1

        return result


if __name__ == "__main__":
    h = Huffman_tree()
    str = "1123545"
    h.create_huffman_tree(str)
    h.output_nodes()
    code = h.encode(str)
    print("encode: ", code)
    print("decode: ", h.decode(code))