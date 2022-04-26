class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree Prims Algo
        n = len(points)
        total_cost = 0
        edges_count = 0
        
        visited = [False]*n
        min_dist = [math.inf]*n
        min_dist[0] = 0 # Start Point
        
        while edges_count < n:
            current_min_edge = math.inf
            current_node = -1
            # Find node with minimum distance
            for node in range(n):
                if not visited[node] and min_dist[node] < current_min_edge:
                    current_node = node
                    current_min_edge = min_dist[node]
                
            total_cost += current_min_edge
            edges_count += 1
            visited[current_node] = True
            
            for next_node in range(n):
                weight = abs(points[current_node][0] - points[next_node][0]) + abs(points[current_node][1] - points[next_node][1])
                if not visited[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight
        return total_cost