class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0 and self.dfs(grid, row, col):
                    count += 1
        return count
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        # Reached 1's Boundary
        if grid[row][col] == 1:
            return True
        # Prevent Recursion Error by marking it as 1 as visited
        grid[row][col] = 1
        # Previous Line that gave Wrong Answer
        #return self.dfs(grid, row-1, col) and self.dfs(grid, row, col-1) and self.dfs(grid, row+1, col) and self.dfs(grid, row, col+1)
        dfs1 = self.dfs(grid, row-1, col) 
        dfs2 = self.dfs(grid, row, col-1)
        dfs3 = self.dfs(grid, row+1, col)
        dfs4 = self.dfs(grid, row, col+1)
        # Traverese all direction before making decision
        return dfs1 and dfs2 and dfs3 and dfs4