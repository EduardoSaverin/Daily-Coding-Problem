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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = [root,'#']
        prev = None
        while q:
            # print(q)
            node = q.pop(0)
            if node == '#':
                if prev is not None:
                    prev.next = None
                if q:
                    # node = q.pop(0)
                    prev = None
                    q.append('#')
                    continue
                else:
                    break
            else:
                if prev is not None:
                    prev.next = node
                prev = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
            
            
        