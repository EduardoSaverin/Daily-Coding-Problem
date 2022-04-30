class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.d = defaultdict(list)
        for index, [A,B] in enumerate(equations):
            self.d[A].append([B, values[index]])
            self.d[B].append([A, 1/ values[index]])
        result = []
        for query in queries:
            result.append(self.dfs(query))
        return result
        
    def dfs(self, query):
        start, end = query
        if start not in self.d or end not in self.d:
            return -1.0
        dq = deque([(start, 1.0)])
        visited = set()
        while dq:
            node, val = dq.popleft()
            if node == end:
                return val
            visited.add(node)
            for adj, value in self.d[node]:
                if adj not in visited:
                    dq.append((adj, val*value))
        return -1.0
            
        