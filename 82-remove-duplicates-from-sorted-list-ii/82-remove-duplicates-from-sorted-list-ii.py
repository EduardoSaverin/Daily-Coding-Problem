# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = previous = ListNode()
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and (head.val == head.next.val):
                    head = head.next
                previous.next = head.next
            else:
                previous = previous.next
            head = head.next
        return dummy.next