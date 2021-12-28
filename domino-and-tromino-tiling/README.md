# 790. Domino and Tromino Tiling

## Medium

***

You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may rotate these shapes.

![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

Given an integer n, return _the number of ways to tile an_ `2 x n` _board_. Since the answer may be very large, return it **modulo** `109 + 7`.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg)

```
Input: n = 3
Output: 5
Explanation: The five different ways are show above.
```

**Example 2:**

```
Input: n = 1
Output: 1
```

&#x20;

**Constraints:**

* `1 <= n <= 1000`

```python
class Solution:
    def __init__(self):
        self.MOD = 1000000007
        
    def numTilings(self, n: int) -> int:
        d = {}
        d[1] = 1 # For n=1 Just one Solution
        d[2] = 2 # For n=2 2 ways exists
        d[3] = 5 # For n=3 5 ways as given in question example 1
        d[1.5] = 1 # We know this from Tromino tile
        result = self.countTiles(n, d)
        return result
    
    def countTiles(self, n:int, d):
        if n in d:
            return d[n]
        if n < 1:
            return 0
        count = 0
        if n%1 == 0:
            # This case means no half point tile coming out and it is full rectangle till now
            # Not Three Cases Are there
            # Case 1 : One Vertical Domino
            # Case 2 : 2 Horizontal Domino
            # Case 3 : One Tromino, Here we can multiply by 2 since we can place this in two ways. Notice -1.5 because tromino will occupy 1.5 space
            count = (self.countTiles(n-1, d) + self.countTiles(n-2, d) + 2*self.countTiles(n-1.5, d)) % self.MOD
        else:
            # Here we can apply either Case 1 or Case 3 (only one time because we have to fill 0.5 space also and that can be one in one way only) only
            count = (self.countTiles(n-1, d) + self.countTiles(n-1.5, d)) % self.MOD
        d[n] = count
        return count
```
