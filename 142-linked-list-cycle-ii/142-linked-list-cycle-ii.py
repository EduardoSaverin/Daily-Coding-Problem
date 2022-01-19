# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        ptr = head
        while ptr and ptr not in s:
            s.add(ptr)
            ptr = ptr.next
        return None if ptr is None else ptr