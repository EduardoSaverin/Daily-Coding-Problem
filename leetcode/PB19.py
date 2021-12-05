# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    # Dual Pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        pointer = head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next
        if count == 1 and n == 1:
            return None
        elif count == 1 and n == 0:
            return head
        elif count == n:
            return head.next
        pointer = head.next
        for _ in range(0,count-n-1):
            prev = pointer
            pointer = pointer.next
        prev.next = pointer.next
        return head

    # Single Pass
    def removeNthFromEndV2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return slow.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head