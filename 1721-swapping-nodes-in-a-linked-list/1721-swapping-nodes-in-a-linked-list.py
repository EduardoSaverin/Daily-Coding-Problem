# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        # (k-1) since it is given as 1-Indexed
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        new_head = pointer = None
        for num in arr:
            temp = ListNode(num)
            if new_head is None:
                pointer = new_head = temp
            else:
                pointer.next = temp
                pointer = temp
        return new_head
            