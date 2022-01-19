# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    # Follow Up
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
                
    
    def detectCycleOld(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        ptr = head
        while ptr and ptr not in s:
            s.add(ptr)
            ptr = ptr.next
        return None if ptr is None else ptr