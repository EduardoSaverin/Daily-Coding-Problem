class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Seems like a graph where together connected components needs to be 
        # sorted. Example 0 -> 1 -> 2 if these indices are connected then we need to simple sort these
        d = defaultdict(list)
        for source, destination in pairs:
            d[source].append(destination)
            d[destination].append(source)
        self.d = d
        visited = [False]*(len(s))
        self.visited = visited
        result = ['']*len(s)
        for vertex in range(len(s)):
            if not self.visited[vertex]:
                chars = []
                indices = []
                self.DFS(s, vertex, chars, indices)
                chars.sort()
                indices.sort()
                for index in range(len(chars)):
                    result[indices[index]] = chars[index]
        return ''.join(result)
    
    def DFS(self, s, vertex, chars, indices):
        chars.append(s[vertex])
        indices.append(vertex)
        self.visited[vertex] = True
        for adj in self.d[vertex]:
            if not self.visited[adj]:
                self.DFS(s, adj, chars, indices)
