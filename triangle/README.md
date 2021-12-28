# 120. Triangle

## Medium

***

Given a `triangle` array, return _the minimum path sum from top to bottom_.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

&#x20;

**Example 1:**

```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
```

**Example 2:**

```
Input: triangle = [[-10]]
Output: -10
```

&#x20;

**Constraints:**

* `1 <= triangle.length <= 200`
* `triangle[0].length == 1`
* `triangle[i].length == triangle[i - 1].length + 1`
* `-104 <= triangle[i][j] <= 104`

&#x20;

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Move from Bottom to UP
        # For Second row from bottom update minimum in that row using its below row
        # Same goes for its upper rows
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                # For Row 2 Column 0 <--- Min(Row 3 Column 0, Row 3 Column 1)
                # In Same way do for other columns in same row, then ,move to upper row
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
```
