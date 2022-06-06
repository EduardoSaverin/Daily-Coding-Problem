# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B = headA, headB
        lengthA = 0
        lengthB = 0
        while headA:
            headA = headA.next
            lengthA += 1
        while headB:
            headB = headB.next
            lengthB += 1
        headA, headB = A,B
        diff = abs(lengthA-lengthB)
        if lengthB < lengthA:
            while diff:
                diff -= 1
                headA = headA.next
        else:
            while diff:
                diff -= 1
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None