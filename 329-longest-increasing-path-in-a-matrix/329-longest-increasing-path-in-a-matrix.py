class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dp = [[0] * self.cols for i in range(self.rows)]
        result = 0
        for i in range(self.rows):
            for j in range(self.cols):
                result = max(result, self.dfs(i,j))
        return result
    
    def dfs(self, row, col):
        if not self.dp[row][col]:
            self.dp[row][col] = 1 + max(
                self.dfs(row-1, col) if row and self.matrix[row][col] < self.matrix[row-1][col] else 0,
                self.dfs(row+1, col) if row+1 < self.rows and self.matrix[row][col] < self.matrix[row+1][col] else 0,
                self.dfs(row, col-1) if col and self.matrix[row][col] < self.matrix[row][col-1] else 0,
                self.dfs(row, col+1) if col+1 < self.cols and self.matrix[row][col] < self.matrix[row][col+1] else 0
            )
        return self.dp[row][col]