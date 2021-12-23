class Solution:
    def __init__(self):
        # This is very common thing that can be used for all-direction moving
        self.directions=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If [0,0] is 1 or bottom-right is 1 then return -1
        # because there will be no path
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        visited = [[-1 for j in range(col)] for i in range(row)]
        # [Row Index, Col Index, Moves]
        q = deque()
        q.append((0,0,1))
        visited[0][0] = 0
        while q:
            r,c,m = q.popleft()
            if r == (row-1) and c == (col-1):
                return m
            for dr,dc in self.directions:
                newR = r+dr
                newC = c+dc
                if self.isPathValid(grid, visited, newR, newC):
                    visited[newR][newC] = 0
                    q.append((newR,newC,m+1))
        return -1
            
    def isPathValid(self,grid, visited, row,col):
        if 0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1 and visited[row][col] == -1 and grid[row][col] == 0:
            return True
        return False