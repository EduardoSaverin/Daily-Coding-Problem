# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            node1 = ptr
            node2 = ptr.next
            node1.val, node2.val = node2.val, node1.val
            ptr = node2.next
        return head