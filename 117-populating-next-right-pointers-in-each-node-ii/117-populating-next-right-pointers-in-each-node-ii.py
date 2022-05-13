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
        dq = deque()
        dq.append(root)
        dq.append('#')
        prev = None
        while dq:
            node = dq.popleft()
            if node == '#':
                if prev:
                    prev.next = None
                    prev = None
                if len(dq) != 0:
                    dq.append('#')
                continue
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            if prev:
                prev.next = node
            prev = node
        return root
                
                
                