
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

def dele_common_ele(root):
    if  not root or not root.next:
        return
    head = ListNode(0) #头结点
    head.next = root
    pre = head
    last = head.next

    while last:
        if last.next and last.val == last.next.val:
            while last.next and last.val == last.next.val:
                last = last.next
            pre.next = last.next
            last = last.next
        else:
            pre = pre.next
            last = last.next

        return head.next