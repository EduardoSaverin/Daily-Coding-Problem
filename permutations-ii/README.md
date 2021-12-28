# 47. Permutations II

## Medium

***

Given a collection of numbers, `nums`, that might contain duplicates, return _all possible unique permutations **in any order**._

&#x20;

**Example 1:**

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 8`
* `-10 <= nums[i] <= 10`

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def recursion(nums, temp, result):
            if not nums:
                result.append(temp)
            for index in range(len(nums)):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                recursion(nums[:index] + nums[index+1:], temp + [nums[index]], result)
        recursion(nums, [], result)
        return result
```
