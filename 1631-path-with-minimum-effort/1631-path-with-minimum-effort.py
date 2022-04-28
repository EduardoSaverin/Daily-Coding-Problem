class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #.
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.grid = heights
        low = 0
        high = 10**6
        while low < high:
            mid = low + (high-low) // 2
            if self.dfs(mid):
                high = mid
            else:
                low = mid + 1
        return low
        
        
    def dfs(self, threshold):
        visited = {(0,0)}
        dq = deque([(0,0)])
        while dq:
            x, y = dq.popleft()
            # Reached bottom right
            if (x,y) == (self.rows-1, self.cols-1):
                return True
            for r,c in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
                if (r,c) not in visited and (0 <= r < self.rows and 0 <= c < self.cols) and abs(self.grid[r][c] - self.grid[x][y]) <= threshold:
                    visited.add((r,c))
                    dq.append((r,c))
        return False
                    
                
        
        
        
        
        
        
        