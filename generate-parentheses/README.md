# 22. Generate Parentheses

## Medium

***

Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

&#x20;

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```

&#x20;

**Constraints:**

* `1 <= n <= 8`

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursion(start, end, path):
            if start == 0 and end == 0:
                result.append(path[:])
            if start > 0:
                recursion(start-1, end, path + '(')
            if end > 0 and end > start:
                recursion(start, end-1, path + ')')
        recursion(n,n,'')
        return result
```
