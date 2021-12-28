# 70. Climbing Stairs

## Easy

***

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

&#x20;

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

&#x20;

**Constraints:**

* `1 <= n <= 45`

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def recursion(n, d):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in d:
                return d[n]
            sum = recursion(n-1, d) + recursion(n-2, d)
            d[n] = sum
            return sum
        return recursion(n, d)
```
