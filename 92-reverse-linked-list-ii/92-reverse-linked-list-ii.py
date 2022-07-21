# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head
        starting = head
        stack = []
        count = 0
        leftNodePrev = None
        rightNodeNext = None
        prev = None
        while head:
            count += 1
            if left <= count <= right:
                if left == count:
                    leftNodePrev = prev
                if right == count:
                    rightNodeNext = head.next
                stack.append(head)
            prev = head
            head = head.next
        d = dummy = ListNode()
        while stack:
            dummy.next = stack.pop()
            dummy = dummy.next
        if leftNodePrev:
            leftNodePrev.next = d.next
        else:
            starting = d.next
        dummy.next = rightNodeNext
        return starting
        