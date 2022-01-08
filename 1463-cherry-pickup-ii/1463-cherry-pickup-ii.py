class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        visited = {}
        return max(self.dfs(grid, visited, 0, 0, 0, len(grid[0])-1), 0)
    
    def dfs(self, grid, visited, row1, col1, row2, col2):
        if (row1,col1,row2,col2) in visited:
            return visited[(row1,col1,row2,col2)]
        rows = len(grid)
        cols = len(grid[0])
        # Robots going outside of grid
        if col1 in (-1, cols) or col2 in (-1, cols):
            return -float("inf")
        # Both Reached End
        if row1 == rows and row2 == rows:
            return 0
        # Robot One Moves Below Left Position
        dfs1 = self.dfs(grid, visited, row1+1, col1-1, row2+1, col2-1)
        dfs2 = self.dfs(grid, visited, row1+1, col1-1, row2+1, col2)
        dfs3 = self.dfs(grid, visited, row1+1, col1-1, row2+1, col2+1)
        # Robot One Moves Below Only
        dfs4 = self.dfs(grid, visited, row1+1, col1, row2+1, col2-1)
        dfs5 = self.dfs(grid, visited, row1+1, col1, row2+1, col2+1)
        dfs6 = self.dfs(grid, visited, row1+1, col1, row2+1, col2)
        #Robot One Moves Below Right Position
        dfs7 = self.dfs(grid, visited, row1+1, col1+1, row2+1, col2-1)
        dfs8 = self.dfs(grid, visited, row1+1, col1+1, row2+1, col2+1)
        dfs9 = self.dfs(grid, visited, row1+1, col1+1, row2+1, col2)
        # Get Max of all possible movement
        result = max(dfs1, dfs2, dfs3, dfs4, dfs5, dfs6, dfs7, dfs8, dfs9)
        
        # Both Robot are on same grid spot
        if row1 == row2 and col1 == col2:
            result += grid[row1][col1]
        else:
            result += grid[row1][col1] + grid[row2][col2]
        visited[(row1,col1, row2,col2)] = result
        return result
        