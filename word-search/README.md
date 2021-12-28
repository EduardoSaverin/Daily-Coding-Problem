# 79. Word Search

## Medium

***

Given an `m x n` grid of characters `board` and a string `word`, return `true` _if_ `word` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

&#x20;

**Constraints:**

* `m == board.length`
* `n = board[i].length`
* `1 <= m, n <= 6`
* `1 <= word.length <= 15`
* `board` and `word` consists of only lowercase and uppercase English letters.

&#x20;

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # No Need to check for empty board since in contraints it is 1 minimum
        # Word to searc is also 1 minimum
        # Created visited matrix to not visit same node in dfs dual
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, visited, word, 0, i, j):
                    return True
        return False
        
    def dfs(self, board, visited, word, index, i ,j):
        if len(word) == index:
            # If we reach till this point it means we have matched all nodes till here
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or word[index] != board[i][j]:
            return False
        visited[i][j] = 1
        result = self.dfs(board, visited, word, index+1, i+1,j) or self.dfs(board, visited, word, index+1, i-1,j) or self.dfs(board, visited, word, index+1, i,j-1)  or self.dfs(board, visited, word, index+1, i,j+1) 
        # While self unit testing found that it will fail for 
        # [["A","S","C","E"],["S","F","C","S"],["A","D","E","E"]]
        # "ASFCCESEEDAS"
        # If below unvisit not done
        visited[i][j] = 0
        return result
```
