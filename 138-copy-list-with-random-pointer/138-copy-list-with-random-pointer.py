"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        ptr = head
        prev = None
        while ptr:
            node = Node(ptr.val) # Create Node
            temp = ptr.next # Store next
            ptr.next = node # insert inbetween
            node.next = temp # 
            ptr = temp
        ptr = head
        while ptr and ptr.next:
            ran = ptr.random
            ptr.next.random = ran.next if ran else None
            ptr = ptr.next.next
        ptr = head
        while ptr and ptr.next:
            if new_head is None:
                new_head = ptr.next
            if prev is not None:
                prev.next = ptr.next
            prev = ptr.next
            ptr = ptr.next.next
        return new_head