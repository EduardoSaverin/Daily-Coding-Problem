class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        visited = {}
        self.dfs(dungeon, 0 ,0, visited)
        return visited[(0,0)]
    
    def dfs(self, grid, row, col, visited):
        if (row,col) in visited:
            return visited[(row,col)]
        rows = len(grid)
        cols = len(grid[0])
        if row == rows or col == cols:
            return float("inf")
        
        health = float("inf")
        this = grid[row][col]
        dfs1 = self.dfs(grid, row+1, col, visited)
        dfs2 = self.dfs(grid, row, col+1, visited)
        health = min(health, dfs1, dfs2)
        
        if health == float("inf"):
            if this < 0:
                health = 1 - this
            else:
                health = 1
        elif health > this:
            health = health - this
        else:
            health = 1
        visited[(row,col)] = health
        return health
            
        