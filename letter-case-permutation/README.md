# 784. Letter Case Permutation

## Medium

***

Given a string `s`, we can transform every letter individually to be lowercase or uppercase to create another string.

Return _a list of all possible strings we could create_. You can return the output in **any order**.

&#x20;

**Example 1:**

```
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```

**Example 2:**

```
Input: s = "3z4"
Output: ["3z4","3Z4"]
```

**Example 3:**

```
Input: s = "12345"
Output: ["12345"]
```

**Example 4:**

```
Input: s = "0"
Output: ["0"]
```

&#x20;

**Constraints:**

* `s` will be a string with length between `1` and `12`.
* `s` will consist only of letters or digits.

```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        result = set()
        def recursion(s, ele, start, result):
            if start >= len(s):
                result.add(ele)
                return
            for index in range(start, len(s)):
                recursion(s, ele[:index] + ele[index].upper() + ele[index+1:], index+1, result)
                recursion(s, ele, index+1, result)
        recursion(s,s,0, result)
        return list(result)
```
