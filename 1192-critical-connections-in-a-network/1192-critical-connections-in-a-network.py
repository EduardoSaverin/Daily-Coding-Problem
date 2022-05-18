class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = set()
        self.low = {}
        self.d = defaultdict(list)
        self.result = []
        for source, destination in connections:
            self.d[source].append(destination)
            self.d[destination].append(source)
        self.dfs(0,-1,0)
        return self.result
    
    def dfs(self, node, parent, rank):
        self.low[node] = rank
        self.visited.add(node)
        for adj in self.d[node]:
            if adj == parent:
                continue
            if adj not in self.visited:
                self.dfs(adj, node, rank+1)
            self.low[node] = min(self.low[node], self.low[adj])
            if rank < self.low[adj]:
                self.result.append([node, adj])
                
            