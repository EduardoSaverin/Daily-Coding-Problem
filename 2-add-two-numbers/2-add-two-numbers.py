# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = new = ListNode()
        while l1 and l2:
            num1 = l1.val
            num2 = l2.val
            sumation = num1 + num2 + carry
            carry = (sumation) // 10
            new_node = ListNode(sumation % 10)
            new.next = new_node
            new = new_node
            l1 = l1.next
            l2 = l2.next
        left_node = l1 or l2
        while left_node:
            num2 = left_node.val
            sumation = num2 + carry
            carry = (sumation) // 10
            new_node = ListNode(sumation % 10)
            new.next = new_node
            new = new_node
            left_node = left_node.next
        if carry:
            new_node = ListNode(carry)
            new.next = new_node
            new = new_node
        return head.next