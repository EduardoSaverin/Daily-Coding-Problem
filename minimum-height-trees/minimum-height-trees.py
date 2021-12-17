from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        childs = defaultdict(set)
        degree = defaultdict(int)
        for u,v in edges:
            childs[u].add(v)
            childs[v].add(u)
            degree[u] += 1
            degree[v] += 1
        # Now Find Leave Nodes
        leaves = [i for i in range(n) if degree[i] == 1]
        # This condition because we have to reduce nodes till 2
        while n > 2:
            size = len(leaves)
            n -= size
            while size:
                current_node = leaves.pop(0)
                for this_node_child in childs[current_node]:
                    degree[this_node_child] -= 1
                    if degree[this_node_child] == 1:
                        leaves.append(this_node_child) 
                size -= 1
        return leaves