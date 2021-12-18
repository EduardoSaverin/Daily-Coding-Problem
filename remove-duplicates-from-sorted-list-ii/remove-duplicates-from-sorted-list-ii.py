# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        new = head
        prev = None
        old = None
        if head.next is None:
            return head
        prev = new
        new = new.next
        repeat = False
        newHead = None
        while new:
            if new.val != prev.val:
                if not repeat:
                    if old is None:
                        old = prev
                        if newHead is None:
                            newHead = old
                    else:
                        old.next = prev
                        old = prev
                prev = new
                new = new.next
                repeat = False
            elif new.val == prev.val:
                repeat = True
                prev = new
                new = new.next
        if newHead is None and not repeat:
            return prev
        elif newHead is None:
            return None
        if not repeat:
            old.next = prev
        else:
            old.next = None
        return newHead