# 1446. Consecutive Characters

## Easy

***

The **power** of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string `s`, return _the **power** of_ `s`.

&#x20;

**Example 1:**

```
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
```

**Example 2:**

```
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
```

**Example 3:**

```
Input: s = "triplepillooooow"
Output: 5
```

**Example 4:**

```
Input: s = "hooraaaaaaaaaaay"
Output: 11
```

**Example 5:**

```
Input: s = "tourist"
Output: 1
```

&#x20;

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of only lowercase English letters.

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def recursion(n, k, start=1, temp=[]):
            nonlocal result
            if k <= 0:
                result.append(list(temp))
                return temp
            for index in range(start, n+1):
                temp.append(index)
                # if (k-1) == 0:
                #     result.append(list(temp))
                t = recursion(n, k-1,index+1, temp)
                temp.pop()
        recursion(n,k,1,[])
        return resultcode
```
