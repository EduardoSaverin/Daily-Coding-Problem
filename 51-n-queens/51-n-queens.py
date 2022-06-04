class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDia = set()
        negDia = set()
        res = []
        board = [["."]*n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDia or (r-c) in negDia:
                    continue
                # Found The Place for Queen
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1) # Do the backtrack for next row
                # Bactrack previous row Queen Position
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res