class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.dfs(m,n, startRow, startColumn, maxMove) % (10**9 + 7)
    
    @lru_cache(None)
    def dfs(self, m, n , row, col, movesLeft):
        if ((row < 0 or row >= m) or (col < 0 or col >= n)) and movesLeft >= 0:
            return 1
        if movesLeft < 0:
            return 0
        return self.dfs(m,n,row-1,col, movesLeft-1) +  self.dfs(m,n,row,col+1, movesLeft-1) + self.dfs(m,n,row+1,col, movesLeft-1) + self.dfs(m,n,row,col-1, movesLeft-1)