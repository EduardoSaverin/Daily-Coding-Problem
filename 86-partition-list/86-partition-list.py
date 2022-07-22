# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1,less = None, None
        p2,more = None, None
        while head:
            if head.val < x:
                if less is None:
                    p1, less = head, head
                else:
                    less.next = head
                    less = head
            else:
                if more is None:
                    p2, more = head, head
                else:
                    more.next = head
                    more = head
            head = head.next
        if more:
            more.next = None
        if less:
            less.next = p2
        return p1 or p2