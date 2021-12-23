class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        result = []
        def recursion(node, path):
            # Base Condition
            if node == target:
                result.append(path)
            for adj in graph[node]:
                path.append(adj)
                recursion(adj, path[:])
                path.pop()
        recursion(0, [0])
        return result