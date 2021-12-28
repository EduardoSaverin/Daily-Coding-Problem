# 46. Permutations

## Medium

***

Given an array `nums` of distinct integers, return _all the possible permutations_. You can return the answer in **any order**.

&#x20;

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

```python
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recursion(nums, temp, result):
            if not nums:
                result.append(temp)
            for index in range(len(nums)):
                recursion(nums[:index] + nums[index+1:], temp + [nums[index]], result)
        recursion(nums, [], result)
        return result
```
