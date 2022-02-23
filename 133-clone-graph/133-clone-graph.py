"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        d = {}
        d[node] = Node(node.val)
        self.dfs(node, d)
        return d[node]
    
    def dfs(self, node, d):
        for ne in node.neighbors:
            if ne not in d:
                d[ne] = Node(ne.val)
                self.dfs(ne, d)
            d[node].neighbors.append(d[ne])
            