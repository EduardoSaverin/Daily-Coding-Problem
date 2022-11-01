class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        @lru_cache(None)
        def recursion(row, col):
            if row == rows:
                return col
            elif grid[row][col] == 1 and col+1 < cols and grid[row][col+1] == 1:
                return recursion(row+1, col+1)
            elif grid[row][col] == -1 and col-1 >= 0 and grid[row][col-1] == -1:
                return recursion(row+1, col-1)
            return -1
        return [recursion(0, col) for col in range(cols)]