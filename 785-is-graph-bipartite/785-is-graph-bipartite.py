class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        # Graph Coloring
        self.color = {}
        for index in range(len(graph)):
            if index not in self.color:
                # Initial Color of node is 0
                self.color[index] = 0
                # Call for DFS Traversal of this node
                if not self.dfs(index):
                    return False
        return True
        
    def dfs(self, index):
        # Traverse Adjacent Nodes
        for adj in self.graph[index]:
            # If Adjacent node is not colored yet, color it
            if adj not in self.color:
                self.color[adj] = 1 - self.color[index]
                # Call for this adjacent node DFS
                if not self.dfs(adj):
                    return False
            else:
                # If adjacent node is colored and having same color as node on other edge then 
                # it means they are in same setso return False
                if self.color[adj] == self.color[index]:
                    return False
        return True
        