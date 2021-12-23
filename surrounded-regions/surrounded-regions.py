class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        for index in range(row):
            self.dfs(board, index, 0)
            self.dfs(board, index, col-1)
        for index in range(col):
            self.dfs(board, 0 , index)
            self.dfs(board, row-1, index)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
    def dfs(self, board, row, col):
        if self.isValid(board, row, col) and board[row][col] == "O":
            board[row][col] = "#"
            self.dfs(board, row-1,col)
            self.dfs(board, row, col-1)
            self.dfs(board, row+1,col)
            self.dfs(board, row, col+1)
        return
            
        
    def isValid(self, board, row, col):
        if 0 <= row <= (len(board)-1) and 0 <= col <= (len(board[0])-1):
            return True
        return False