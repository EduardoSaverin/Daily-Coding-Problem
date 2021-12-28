class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j] = 1 if i == 0 or j ==0 else arr[i-1][j] + arr[i][j-1]
        return arr[m-1][n-1]