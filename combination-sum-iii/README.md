# 216. Combination Sum III

## Medium

***

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

* Only numbers `1` through `9` are used.
* Each number is used **at most once**.

Return _a list of all possible valid combinations_. The list must not contain the same combination twice, and the combinations may be returned in any order.

&#x20;

**Example 1:**

```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
```

**Example 2:**

```
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
```

**Example 3:**

```
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
```

&#x20;

**Constraints:**

* `2 <= k <= 9`
* `1 <= n <= 60`

**Solution**

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        l = [1,2,3,4,5,6,7,8,9]
        def recursion(l, k ,start, n, path):
            if len(path) > k:
                return
            if  sum(path) == n and len(path) == k:
                result.append(path[:])
                return
            for index in range(start, len(l)):
                if index > start and l[index] == l[index-1]:
                    continue
                num = l[index]
                path.append(num)
                recursion(l, k, index+1, n, path)
                path.pop()
        recursion(l, k, 0, n, [])
        return result
```
