# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next 
        previous.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
        
    def merge(self, left, right):
        dummy = tail = ListNode(None)
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next
        