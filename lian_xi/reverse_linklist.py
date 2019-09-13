

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linklist(l):
    if len(l) == 0:
        return
    root = ListNode(l[0])
    curr = root
    for i in range(1, len(l)):
        curr.next = ListNode(l[i])
        curr = curr.next

    return root

def print_linklist(root):
    while root:
        print(root.val)
        root = root.next

def reverse_linklist(root):
    if root == None:
        return

    p = None
    q = root

    while q:
        r = q.next
        q.next = p
        p = q
        q = r

    return p


def  reverse_2(root):
    if not root:
        return
    p = root
    q= root.next
    r = q.next
    while r:
        q.next = p
        p =q
        q =r
        r = r.next
    q.next = p
    root.next = None

    return q


if __name__ == "__main__":
    l = [1,2,3,4,5]
    root = create_linklist(l)
    # print_linklist(root)

    # reverse_root = reverse_linklist(root)
    reverse_root = reverse_2(root)
    print_linklist(reverse_root)
