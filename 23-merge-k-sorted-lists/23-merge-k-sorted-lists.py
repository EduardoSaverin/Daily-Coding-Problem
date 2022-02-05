# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0 # This is not useful(only used for comparison) but create so that we don't get error in heap
        # Push First K elements each from one of the K list
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, count, node))
                count+=1
        head = dummy = ListNode()
        # Pick min from heap and put the next element of that list to which this element belongs
        while min_heap:
            val, _ ,node = heapq.heappop(min_heap)
            if node:
                head.next = node
                head = node
                node = node.next
                if node:
                    heapq.heappush(min_heap, (node.val, count, node))
                    count+=1
        return dummy.next