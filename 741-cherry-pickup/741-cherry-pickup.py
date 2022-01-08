class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        visited = {}
        return max(self.dfs(0,0,0,0, len(grid), len(grid[0]), grid, visited), 0)
    
    def dfs(self, row1, col1, row2, col2, rows, cols, grid, visited):
        if (row1,col1,row2,col2) in visited:
            return visited[(row1,col1,row2,col2)]
        if row1 == rows or row2 == rows or col1 == cols or col2 == cols or grid[row1][col1] == -1 or grid[row2][col2] == -1:
            return -float("inf")
        if row1 == (rows-1) and row2 == (rows-1) and col1 == (cols-1) and col2 == (cols-1):
            return grid[rows-1][cols-1]
        dfs1 = self.dfs(row1+1, col1, row2+1, col2, rows, cols, grid, visited)
        dfs2 = self.dfs(row1+1, col1, row2, col2+1, rows, cols, grid, visited)
        dfs3 = self.dfs(row1, col1+1, row2+1, col2, rows, cols, grid, visited)
        dfs4 = self.dfs(row1, col1+1, row2, col2+1, rows, cols, grid, visited)
        result = max(dfs1, dfs2, dfs3, dfs4)
        if row1 == row2 and col1 == col2:
            result += grid[row1][col1]
        else:
            result += grid[row1][col1] + grid[row2][col2]
        visited[(row1,col1,row2,col2)] = result
        return result
        