# 1091. Shortest Path in Binary Matrix

## Medium

***

Given an `n x n` binary matrix `grid`, return _the length of the shortest **clear path** in the matrix_. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

* All the visited cells of the path are `0`.
* All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/example1\_1.png)

```
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/example2\_1.png)

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

**Example 3:**

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

&#x20;

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 100`
* `grid[i][j] is 0 or 1`

```python
class Solution:
    def __init__(self):
        # This is very common thing that can be used for all-direction moving
        self.directions=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If [0,0] is 1 or bottom-right is 1 then return -1
        # because there will be no path
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        visited = [[-1 for j in range(col)] for i in range(row)]
        # [Row Index, Col Index, Moves]
        q = deque()
        q.append((0,0,1))
        visited[0][0] = 0
        while q:
            r,c,m = q.popleft()
            if r == (row-1) and c == (col-1):
                return m
            for dr,dc in self.directions:
                newR = r+dr
                newC = c+dc
                if self.isPathValid(grid, visited, newR, newC):
                    visited[newR][newC] = 0
                    q.append((newR,newC,m+1))
        return -1
            
    def isPathValid(self,grid, visited, row,col):
        if 0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1 and visited[row][col] == -1 and grid[row][col] == 0:
            return True
        return False
```
