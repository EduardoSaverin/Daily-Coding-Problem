"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = []
        q.append(root)
        q.append(None) # <--  Marking end of current level
        prev = None
        while q:
            current = q.pop(0)
            if current is None:
                if prev is None:
                    continue
                q.append(None)
                if prev is not None:
                    prev.next = None
                    prev = current
                continue
            if prev is not None:
                prev.next = current
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            prev = current
        return root
            
        