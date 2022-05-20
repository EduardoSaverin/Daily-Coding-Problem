class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        return self.dfs(0,0)
    
    @lru_cache
    def dfs(self, row, col):
        if row >= len(self.grid) or col >= len(self.grid[0]) or self.grid[row][col] == 1:
            return 0
        if row == len(self.grid)-1 and col == len(self.grid[0])-1:
            return 1
        dfs1 = self.dfs(row+1, col)
        dfs2 = self.dfs(row, col+1)
        return dfs1 + dfs2