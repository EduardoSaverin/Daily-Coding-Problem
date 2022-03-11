# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        main = slow = fast = head
        index = 1
        length = self.get_length(head)
        k = k % length
        while index <= k and fast:
            index += 1
            fast = fast.next
        if not fast:
            return slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = main
        head = slow.next
        slow.next = None
        return head
    
    def get_length(self, head) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length