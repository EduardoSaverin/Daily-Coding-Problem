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
    def connect(self, root):
        nodes_list = []
        nodes_list.append(root)
        nodes_list.append(None)
        prev = None
        while len(nodes_list) > 0:
            curr = nodes_list.pop(0)
            if prev is not None:
                prev.next = curr
            if prev is None and curr is None:
                break
            prev = curr
            if curr is None:
                nodes_list.append(None)
                continue
            if curr.left is not None:
                nodes_list.append(curr.left)
            if curr.right is not None:
                nodes_list.append(curr.right)
        return root