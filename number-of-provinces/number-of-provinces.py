class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)
        result = []
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and not visited[col]:
                    result.append(self.findConnectedNodes(visited, isConnected, col))
        return len(result)
                
    def findConnectedNodes(self, visited, isConnected, node, connectedNodeList=[]):
        visited[node] = True
        for col in range(len(isConnected[0])):
            if isConnected[node][col] == 1 and not visited[col]:
                connectedNodeList.append(self.findConnectedNodes(visited, isConnected, col))
        return connectedNodeList