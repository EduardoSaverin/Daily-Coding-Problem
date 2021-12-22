# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        def recursion(right):
            nonlocal left
            if not right:
                return
            recursion(right.next)
            if left.next:
                temp = left.next
                left.next = right
                right.next = temp
                left = temp
            if left.next == right:
                left.next = None
        recursion(head)
        return left
            