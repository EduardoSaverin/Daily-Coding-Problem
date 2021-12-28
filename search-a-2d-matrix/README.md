# 74. Search a 2D Matrix

## Medium

***

Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-104 <= matrix[i][j], target <= 104`

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        minRow = 0
        maxRow = 0
        for r in range(row):
            if target <= matrix[r][col-1]:
                maxRow = r
            elif matrix[r][0] >= target:
                minRow = r
        for r in range(minRow, maxRow+1):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        return False
        
```
