# 130. Surrounded Regions

## Medium

***

Given an `m x n` matrix `board` containing `'X'` and `'O'`, _capture all regions that are 4-directionally surrounded by_ `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
```

**Example 2:**

```
Input: board = [["X"]]
Output: [["X"]]
```

&#x20;

**Constraints:**

* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 200`
* `board[i][j]` is `'X'` or `'O'`.

```python
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
```
