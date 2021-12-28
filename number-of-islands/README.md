# 200. Number of Islands

## Medium

***

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

&#x20;

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    s.add(self.getKey(row,col))
        count = 0
        while s:
            count += 1
            s = self.removeAllAdjacent(grid,s)
        return count
            
    def removeAllAdjacent(self, grid, s):
        q = []
        q.append(s.pop())
        while q:
            newKey = q.pop(0)
            if newKey in s:
                s.remove(newKey)
            row, col = newKey.split("-")
            row = int(row)
            col = int(col)
            if (row-1) >= 0 and grid[row-1][col] == '1' and self.getKey(row-1,col) in s:
                s.remove(self.getKey(row-1,col))
                q.append(self.getKey(row-1, col))
            if (col-1) >= 0 and grid[row][col-1] == '1' and self.getKey(row,col-1) in s:
                s.remove(self.getKey(row,col-1))
                q.append(self.getKey(row,col-1))
            if (row+1) < len(grid) and grid[row+1][col] == '1' and self.getKey(row+1,col) in s:
                s.remove(self.getKey(row+1,col))
                q.append(self.getKey(row+1, col))
            if (col+1) < len(grid[0]) and grid[row][col+1] == '1' and self.getKey(row,col+1) in s:
                s.remove(self.getKey(row,col+1))
                q.append(self.getKey(row, col+1))
        return s
                
    def getKey(self,row,col):
        return str(row)+"-"+str(col)
```
