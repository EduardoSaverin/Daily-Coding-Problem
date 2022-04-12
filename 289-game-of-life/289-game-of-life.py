class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    count = self.getCount(board, row, col)
                    if count == 3:
                        board[row][col] = 2
                else:
                    count = self.getCount(board, row, col)
                    if count < 2 or count > 3:
                        board[row][col] = 3
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 3:
                    board[row][col] = 0
        
    def getCount(self, board, row, col):
        count = 0
        if self.isValid(board, row-1, col-1):
            count += board[row-1][col-1] % 2
        if self.isValid(board, row-1, col):
            count += board[row-1][col] % 2
        if self.isValid(board, row-1, col+1):
            count += board[row-1][col+1] % 2
        if self.isValid(board, row, col+1):
            count += board[row][col+1] % 2
        if self.isValid(board, row+1, col+1):
            count += board[row+1][col+1] % 2
        if self.isValid(board, row+1, col):
            count += board[row+1][col] % 2
        if self.isValid(board, row+1, col-1):
            count += board[row+1][col-1] % 2
        if self.isValid(board, row, col-1):
            count += board[row][col-1] % 2
        return count
        
    
    def isValid(self, board, row, col):
        rows = len(board)
        cols = len(board[0])
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return False
        return True
        