# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = head.next
        head.next = None
        while node:
            next_node = node.next
            ptr = dummy
            # note that we are creating reverse list here just like insertion order
            while ptr.next and ptr.next.val > node.val:
                ptr = ptr.next
            node.next = ptr.next
            ptr.next = node
            node = next_node
        node  = dummy.next
        head = None
        # Simple Reversing
        while node:
            next_node = node.next
            node.next = head
            head = node
            node = next_node
        return head