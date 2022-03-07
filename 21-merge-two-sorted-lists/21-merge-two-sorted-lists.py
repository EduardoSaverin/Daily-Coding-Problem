# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        head = pointer = None
        while list1 and list2:
            temp = None
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            if temp is not None:
                if head is None:
                    head = temp
                if pointer is None:
                    pointer = temp
                else:
                    pointer.next = temp
                    pointer = pointer.next
        if list1 is not None:
            pointer.next = list1
        elif list2 is not None:
            pointer.next = list2
        return head