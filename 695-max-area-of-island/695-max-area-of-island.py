class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        visited = set()
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(self.dfs(row, col, visited), max_area)
        return max_area
    
    def dfs(self, row: int, col: int, visited) -> int:
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]) or (row,col) in visited or self.grid[row][col] != 1:
            return 0
        area = 1
        visited.add((row, col))
        for i,j in [(-1,0), (0,1), (1,0), (0,-1)]:
            area += self.dfs(row+i, col+j, visited)
        return area