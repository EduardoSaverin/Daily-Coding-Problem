"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [root]
        result = []
        while q:
            new_q = []
            temp = []
            for node in q:
                temp.append(node.val)
                for child in node.children:
                    new_q.append(child)
            q = new_q
            result.append(temp)
        return result