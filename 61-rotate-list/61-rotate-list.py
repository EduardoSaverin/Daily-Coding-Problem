# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        last = None
        length = self.get_length(head, last)
        k = k % length
        if k == 0:
            return head
        break_index = length - k
        index = 1
        temp = head
        prev = None
        while index <= break_index:
            prev = temp
            temp = temp.next
            index += 1
        prev.next = None
        start = temp
        while temp.next:
            temp = temp.next
        temp.next = head
        return start
        
    def get_length(self, head, last):
        count = 0
        while head:
            last = head
            head = head.next
            count += 1
        return count