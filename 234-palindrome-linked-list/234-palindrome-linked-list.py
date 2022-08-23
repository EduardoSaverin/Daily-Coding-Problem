# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        t = ""
        def recursion(head):
            nonlocal s
            nonlocal t
            if not head:
                return 
            s += str(head.val)
            recursion(head.next)
            t += str(head.val)
        recursion(head)
        return s == t
        