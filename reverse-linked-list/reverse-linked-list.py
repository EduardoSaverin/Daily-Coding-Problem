# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        elif head.next is None:
            return head
        tail = None
        def recursion(head):
            nonlocal tail
            if head.next:
                # 5 = (4.next)
                # 4 = (3.next)
                node = recursion(head.next)
                if tail is None:
                    tail = node
                # print(head, head.next, node)
                # 4.next = None
                # 3.next = None
                head.next = None
                if node is None:
                    return head
                # 5.next = 4
                # 4.next = 3
                node.next = head
                # print('Node', node)
                # 4
                # 3 = 4.next
                node = node.next
                # print('Nodes Next', node)
                return node
            else:
                return head
        recursion(head)
        return tail